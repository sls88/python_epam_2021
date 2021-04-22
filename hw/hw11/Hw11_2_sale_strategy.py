"""Homework 11.2."""
from typing import Callable


class Order:
    """Return the cost of the product, depending on the transferred discount strategy.

        If several discount strategies are transferred, return the cost of the goods
            with the maximum discount
        If discount strategies are not transferred, return the full cost of the goods
    Args:
        price: cost of goods
        discount_strategy: discount_strategy

    Returns:
        The return value. Cost of goods with discount
    """

    def __init__(self, price: int, *discount_strategy: Callable):
        self.price = price
        self.discount_strategy = tuple(discount_strategy)
        self.sale = 0

    def _check_sale(self) -> float:
        """Check the amount of the discount (no more than free).

        Returns:
            The return value. Positive price
        """
        return self.price if self.sale > self.price else self.sale

    def _calculate_discount(self) -> float:
        """Select the maximum discount and check total price.

        Returns:
            The return value. Maximum deductible item value
        """
        if self.discount_strategy:
            self.sale = max(strat(self) for strat in self.discount_strategy)
        return self._check_sale()

    def final_price(self) -> float:
        """Return final price.

        Returns:
            The return value. Final price with maximum discount
        """
        return self.price - self._calculate_discount()
