# This file contains the Unit Tests for the party invitations project

import unittest
import math

import ingest_file
from user_details import UserDetails
from guest_list import GuestList

class TestDublin(unittest.TestCase) :

    def setUp(self):

        self.all_user_list = 'inputFiles/gistfile.txt'
        self.small_user_list = 'inputFiles/small_list.txt'
        self.three_valid_list = 'inputFiles/three_valid_users.txt'

        self.reference_latitude = 53.339428
        self.reference_longitude = -6.257664
    
    def test_good_json_file_load(self):
        '''
        Loading the full list of 32 users 
        checking if all 32 users loaded
        '''
        print("\n=====Running Test=====")
        print("File containing 32 users")
        print("======================")
        json_data = ingest_file.IngestJSONLines(self.all_user_list)
        self.assertEqual(len(json_data), 32)
    
    def test_out_of_range_guests(self):
        '''
        Test if list if sorted
        '''
        print("\n=====Running Test=====")
        print("File containing 32 users, Sorted ??")
        print("======================")
        json_data = ingest_file.IngestJSONLines(self.all_user_list)
        guests = GuestList(json_data, self.reference_latitude, self.reference_longitude)
        
        guests_in_range = guests.get_guests_closer_than(150)
        for guest in guests_in_range:
            self.assertEqual( guest[1] <= 150, True)

        guests_in_range = guests.get_guests_closer_than(20)
        for guest in guests_in_range:
            self.assertEqual( guest[1] <= 20, True)

        guests_in_range = guests.get_guests_closer_than(1000)
        for guest in guests_in_range:
            self.assertEqual( guest[1] <= 1000, True)

        guests_in_range = guests.get_guests_closer_than(0)
        for guest in guests_in_range:
            self.assertEqual( guest[1] <= 0, True)
        
    def test_distance_calculations(self):
        '''
        To test the distance calculation
        Checking all distance values in small_list.txt file
        '''
        print("\n=====Running Test=====")
        print("Distance calculation tests")
        print("======================")
        json_data = ingest_file.IngestJSONLines(self.small_user_list)
        guests = GuestList(json_data, self.reference_latitude, self.reference_longitude)
        # pre computed list verified from the web
        correct_distance_list = [0.0, 0.17, 0.81, 100.44, 11516.88]
        
        for itr in range(5):
            dist_compare = math.isclose(guests.user_list[itr].distance, correct_distance_list[itr], abs_tol= 0.01)
            print('{},{}, {}'.format(guests.user_list[itr].distance,correct_distance_list[itr], dist_compare ))
            self.assertEqual(dist_compare, True)
    
    def test_bad_json_file_load(self):
        '''
        File does not exist
        '''
        print("\n=====Running Test=====")
        print("File does not exist")
        print("======================")
        json_data = ingest_file.IngestJSONLines("file_does_not_exist")
        self.assertEqual(len(json_data), 0)
    
    def test_three_users(self):
        '''
        Only 3 valid users present in file
        '''
        print("\n=====Running Test=====")
        print("Only 3 valid users")
        print("======================")
        json_data = ingest_file.IngestJSONLines(self.three_valid_list)
        self.assertEqual(len(json_data), 3)

if __name__ == "__main__":
       unittest.main()
