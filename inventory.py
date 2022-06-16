import csv

class Inventory():        
    def __init__(self,bar_code,name='None',price=0,promo_offer1='None', quantity1=0, promo_price1=0, promo_offer2='None', quantity2=0, promo_price2=0):
        self.bar_code = bar_code
        self.name = name
        self.price = price
        self.promo_offer1 = promo_offer1
        self.quantity1 = quantity1
        self.promo_price1 = promo_price1
        self.promo_offer2 = promo_offer2
        self.quantity2 = quantity2
        self.promo_price2 = promo_price2

    def load_inventory(self):
        # For the Future work this inventory can be stored and loaded by connecting to oracle database instead of loaeding from csv file.
        # Currently I have used csv file instead of static data as it adds flexibility to add items in csv file anytime.
        # Currently 2 promotional offers are taken but this can be further changed to add more promotional offers.
        with open("Inventory.csv", "r") as f:
            reader = csv.DictReader(f)
            self.inventory_items = list(reader)

    def check_sku_availability(self):
        #Load inventory everytime
        self.load_inventory()

        available = False       
        for index, item in enumerate(self.inventory_items):                        
            if self.bar_code == item['bar_code']:              
                sku_avail = {'bar_code': item['bar_code'],'name': item['name'],'price': int(item['price']), \
                'promo_offer1': item['promo_offer1'], 'quantity1': int(item['quantity1']), 'promo_price1':int(item['promo_price1']), \
                'promo_offer2': item['promo_offer2'], 'quantity2': int(item['quantity2']), 'promo_price2':int(item['promo_price2'])}
                available = True
                print(item['name']," -  £", item['price'],'\n' )
                                
        if available == True :            
            return sku_avail
        else:
            return False
