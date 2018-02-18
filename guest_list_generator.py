#!/usr/bin/python
# Main program to generate a guest list for a specific event
# Defaults have been provided for a distacne of 100km 
# # from given reference location [53.339428, -6.257664]

import argparse

import ingest_file
from user_details import UserDetails
from guest_list import GuestList

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", dest="max_distance", type=int,
                        help="the maximum dist that a GUEST can be invited from i.e -m 25 ",
                        default=100)
    parser.add_argument("-lat", dest="reference_latitude", type=float,
                        help="the latitude in degrees of the HOST's coordinates\n use +ve for North, -ve for South",
                        default=53.339428)
    parser.add_argument("-lon", dest="reference_longitude", type=float,
                        help="the longitude in degrees of the HOST's coordinates\n use +ve for East, -ve for West",
                        default=-6.257664)
                        
    args = parser.parse_args()

    all_users = []

    all_users = ingest_file.IngestJSONLines("inputFiles/gistfile.txt")
    if (len(all_users) == 0):
        print("No users found in file, Exiting !!")
    
    # create a guest list for a party at a location
    guests = GuestList(all_users, args.reference_latitude, args.reference_longitude)
    
    # get the guest within range in kilometers 
    guests_in_range = guests.get_guests_closer_than(100)
    
    # print the guest in ascending order of their ID
    guests.print_selected_guest_list(guests_in_range)

if __name__ == "__main__":
    # execute only if run as a script
    main()

