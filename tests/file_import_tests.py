
import unittest

import ingest_file
from user_details import UserDetails

class TestFileImport(unittest.TestCase) :

    def setUp(self):

        self.all_user_list = 'inputFiles/gistfile.txt'
        self.small_user_list = 'inputFiles/small_list.txt'
        self.three_valid_users_list = 'inputFiles/three_valid_users.txt'

    
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
        print("Only 3 valid users in file, A few erroneous lines expected ...")
        print("Should print an error msg per bad line, and not crash")
        print("======================")
        json_data = ingest_file.IngestJSONLines(self.three_valid_users_list)
        self.assertEqual(len(json_data), 3)

if __name__ == "__main__":
       unittest.main()
