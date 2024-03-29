# A function that gets the user's input of money and validates it
import inventory as inv
def get_money():
  try:
    money = float(input("Please enter the amount of money you have: $"))
    if money <= 0:
      print("Money must be greater than 0.")
      return get_money()
    else:
      return money
  except Exception as e:
    print("Error")
    return get_money()

# A function that displays the list of items and gets the user's choice of item
def get_choice(inventory):
  user_selection = input("Please enter your choice: ")
  if user_selection in inv.inventory_dict.keys():
    return user_selection
  else:
    print("Invalid selection")
    return get_choice(inventory)