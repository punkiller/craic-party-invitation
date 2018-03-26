# The Unit Tests for the party invitations project

import unittest
import math

import ingest_file
from user_details import UserDetails
from guest_list import GuestList

class InvitationTests(unittest.TestCase) :

    def setUp(self):

        self.all_user_list = 'inputFiles/gistfile.txt'
        self.small_user_list = 'inputFiles/small_list.txt'
        self.three_valid_users_list = 'inputFiles/three_valid_users.txt'

        self.reference_latitude = 53.339428
        self.reference_longitude = -6.257664
    
    def test_if_excluded_users_are_far(self):
        '''
        Test if users that were not invited are really farther than max disatnce
        '''
        print("\n=====Running Test=====")
        print("Checking if users not invited are all outside the distance range")
        print("======================")
        json_data = ingest_file.IngestJSONLines(self.all_user_list)
        guests = GuestList(json_data, self.reference_latitude, self.reference_longitude)
        
        test_distances = [150, 20, 1000, 0]
        for sample_dist in test_distances:
            guests.set_maximum_distance_from_venue(sample_dist)
            excludeds = guests.get_users_excluded_from_party()
            for id in excludeds:
                distance = guests.user_lookup[id].get_distance_from_pt(self.reference_latitude, self.reference_longitude)
                self.assertGreater(distance, sample_dist)

    def test_if_guests_within_range(self):
        '''
        Test if users invited are really within range
        '''
        print("\n=====Running Test=====")
        print("Checking if invited users are really within range")
        print("======================")
        json_data = ingest_file.IngestJSONLines(self.all_user_list)
        guests = GuestList(json_data, self.reference_latitude, self.reference_longitude)
        
        test_distances = [150, 20, 1000, 0]
        for sample_dist in test_distances:
            guests.set_maximum_distance_from_venue(sample_dist)
            inviteds = guests.get_users_invited_to_party()
            for id in inviteds:
                distance = guests.user_lookup[id].get_distance_from_pt(self.reference_latitude, self.reference_longitude)
                self.assertLessEqual(distance, sample_dist)
        
    def test_distance_calculations(self):
        '''
        To test the distance calculation
        Checking all distance values in small_list.txt file
        '''
        print("\n=====Running Test=====")
        print("Distance calculation tests")
        print("======================")
        
        #{"latitude": "52.46", "user_id": 7, "name": "Julio Jones", "longitude": "-6.6"}
        Julio = UserDetails("Julio", 7, 52.46, -6.6)
        distance = Julio.get_distance_from_pt(self.reference_latitude, self.reference_longitude)
        dist_compare = math.isclose(distance, 100.45, abs_tol= 0.01)
        print('{} == {}, {}'.format(distance, 0.0, dist_compare))
        self.assertTrue(dist_compare)

        #{"latitude": "-50.0", "user_id": 6, "name": "Fernando Torres", "longitude": "2.0"}
        Torres= UserDetails("Torres", 6, -50.00, 2.00)
        distance = Torres.get_distance_from_pt(self.reference_latitude, self.reference_longitude)
        dist_compare = math.isclose(distance, 11516.88, abs_tol= 0.01)
        print('{} == {}, {}'.format(distance, 11516.88, dist_compare))
        self.assertTrue(dist_compare)
        
        #{"latitude": "53.339428", "user_id": 5, "name": "Barack Obama", "longitude": "-6.27"}
        Obama = UserDetails("Obama", 5, 53.339428, -6.27)
        distance = Obama.get_distance_from_pt(self.reference_latitude, self.reference_longitude)
        dist_compare = math.isclose(distance, 0.819, abs_tol= 0.01)
        print('{} == {}, {}'.format(distance, 0.819, dist_compare))
        self.assertTrue(dist_compare)

        #{"latitude": "53.339428", "user_id": 3, "name": "Niraj Yadav", "longitude": "-6.257664"}
        Niraj = UserDetails("Niraj", 3, 53.339428, -6.257664)
        distance = Niraj.get_distance_from_pt(self.reference_latitude, self.reference_longitude)
        dist_compare = math.isclose(distance, 0.0, abs_tol= 0.01)
        print('{} == {}, {}'.format(distance, 0.0, dist_compare))
        self.assertTrue(dist_compare)

        #{"latitude": "53.339428", "user_id": 10, "name": "Pankaj Yadav", "longitude": "-6.255"}
        Pankaj = UserDetails("Pankaj", 10, 53.339428, -6.255)
        distance = Pankaj.get_distance_from_pt(self.reference_latitude, self.reference_longitude)
        dist_compare = math.isclose(distance, 0.18, abs_tol= 0.01)
        print('{} == {}, {}'.format(distance, 0.18, dist_compare))
        self.assertTrue(dist_compare)

if __name__ == "__main__":
       unittest.main()
