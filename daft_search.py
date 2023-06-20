import time
import pygame
from daftlistings import Daft, Location, SearchType, PropertyType
from pprint import pprint

# Initialize mixer and load mp3
pygame.mixer.init()
pygame.mixer.music.load("BEEPTimer_Digital_watch.mp3")

# Create a set to hold the ids of listings we've already seen
seen_listings = set()

while True:
    daft = Daft()
    daft.set_location(Location.DUBLIN)
    daft.set_search_type(SearchType.RESIDENTIAL_RENT)
    daft.set_property_type(PropertyType.HOUSE)
    daft.set_min_baths(2)
    daft.set_min_beds(3)
    daft.set_max_price(2400)

    listings = daft.search()

    for listing in listings:
        listing_dict = listing.as_dict()
        
        # Filter out listings with less than 2 bathrooms
        num_baths = int(listing_dict.get('numBathrooms', '0 Bath').split()[0])
        if num_baths < 2:
            continue

        if listing_dict['id'] not in seen_listings:
            # pprint(listing_dict)
            print()
            print("URL:", listing.daft_link)
            print("---------------------------------")
            seen_listings.add(listing_dict['id'])
            pygame.mixer.music.play()

    # Wait for 5 minutes (300 seconds)
    time.sleep(15)
