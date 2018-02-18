# craic-party-invitation

To invite people to a party using their latitude and longitude coordinates

Using some people records in a text file (/inputFiles) -- one customer per line, JSON-encoded. 

You can invite any person within any specific distance of your location for some food and drinks.

This program that will read the full list of friends and output the names and ids of matching friends (within X kms), sorted by ID (ascending).


The program flow:

Ingest_file will read the input file of records of UserDetails and store it into a GuestList Object

Now using the interface of GuestList object
you can get users within 100 km and pass this list to a function of the same object to print them in order of their IDs

Classes:

  UserDetails

  GuestList
