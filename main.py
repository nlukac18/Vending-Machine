# Import the inventory and user_io modules
import inventory as inv
import user_io as io
def main():
  print("These are your choices:", inv.inventory_dict)
  money = io.get_money()
  user_selection = io.get_choice(inv.inventory_dict)
  item_price = float(inv.inventory_dict[user_selection][0])
  if item_price > money:
    print("Error, insufficient funds")
  elif item_price == money:
    print(f'Here is your {user_selection} no change is required')
  else:
    change = money - item_price
    print(f'Here is your {user_selection} and your change ${change}')
    result = input("Would you like anything else: Yes/No ")
  if result == "Yes":
    main()
  else:
    print("Thank you for coming to the vending machine!")  
main()

