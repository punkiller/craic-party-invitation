# Craic Party Invitation

A Party management system that can be used to generate a guest list, based on how far they are from the party.
The distance of a person is determined by their GPS coordinates (latitude and longitude).
The user list can be input through a File, containig JSON encoded user data.
For example files see : (/inputFiles). 

This program that will read the full list of friends and output the names and ids of matching friends (within X kms), sorted by ID (ascending).

## Getting Started

You need to download the source
```
git clone https://github.com/punkiller/craic-party-invitation.git
```
run 
```
$ ./guest_list_generator.py
```
The above command default distance 100km from latitude 53.339428, longitude 6.257664, input file 'inputFiles/gistfile.txt'

for help use : 
```
./guest_list_generator --help
```
```
$ ./guest_list_generator.py --help
usage: guest_list_generator.py [-h] [-m MAX_DISTANCE]
                               [-lat REFERENCE_LATITUDE]
                               [-lon REFERENCE_LONGITUDE] [-f INPUT_FILE]

optional arguments:
  -h, --help            show this help message and exit
  -m MAX_DISTANCE       the maximum dist that a GUEST can be invited from i.e
                        -m 25
  -lat REFERENCE_LATITUDE
                        the latitude in degrees of the HOST's coordinates use
                        +ve for North, -ve for South
  -lon REFERENCE_LONGITUDE
                        the longitude in degrees of the HOST's coordinates use
                        +ve for East, -ve for West
  -f INPUT_FILE         Path to the input file containing json encoded user
                        data

```
## Examples

Example input file line format :
{"latitude": "53.1229599", "user_id": 6, "name": "Theresa Enright", "longitude": "-6.2705202"}
Taken from file :
craic-party-invitation/inputFiles/gistfile.txt

 How to generate list of guests 200km or less distance away from craic party
```
Pankajs-MacBook-Pro:Party_Invitations pankajyadav$ ./guest_list_generator.py -m 2000  

Ingested User Data for [32] users from file [inputFiles/gistfile.txt]
Name [Alice Cahill], ID [1]
Name [Ian McArdle], ID [2]
Name [Jack Enright], ID [3]
Name [Ian Kehoe], ID [4]
Name [Nora Dempsey], ID [5]
Name [Theresa Enright], ID [6]
Name [Frank Kehoe], ID [7]
Name [Eoin Ahearn], ID [8]
Name [Jack Dempsey], ID [9]
Name [Georgina Gallagher], ID [10]
Name [Richard Finnegan], ID [11]
Name [Christina McArdle], ID [12]
Name [Olive Ahearn], ID [13]
Name [Helen Cahill], ID [14]
Name [Michael Ahearn], ID [15]
Name [Ian Larkin], ID [16]
Name [Patricia Cahill], ID [17]
Name [Bob Larkin], ID [18]
Name [Enid Cahill], ID [19]
Name [Enid Enright], ID [20]
Name [David Ahearn], ID [21]
Name [Charlie McArdle], ID [22]
Name [Eoin Gallagher], ID [23]
Name [Rose Enright], ID [24]
Name [David Behan], ID [25]
Name [Stephen McArdle], ID [26]
Name [Enid Gallagher], ID [27]
Name [Charlie Halligan], ID [28]
Name [Oliver Ahearn], ID [29]
Name [Nick Enright], ID [30]
Name [Alan Behan], ID [31]
Name [Lisa Ahearn], ID [39]
```
 How to generate list of guests 25km or less distance away from craic party
```
Pankajs-MacBook-Pro:Party_Invitations pankajyadav$ ./guest_list_generator.py -m 25  

Ingested User Data for [32] users from file [inputFiles/gistfile.txt]

Name [Ian Kehoe], ID [4]
Name [Nora Dempsey], ID [5]
Name [Theresa Enright], ID [6]
```
 How to generate list of guests 50km or less away from craic party
```
Pankajs-MacBook-Pro:Party_Invitations pankajyadav$ ./guest_list_generator.py -m 50

Ingested User Data for [32] users from file [inputFiles/gistfile.txt]

Name [Ian Kehoe], ID [4]
Name [Nora Dempsey], ID [5]
Name [Theresa Enright], ID [6]
Name [Richard Finnegan], ID [11]
Name [Christina McArdle], ID [12]
Name [Michael Ahearn], ID [15]
Name [Alan Behan], ID [31]
Name [Lisa Ahearn], ID [39]
```
 How to generate list of guests 100km or less distance away from craic party
```
Pankajs-MacBook-Pro:Party_Invitations pankajyadav$ ./guest_list_generator.py -m 100

Ingested User Data for [32] users from file [inputFiles/gistfile.txt]

Name [Ian Kehoe], ID [4]
Name [Nora Dempsey], ID [5]
Name [Theresa Enright], ID [6]
Name [Eoin Ahearn], ID [8]
Name [Richard Finnegan], ID [11]
Name [Christina McArdle], ID [12]
Name [Olive Ahearn], ID [13]
Name [Michael Ahearn], ID [15]
Name [Patricia Cahill], ID [17]
Name [Eoin Gallagher], ID [23]
Name [Rose Enright], ID [24]
Name [Stephen McArdle], ID [26]
Name [Oliver Ahearn], ID [29]
Name [Nick Enright], ID [30]
Name [Alan Behan], ID [31]
Name [Lisa Ahearn], ID [39]
```
### Prerequisites

You should have python3 installed 
No other special modules are required

## Running the tests
```
Pankajs-MacBook-Pro:Party_Invitations pankajyadav$ python3 -m unittest discover <path-to-test-directory> -p '*.py'
Pankajs-MacBook-Pro:Party_Invitations pankajyadav$ python3 -m unittest discover tests -p '*.py'
```
### Break down of tests

There are two test files 
```
tests/file_import_tests.py : Tests import of files, this is expected to be the preferred method of loading user data
tests/basic_tests.py : Test the functionality of the project.
```
file_import_tests 
```
test_good_json_file_load
This test loads file inputFiles/gistfile.txt,
containing 32 valid lines, 
it checks if 32 users have been entered into the system

test_bad_json_file_load
This test tries to load a non existent file and fails, 
making sure that system prints an error statement and exits gracefully, 
while having entered 0 registered users

test_three_users
This test loads file inputFiles/three_valid_users.txt, 
the file contains some bad lines, 
so it will print error messages for the bad lines, 
but continue processing and input the 3 valid users into the system
```
basic_tests
```
test_if_excluded_users_are_far
Gets a list of users that are not invited,
and checks if their distance from the craic party is,
greater than the maximum distance allowed for the party

test_if_guests_within_range
Gets a list of the invited guests and checks if they are located within the maximum distance  allowed for the party

test_distance_calculations
Has a fixed set of users whose coordinates are known and distances have been confirmed, their distances and calculated by the craic party invitation system and compared to their known distance within 0.01 km of acceptable tolerance.
```
## Author

* **Pankaj Yadav**
