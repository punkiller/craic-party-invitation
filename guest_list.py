# This file contains the definition of class GuestList
from user_details import UserDetails
from collections import namedtuple

class GuestList:

    def __init__(self, _all_users, _host_latitude, _host_longitude):
        '''
        Class to store a list of Guests for a specific event being held at a specific location
        Input args: 
        1. List of UserDetails Objects contianig information about users
        2. float : Event location latitude 
        3. float : Event location longitude
        '''

        self.latitude = _host_latitude
        self.longitude = _host_longitude

        # list to store a tuple <user_details, distance from party>
        # list is sorted by distance after filling up
        self.user_list = []
        UserDistance = namedtuple('UserDistance', ['user_details', 'distance'])
        
        for user in _all_users:
            user_distance = user.get_distance_from_pt(_host_latitude, _host_longitude)
            guest = UserDistance(user, user_distance)
            self.user_list.append(guest)

        # sort the guest list based on distance, for optimized fetching
        self.user_list.sort(key=lambda x: x.distance)

    def get_guests_closer_than(self, max_distance):
        '''
        Get users within range
        Assuming here the range you need is inclusive of max_distance
        input args: 1. +ve or zero float value, i.e the maximum distance allowed of a guest from the reference point
        return value : list of UserDetails objects that are located less than or exactly max_distance away
        '''
        selected_users = []
        try:
            valid_max_distance = float(max_distance)
            if (valid_max_distance < 0.0):
                print("Enter a valid positive (integer or float) maximum distance value, entered value[{}] is invalid !".format(max_distance))
                return selected_users
        except ValueError:
            print("Enter a valid positive (integer or float) maximum distance value, entered value[{}] is invalid !".format(max_distance))
            return selected_users

        for user in self.user_list:
            distance = user.distance
            if (distance > valid_max_distance):
                # since list is sorted by distance, rest of the users are located farther 
                break
            else:
                selected_users.append(tuple((user.user_details, distance)))
        return selected_users

    def print_full_guest_list(self):
        '''
        Helper function to print the list data for debugging purposes
        '''
        for user in self.user_list:
            print("{}".format(user.distance))
        
    def print_selected_guest_list(self, guest_list):
        '''
        To print a list of users in format : Name [xxx yy] ID [xx] sorted by ID
        input args: list of pairs <UserDetails, distance>
        '''
        NameID = namedtuple('NameID', ['name','user_id'])
        name_and_id = []
        for user_and_dist in guest_list:
            selected_guest = NameID(user_and_dist[0].name, user_and_dist[0].user_id)
            name_and_id.append(selected_guest)
        # sort the list 
        name_and_id.sort(key=lambda x: x.user_id)
        # print in the needed format 
        for x in name_and_id:
            print("Name [{}], ID [{}]".format(x.name, x.user_id))
