import requests
import json
from pyassert import *

from utils.http_manager import HttpManager
from common.bookings import Bookings

URL = f'{Bookings.BASE_URL}/booking/'
BOOKING = Bookings.get_random_booking()
UPDATE = 'Edited'

# GET Pre-request: Takes booking and its firstname, lastname
get_response = requests.get(URL+str(BOOKING))
get_firstname = get_response.json()['firstname']
get_lastname = get_response.json()['lastname']


def test_partial_update_booking():
    """
    Checks whether partial update properly updates booking data
    """
    patch_data = json.dumps({
        "firstname": "{}".format(UPDATE),
        "lastname": "{}".format(UPDATE)
    })
    patch_data_json = json.loads(patch_data)
    patch_response = requests.patch(URL+str(BOOKING), data=patch_data, headers=HttpManager.headers)
    patch_firstname = patch_response.json()['firstname']
    patch_lastname = patch_response.json()['lastname']
    # Tests
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(patch_firstname).is_not_equal_to(get_firstname)
    assert_that(patch_lastname).is_not_equal_to(get_lastname)
    assert_that(patch_firstname).is_equal_to(patch_data_json['firstname'])
    assert_that(patch_lastname).is_equal_to(patch_data_json['lastname'])
    # Cleans up
    cleaning_data = json.dumps({
        "firstname": "{}".format(get_firstname),
        "lastname": "{}".format(get_lastname)
    })
    requests.patch(URL+str(BOOKING), data=cleaning_data, headers=HttpManager.headers)
