#!/usr/bin/env python3

# Main program to generate a guest list for a party
# Defaults have been provided for a distacne of 100km 
# # from given reference location [53.339428, -6.257664]

import argparse

import ingest_file
from user_details import UserDetails
from guest_list import GuestList

def main():
    '''
        Main function to run to generate a list of Users i.e Guests sorted by ID for an event
        input args :
        1. -m : float, max distance from the event coordinates in kilometers, default = 100
        2. -lat : float, the latitude of the event location, default = 53.339428
        3. -lon : float, the longitude of the event location, default = -6.257664
    '''
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
    parser.add_argument("-f", dest="input_file", type=str,
                        help="Path to the input file containing json encoded user data",
                        default='inputFiles/gistfile.txt')
    args = parser.parse_args()

    all_users = []

    # example line format
    # {"latitude": "53.1229599", "user_id": 6, "name": "Theresa Enright", "longitude": "-6.2705202"}
    all_users = ingest_file.IngestJSONLines(args.input_file)
    if (len(all_users) == 0):
        print("No users found in file, Exiting !!")
    
    # Get and Store all guest details for the party
    guests = GuestList(all_users, args.reference_latitude, args.reference_longitude)
    
    # get the guests within range of party in kilometers 
    guests_in_range = guests.get_guests_closer_than(args.max_distance)
    
    # print the guests in ascending order of their ID
    guests.print_selected_guest_list(guests_in_range)

if __name__ == "__main__":
    # execute only if run as a script
    main()

