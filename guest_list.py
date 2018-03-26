# This file contains the definition of class GuestList
from user_details import UserDetails
from collections import namedtuple

class GuestList:

    def __init__(self, _all_users, _host_latitude, _host_longitude):
        '''
        Class to store a list of Guests for a specific event being held at a specific location
        Input args: 
        1. List of UserDetails Objects containing information about users
        2. float : Event location latitude 
        3. float : Event location longitude
        '''

        # Party Venue coordinates
        self.latitude = _host_latitude
        self.longitude = _host_longitude

        # max allowed distance from venue
        self.max_distance = 0

        # Dictionary for looking up user details by id
        self.user_lookup = {}

        # list to store a tuple <user_id, distance from venue>
        # list will be sorted by distance from venue
        self.id_sorted_by_distance = []

        # declaring a namedtuple to store userid->distance pair
        ID_Distance = namedtuple('ID_Distance', ['user_id', 'distance'])

        for user in _all_users:
            user_distance = user.get_distance_from_pt(_host_latitude, _host_longitude)
            user_id_and_distance = ID_Distance(user.user_id, user_distance)
            self.id_sorted_by_distance.append(user_id_and_distance)
            self.user_lookup[user.user_id] = user

        # sort the guest list based on distance, for optimized fetching
        self.id_sorted_by_distance.sort(key=lambda x: x.distance)

    def add_user(self, name, id, lat, lon):
        '''
        Add a single user at a time to the party list
        This does not guarantee an invitation
        Inpur args:
        1. name, string
        2. id, integer
        3. latitude, float
        4. longitude, float
        return 
         True on successfull addition
         False on no addition
        '''
        if (id in self.user_lookup):
            print('ID already exists, Fake ID !!')
            return False
        
        user = UserDetails(name, id, lat, lon)
        self.user_lookup[user.user_id] = user
        # sort the list based on distance, for optimized fetching
        # array is not very efficient, if huge number of users (millions) should probably use a link list
        user_distance = user.get_distance_from_pt(_host_latitude, _host_longitude)
        user_id_and_distance = ID_Distance(user.user_id, user_distance)
        self.id_sorted_by_distance.append(user_id_and_distance)
        self.id_sorted_by_distance.sort(key=lambda x: x.distance)
        return True
        
    def set_maximum_distance_from_venue(self, max_distance):
        '''
        Set the distance from the venue within which people are allowed to come
        People situated farther than this distance will not be invited
        Args: 1. float, distance value 
        '''
        self.max_distance = max_distance

    def get_guests_closer_than(self, max_distance):
        '''
        Get users within range
        Assuming here the range you need is inclusive of max_distance
        input args: 1. +ve or zero float value, i.e the maximum distance allowed of a guest from the reference point
        return value : list of UserDetails objects that are located less than or exactly max_distance away
        '''
        close_users = []
        try:
            valid_max_distance = float(max_distance)
            if (valid_max_distance < 0.0):
                print("Enter a valid positive (integer or float) maximum distance value, entered value[{}] is invalid !".format(max_distance))
                return close_users
        except ValueError:
            print("Enter a valid positive (integer or float) maximum distance value, entered value[{}] is invalid !".format(max_distance))
            return close_users

        for user in self.id_sorted_by_distance:
            distance = user.distance
            if (distance <= valid_max_distance):
                close_users.append(user.user_id)
            else:
                # since list is sorted by distance, rest of the users are located farther 
                break
        return close_users

    def get_users_invited_to_party(self):
        '''
        Get list of users invited to party
        '''
        invited_guests = self.get_guests_closer_than(self.max_distance)
        return invited_guests

    def get_users_excluded_from_party(self):
        '''
        Get list of users not invited to party
        '''
        # get the list of invited guests
        invited_guests = self.get_guests_closer_than(self.max_distance)
        invited_guest_lookup = {}
        for user_id in invited_guests:
            invited_guest_lookup[user_id] = 0

        # loop over all users and store the ones that were not invited :(
        excluded_users = []
        for key in self.user_lookup:
            if key not in invited_guest_lookup:
                excluded_users.append(key)
        return excluded_users

    def print_full_guest_list(self):
        '''
        Helper function to print all user data for debugging purposes
        '''
        for user in self.user_list:
            print("{}".format(user.distance))
        
    def print_selected_guest_list(self, guest_list):
        '''
        To print a list of users sorted by ID, in format :
        Name [xxx yy] ID [xx] 
        input args: list of pairs <UserDetails, distance>
        '''
        NameID = namedtuple('NameID', ['name','user_id'])
        list_to_print = []
        for id in guest_list:
            name = self.user_lookup[id].name
            list_to_print.append(NameID(name, id))

        # sort the list
        list_to_print.sort(key=lambda x: x.user_id)
        # print in the needed format 
        for x in list_to_print:
            print("Name [{}], ID [{}]".format(x.name, x.user_id))
