class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted."""

        print("Please insert coins")

        large_dollar = input("How many large dollars?: ")
        half_dollar = input("How many half dollars?: ")
        quarters = input("How many quarters?: ")
        dimes = input("How many dimes?: ")
        nickels = input("How many nickels?: ")

        # total monetary value
        coins = float(large_dollar) + (float(half_dollar) * 0.50) + (float(quarters) * 0.25) + (float(dimes) * 0.10) + (float(nickels) * 0.05)

        return coins

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient."""
        if coins < cost:
            return False
        else:
            return True