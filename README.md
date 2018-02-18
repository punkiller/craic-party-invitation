# craic-party-invitation

To invite people to a party using their latitude and longitude coordinates

Using some people records in a text file (/inputFiles) -- one customer per line, JSON-encoded. 

You can invite any person within any specific distance of your location for some food and drinks.

This program that will read the full list of friends and output the names and ids of matching friends (within X kms), sorted by ID (ascending).



First Look at guest_list_generator.py :

Ingest_file will read the input file of records of UserDetails and return a list of UserDetails Objects.

**UserDetails[]

This is now used to create a GuestList Object

**GuestList ( UserDetails[], party_latitude, party_longitude)

Now using a member function of GuestList object you can get users and their distances within 100 km.

**GuestList.get_guests_closer_than(X kilometers )

Now pass this list to a member function of GuestList print them in order of their IDs

**GuestList.print_selected_guest_list(list of <UserDetails, distance>)
