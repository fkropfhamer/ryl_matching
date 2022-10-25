from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator = Nominatim(user_agent="app")

def distance(address1, address2):
    cord1 = address_to_cord(address1)
    cord2 = address_to_cord(address2)

    return geodesic(cord1, cord2).km


def address_to_cord(address):
    cord = geolocator.geocode(address)

    return cord.point


def create_address(street: str, postalcode: str, city='münchen', country='germany'):
    return {
        'street': street,
        'city': city,
        'country': country,
        'postalcode': postalcode
    }

school_addresses = {
    'Mittelschule Fürstenrieder Straße': create_address(street='1 Geschwister-Scholl-Platz', postalcode='80539')
}


def get_school_address(school: str):
    if school in school_addresses:
        return school_addresses[school]
    
    print(f"No address for school {school} found")

    return None


if __name__ == '__main__':
    address1 = create_address(
        street='21 Arcisstraße',
        postalcode='80333'
    )

    address2 = create_address(
        street='1 Geschwister-Scholl-Platz',
        postalcode='80539'
    )

    print(distance(address1, address2))
