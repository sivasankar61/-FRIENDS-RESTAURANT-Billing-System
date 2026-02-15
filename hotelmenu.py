# Define the menu
restaurant_menu = {

    "Starters": {
        "Tomato Soup": 120,
        "Veg Manchurian": 180,
        "Chicken Lollipop": 220,
        "French Fries": 100
    },
    
    "Main Course": {
        "Paneer Butter Masala": 250,
        "Butter Naan": 40,
        "Veg Biryani": 200,
        "Chicken Biryani": 280,
        "Dal Tadka": 180
    },
    
    "Fast Food": {
        "Veg Burger": 120,
        "Chicken Burger": 150,
        "Pizza Margherita": 250,
        "Cold Coffee": 90
    },
    
    "Desserts": {
        "Gulab Jamun": 80,
        "Ice Cream": 100,
        "Chocolate Brownie": 150
    },
    
    "Beverages": {
        "Tea": 20,
        "Coffee": 40,
        "Fresh Lime Soda": 60,
        "Mineral Water": 20
    }
}


# Function to display menu
def show_menu():
    print("\n------ MENU ------")
    for category, items in restaurant_menu.items():
        print(f"\n{category}")
        for item, price in items.items():
            print(f"{item} - {price}")


print("Welcome to FRIENDS RESTAURANT 🍽️")

total_bill = 0
ordered_items = []   # To store ordered items

while True:
    show_menu()

    choice = input("\nEnter item name you want to order: ").strip()

    found = False

    for items in restaurant_menu.values():
        if choice in items:
            price = items[choice]
            total_bill += price
            ordered_items.append((choice, price))
            print(f"{choice} added! Price: {price}")
            found = True
            break

    if not found:
        print("Item not found! Please choose from menu.")

    more = input("Do you want to order more? (yes/no): ").lower().strip()
    if more != "yes":
        break


# Show Bill
print("\n\n--------- BILL SUMMARY ---------")
for item, price in ordered_items:
    print(f"{item} - {price}")

print(f"\nSubtotal: {total_bill}")

# Discount Option
discount_percent = float(input("Enter discount percentage (0 if none): "))

discount_amount = (total_bill * discount_percent) / 100
final_bill = total_bill - discount_amount

print(f"Discount Amount: {discount_amount}")
print(f"Final Payable Amount: {final_bill}")

print("\nThank you for visiting! 😊")
