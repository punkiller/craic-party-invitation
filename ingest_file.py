# This file contains the functionality to import files containing user data into the project

import json
import user_details

def IngestJSONLines (file_name):
    '''
    function that will import file with lines of the JSON format 
    input args : 1. the path of the file 
    file format : sample line : {"latitude": "-50.0", "user_id": 6, "name": "Fernando Torres", "longitude": "2.0"}
    '''
    
    user_list = []
    try:
        with open(file_name) as fp_users:
            for line in fp_users:
                # remove leading and trailing spaces from the line
                line.strip()
                # checking for a blank line
                if line in ('\n', '\r\n'):
                    continue
                # loading a json line
                try:
                    current_user = json.loads(line, object_hook=user_details.UserDetails.from_json)    
                except ValueError as e:
                    print("Check the JSON, decoding error ({}).\nFound in line [{}]".format(e, line))
                    continue
                # check if able to get user details from decoded json line
                if (current_user):
                    user_list.append(current_user)
                else:
                    print("Check if all user information is present in this line [{}]".format(line))
    
    except IOError as e:
        print("Json File Input Error ({} : {})".format(e.errno, e.strerror))
        print("Check file [{}]".format(file_name))

    print ("\nIngested User Data for [{}] users from file [{}]".format(len(user_list), file_name))
    return user_list

