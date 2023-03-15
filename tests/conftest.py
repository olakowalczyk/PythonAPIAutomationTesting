import pytest
import json

from common.bookings import Bookings
from utils.http_manager import HttpManager


@pytest.fixture(scope="session")
def token():
    """
    Returns token which will be used (as a fixture) 
    in the test functions that require authentication
    """
    HttpManager.auth(f'{Bookings.BASE_URL}/auth', 'admin', 'password123')
    return HttpManager.headers["Cookie"].split('=')[1]


@pytest.fixture()
def existing_booking(): 
    url = f'{Bookings.BASE_URL}/booking/'
    booking_id = str(Bookings.get_random_booking())
    return url + booking_id


@pytest.fixture()
def json_for_create_booking():
    return json.dumps({
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    })
