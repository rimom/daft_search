# Daft Search

This is a Python script that uses the `daftlistings` package to search for residential rental properties on Daft.ie that meet certain criteria, such as location, property type, minimum number of bathrooms, minimum number of bedrooms, and maximum price. When it finds a new listing that matches the criteria, it plays a sound and prints the URL of the listing.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/daft_search.git
    cd daft_search
    ```

2. Install the required packages:
    ```bash
    python -m pip install daftlistings pygame
    ```

## Usage

To run the script, use the following command:
    ```bash
    python daft_search.py
    ```

The script will run indefinitely, checking for new listings every minute. When it finds a new listing that matches the criteria, it will play a sound and print the URL of the listing. 

To stop the script, simply press `Ctrl+C`.

## Customization

You can customize the search criteria by editing the `daft_search.py` file. The following options are available:

- `set_location(Location.DUBLIN)`: Change `DUBLIN` to your desired location.
- `set_search_type(SearchType.RESIDENTIAL_RENT)`: Change `RESIDENTIAL_RENT` to your desired search type.
- `set_property_type(PropertyType.HOUSE)`: Change `HOUSE` to your desired property type.
- `set_min_baths(2)`: Change `2` to your desired minimum number of bathrooms.
- `set_min_beds(3)`: Change `3` to your desired minimum number of bedrooms.
- `set_max_price(2400)`: Change `2400` to your desired maximum price.

## Note

This script uses the `pygame` library to play a sound when a new listing is found. Make sure your system has the necessary dependencies to run `pygame`.
