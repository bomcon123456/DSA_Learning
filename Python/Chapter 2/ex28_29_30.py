from credit_card import CreditCard


class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit card instance.

    The initial balance is zero.

    customer  the name of the customer (e.g., 'John Bowman')
    bank      the name of the bank (e.g., 'California Savings')
    acnt      the acount identifier (e.g., '5391 0375 9387 5309')
    limit     credit limit (measured in dollars)
    apr       annual percentage rate (e.g., 0.0825 for 8.25% APR)
    """
        super().__init__(customer, bank, acnt, limit)  # call super constructor
        self._apr = apr
        self._charge_per_month = 0
        self._payment_per_month = 0
        self._mmp = 0

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

    Return True if charge was processed.
    Return False and assess $5 fee if charge is denied.
    """
        success = super().charge(price)  # call inherited method
        self._charge_per_month += 1
        if not success:
            self.set_balance(self.get_balance() + 5)  # assess penalty
        if self._charge_per_month >= 10:
            self.set_balance(self.get_balance() + 1)
        return success  # caller expects return value

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self.set_balance(self.get_balance() - amount)
        self._payment_per_month += amount

    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        self._mmp = 0.01 * self._balance
        if self._payment_per_month < self._mmp:
            late_fee = 10
            self.set_balance(self.get_balance() - late_fee)
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1 / 12)
            self.set_balance(self.get_balance() * monthly_factor)
        self._charge_per_month = 0
        self._payment_per_month = 0

