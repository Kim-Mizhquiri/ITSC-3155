import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes

sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    while True:
        user_input = input("What would you like (small/medium/large/off/report): ").lower()

        if user_input == "off":
            break

        elif user_input == "report":
            # Sandwich machine report
            for item, amount in sandwich_maker_instance.machine_resources.items():
                print(item, amount)

            # Cashier report (if your class has one)
            if hasattr(cashier_instance, "report"):
                cashier_instance.report()

        elif user_input in recipes:
            sandwich = recipes[user_input]
            ingredients = sandwich["ingredients"]
            cost = sandwich["cost"]

            # Check resources
            if sandwich_maker_instance.check_resources(ingredients):

                # Process coins → returns total inserted
                total_inserted = cashier_instance.process_coins()

                # Check if transaction succeeds
                if cashier_instance.transaction_result(total_inserted, cost):

                    # Make the sandwich
                    sandwich_maker_instance.make_sandwich(user_input, ingredients)

                    change = total_inserted - cost
                    print(f"Here's ${change:.2f} in change.")
                    print(f"{user_input.title()} sandwich is ready. Bon appetit!")

                else:
                    print("Sorry, that's not enough money. Money refunded.")

            else:
                print("Sorry, not enough resources to make that sandwich.")

        else:
            print("Invalid selection.")
if __name__=="__main__":
    main()
