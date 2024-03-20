# Import the inventory and user_io modules
import inventory as inv
import user_io as io
def main():
  result = "Yes"
  money = io.get_money()
  while result == "Yes":  
    print("These are your choices:", inv.inventory_dict)
    user_selection = io.get_choice(inv.inventory_dict)
    if inv.inventory_dict[user_selection][1] == 0:
       print("Item is no longer availible, please choose again")
       print("These are your choices:", inv.inventory_dict)
       user_selection = io.get_choice(inv.inventory_dict)
    else:
        item_price = float(inv.inventory_dict[user_selection][0])
        if item_price > money:
            print("Error, insufficient funds")
        elif item_price == money:
            print(f'Here is your {user_selection} no change is required')
            money = money - item_price
            result = input("Would you like anything else: Yes/No ")
            inv.inventory_dict[user_selection][1] = inv.inventory_dict[user_selection][1] - 1
        else:
            change = money - item_price
            print(f'Here is your {user_selection} and your change ${change}')
            money = money - item_price
            inv.inventory_dict[user_selection][1] = inv.inventory_dict[user_selection][1] - 1
            result = input("Would you like anything else: Yes/No ") 
main()