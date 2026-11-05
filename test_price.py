import pytest
from price import final_price


@pytest.mark.parametrize("price, expected", [
    (100, 118.0),     # normal price
    (0, 0.0),         # zero price
    (0.01, 0.01),     # boundary - smallest price
    (1000000, 1180000.0),  # boundary - large price
])
def test_final_price(price, expected):
    assert final_price(price) == expected


@pytest.mark.parametrize("bad", [-1, "abc", None])
def test_invalid_input(bad):
    with pytest.raises(ValueError):
        final_price(bad)
