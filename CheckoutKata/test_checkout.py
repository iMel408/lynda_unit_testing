import pytest
from checkout import Checkout

# def test_can_instantiate_checkout():
#     co = Checkout()
# this test is no longer needed as check is covered by next test.

@pytest.fixture()
def checkout():
    checkout = Checkout()
    return checkout


def test_can_add_item_price(checkout):

    checkout.add_item_price('a', 1)


def test_add_item(checkout):

    checkout.add_item('a')

