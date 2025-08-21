from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''
@pytest.mark.parametrize("status", [("available","sold","pending")])
def test_patch_order_by_id(status):

    for status in status:
        test_endpoint = "/store/order/1"
        patch_data = {
            "pet_id": 1,
            'status': status}  

        response = api_helpers.patch_api_data(test_endpoint, patch_data)
        print (response.json()) 
        assert response.status_code == 200      
        assert_that(response.json()['message'], contains_string("Order and pet status updated successfully"))
        assert_that(response.json()['pet_id'], is_(1))
        assert_that(response.json()['status'], is_(status))

# Order endopoint not implemented so this test will fail