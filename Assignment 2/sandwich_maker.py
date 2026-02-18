
class SandwichMaker:

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

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources."""
        # iterate through each resource
        for i in order_ingredients:
            # deduct it from the available resources
            self.machine_resources[i] -= order_ingredients[i]
