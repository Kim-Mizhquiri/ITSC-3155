### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input."""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        # iterates through each ingredient
        for i in ingredients:
            # if the ingredient needed is greater than what is available, break the loop and return what specific item is insufficient
            if ingredients[i] > self.machine_resources[i]:
                print("sorry, there is not enough", i)
                return False
        # if there is enough resources, return true
        return True

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

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources."""

        # iterate through each resource
        for i in order_ingredients:
            # deduct it from the available resources
            self.machine_resources[i] -= order_ingredients[i]

### Make an instance of SandwichMachine class and write the rest of the codes ###


machine = SandwichMachine(resources)


# continue the loop until a condition is met, in which case break it
# the only time it brakes is if the user turns it off
while True:

    user_input = input("What would you like (small/medium/large/off/report): ")

    if user_input.lower() == "off":
        break

    elif user_input == "report":

        # prints each individual item and the amounts
        for item, amount in machine.machine_resources.items():
            print(item, amount)

    # if the user input is a key in the recipes dictionary
    elif user_input.lower() in recipes:

        # looks at the specific type of sandwich to be made
        sandwich = recipes[user_input.lower()]
        #gets the ingredients needed
        ingredients = sandwich["ingredients"]
        #gets the cost of that sandwich
        cost = sandwich["cost"]

        if machine.check_resources(ingredients) == True:

            # assigns the total monetary value of coins and passes it through transaction result to get the result of the transaction
            payment = machine.transaction_result(machine.process_coins(), cost)

            # if the payment goes through, go ahead and make the sandwich
            if payment == True:
                print("Here's $", cost - payment, " in change.")
                machine.make_sandwich(user_input.lower(), ingredients)
                print(user_input.title(), " sandwich is ready. Bon appetit!")

            # if not, start the loop all over again
            else:
                print("Sorry, that's not enough money. Money refunded.")

    # in case anything else is typed in, print invalid and restart the loop
    else:
        print("Invalid selection")

