import pytest
from checkout import Checkout


# def test_can_instantiate_checkout():
#     co = Checkout()
# the above test is no longer needed, covered by next test.

@pytest.fixture()
def checkout():

    checkout = Checkout()
    checkout.add_item_price('a', 1)
    checkout.add_item_price('b', 2)
    return checkout


# def test_can_add_item_price(checkout):
#
#     checkout.add_item_price('a', 1)
#
#
# def test_add_item(checkout):
#
#     checkout.add_item('a')

# the above tests are  no longer needed, covered by next test.


def test_calculate_total(checkout):
    # checkout.add_item_price('a', 1) # repetitive - added to test fixture
    checkout.add_item('a')  # add item to checkout
    assert checkout.calculate_total() == 1


def test_correct_total_with_multi_items(checkout):

    checkout.add_item('a')
    checkout.add_item('b')
    assert checkout.calculate_total() == 3


def test_add_discount_rule(checkout):

    checkout.add_discount('a', 3, 2)


# @pytest.mark.skip
def test_apply_discount_rule(checkout):

    checkout.add_discount('a', 3, 2)
    checkout.add_item('a')
    checkout.add_item('a')
    checkout.add_item('a')
    assert checkout.calculate_total() == 2


def test_exception_with_no_price(checkout):

    with pytest.raises(Exception):
        checkout.add_item('c')
