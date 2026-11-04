
import pytest

from salon_booking import (
    extra_time_charge,
    can_book,
    arrival_status
)


# -------------------------------
# extra_time_charge() tests
# -------------------------------

def test_unknown_service():
    with pytest.raises(ValueError, match="unknown service"):
        extra_time_charge("nails", 30, "junior", False)


def test_negative_duration():
    with pytest.raises(ValueError, match="invalid duration"):
        extra_time_charge("haircut", -5, "junior", False)


def test_member_haircut_included_time():
    assert extra_time_charge("haircut", 40, "junior", True) == 0


def test_spa_member_no_extra_time():
    assert extra_time_charge("spa", 90, "senior", True) == 0


def test_non_member_haircut_extra_time_junior():
    assert extra_time_charge("haircut", 40, "junior", False) == 100


def test_senior_stylist_extra_time():
    assert extra_time_charge("colour", 70, "senior", False) == 180


def test_long_extra_time_junior():
    assert extra_time_charge("haircut", 100, "junior", False) == 1260


def test_long_extra_time_senior():
    assert extra_time_charge("haircut", 100, "senior", False) == 2100


# -------------------------------
# can_book() tests
# -------------------------------

def test_walk_in_allowed():
    assert can_book(2, 5, True) is True


def test_walk_in_not_allowed():
    assert can_book(3, 1, True) is False


def test_party_size_exceeds_limit():
    assert can_book(5, 1, False) is False


def test_booking_with_two_services():
    assert can_book(4, 2, False) is True


def test_booking_with_more_than_two_services():
    assert can_book(3, 3, False) is False


# -------------------------------
# arrival_status() tests
# -------------------------------

def test_colour_weekday_open():
    assert arrival_status(10, True, False) == "open"


def test_colour_weekday_late():
    assert arrival_status(0, True, False) == "late"


def test_colour_weekday_closed():
    assert arrival_status(-6, True, False) == "closed"


def test_non_colour_weekday_open():
    assert arrival_status(5, False, False) == "open"


def test_non_colour_weekday_late():
    assert arrival_status(-5, False, False) == "late"


def test_weekend_colour_open():
    assert arrival_status(20, True, True) == "open"


def test_weekend_non_colour_late():
    assert arrival_status(0, False, True) == "late"


def test_weekend_non_colour_closed():
    assert arrival_status(-11, False, True) == "closed"
