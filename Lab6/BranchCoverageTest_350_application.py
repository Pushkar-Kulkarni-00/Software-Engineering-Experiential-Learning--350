
import pytest

from salon_booking import (
    extra_time_charge,
    can_book,
    arrival_status
)


# =====================================
# extra_time_charge() branch tests
# =====================================

def test_unknown_service_branch():
    with pytest.raises(ValueError):
        extra_time_charge("unknown", 30, "junior", False)


def test_negative_duration_branch():
    with pytest.raises(ValueError):
        extra_time_charge("spa", -1, "senior", False)


def test_member_non_spa_branch():
    assert extra_time_charge("colour", 70, "junior", True) == 0


def test_member_spa_branch():
    assert extra_time_charge("spa", 90, "senior", True) == 0


def test_extra_time_zero_branch():
    assert extra_time_charge("haircut", 30, "junior", False) == 0


def test_extra_time_positive_junior_branch():
    assert extra_time_charge("haircut", 40, "junior", False) == 100


def test_extra_time_positive_non_junior_branch():
    assert extra_time_charge("colour", 70, "senior", False) == 180


def test_extra_time_above_60_junior_branch():
    assert extra_time_charge("haircut", 91, "junior", False) == 1098


def test_extra_time_above_60_senior_branch():
    assert extra_time_charge("haircut", 91, "senior", False) == 1830


# =====================================
# can_book() branch tests
# =====================================

def test_walkin_party_size_two():
    assert can_book(2, 3, True) is True


def test_walkin_party_size_above_two():
    assert can_book(3, 1, True) is False


def test_regular_booking_party_above_four():
    assert can_book(5, 1, False) is False


def test_regular_booking_two_services():
    assert can_book(4, 2, False) is True


def test_regular_booking_more_than_two_services():
    assert can_book(4, 3, False) is False


# =====================================
# arrival_status() branch tests
# =====================================

def test_colour_cutoff_open():
    assert arrival_status(10, True, False) == "open"


def test_colour_cutoff_late():
    assert arrival_status(9, True, False) == "late"


def test_colour_cutoff_closed():
    assert arrival_status(-6, True, False) == "closed"


def test_non_colour_cutoff_open():
    assert arrival_status(5, False, False) == "open"


def test_non_colour_cutoff_late():
    assert arrival_status(4, False, False) == "late"


def test_weekend_colour_open():
    assert arrival_status(20, True, True) == "open"


def test_weekend_colour_late():
    assert arrival_status(5, True, True) == "late"


def test_weekend_non_colour_closed():
    assert arrival_status(-11, False, True) == "closed"
