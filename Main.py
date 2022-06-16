from inventory import Inventory
from basketcheckout import BasketCheckOut
from time import gmtime, strftime

basket = []

def scan_item():
    bar_code = input("\nPlease enter the barcode of the item: ")
    inv = Inventory(bar_code)
    item_avail = inv.check_sku_availability()
    if(item_avail == False):
        print("This item does not exist in our inventory.\n")
        scan_next_item()
    else:        
        basket.append(item_avail)
        scan_next_item()
       
def scan_next_item():
    scan_sku = input("Would you wish to scan next item(Y) or remove item(R) or Exit(E)? (Y/R/E)")
    if(scan_sku == 'Y' or scan_sku == 'y'):
        scan_item()
    elif(scan_sku == 'R' or scan_sku == 'r'):
        remove_item()

def remove_item():
    bar_code = input("\nPlease enter the barcode of item you wish to remove: ")  
    
    on_basket = False
    for index, item in enumerate(basket):                               
        if bar_code == item['bar_code']:                
            item_on_basket = item
            on_basket = True
                                
    if on_basket == True:
        basket.remove(item_on_basket)
        scan_next_item()
    else:
        print("This item does not exist in your basket.\n")
        scan_next_item()

def main():
    current_date_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    scan_item()
    bo = BasketCheckOut(current_date_time,basket)
    bo.compute_amount_due()
    print("\nThank you for shopping, See you next time !")

    next = input("Next customer(N) or Quit(Q)?(N/Q)")
    if(next == "n" or next == "N"):
        basket[:] = []
        main()     
    else:
        exit()

main()
