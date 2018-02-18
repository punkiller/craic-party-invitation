# This file contains the definition of the class UserDetails

# imports to calculate distances of users from a reference point
from math import sin, cos, radians, acos

EARTH_RADIUS = 6371.0 # kilometers

# class for a User, will contain all information pertaining to a user
class UserDetails(object):
    def __init__(self, _name, _user_id, _latitude, _longitude):
        '''
        stores members : user name, user id, latitude in radians and longitude in radians.
        The class will be used to store user details in its members and 
        will have ability to calculate a users distance from a certain point on the earth.
        An object of this class can be constructed from a Json block containing the required member information
        '''
        
        self.name = _name
        self.user_id = _user_id
        self.radian_latitude  = radians(_latitude)
        self.radian_longitude = radians(_longitude)
 
    def print(self):
        print(self.name)
        print(self.user_id)
        print(self.radian_latitude)
        print(self.radian_longitude)

    def get_distance_from_pt(self, reference_latitude, reference_longitude):
        '''
        Member function to calculate the user's distance from a reference point on the earth
        Input args: 
            1. reference point latitude in degrees, Type : float (+ve or -ve)
            2. reference point longitude in degrees, Type : float (+ve or -ve)
        Return value:
            distance from reference point in kilometers, Type: +ve float number
        '''
        radian_reference_latitude = radians(reference_latitude)
        radian_reference_longitude = radians(reference_longitude)
        
        # using first formula from Wikipedia page to calculate distance
        # https://en.wikipedia.org/wiki/Great-circle_distance

        longitude_delta = self.radian_longitude - radian_reference_longitude
        central_angle =   acos( 
            sin(self.radian_latitude) * sin(radian_reference_latitude) 
                + cos(self.radian_latitude) * cos(radian_reference_latitude) * cos(longitude_delta)
            )

        distance_from_reference = EARTH_RADIUS * central_angle
        return distance_from_reference
    
    @classmethod
    def from_json(self, json_dict):
        '''
        Method to contruct a UserDetails object from a json encoded line
        input args: 1. json encoded line containing relevant user details
        '''
        if all (keys in json_dict for keys in ('name', 'user_id', 'latitude', 'longitude')):
            return UserDetails(json_dict['name'], json_dict['user_id'], float(json_dict['latitude']), float(json_dict['longitude']))