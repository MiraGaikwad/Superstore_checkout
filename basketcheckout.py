from collections import Counter
import numpy as np

class BasketCheckOut():
    def __init__(self,checkout_date,checkout_items):
        self.checkout_date = checkout_date
        self.checkout_items = checkout_items

    # Function to calculate quantity of each item in cart
    def cal_item_quantity(self):       
        cart_items_count=[]
        for en, item in enumerate(self.checkout_items):
            cart_items_count.append(item['bar_code'])
        self.item_qty=Counter(cart_items_count)
        self.unique_item_list = list(np.unique(cart_items_count))

    # Function to calculate the due amount for all items in cart
    def compute_amount_due(self):
        self.cal_item_quantity()
        self.cart_total = 0
        payable_amount = 0

        # Iterate through list of unique items 
        for item in self.unique_item_list:
            # Iterate through items in main cart
            for en, self.product in enumerate(self.checkout_items):
                if item == self.product['bar_code']:
                    for i in self.item_qty:
                        if i == self.product['bar_code']:
                        # Fetch quantity of items
                            self.count = 0
                            self.count = self.item_qty[self.product['bar_code']]

                            #Check if item quantity is applicable for promotional offer
                            if self.product['promo_offer1'] != 'None' and self.count >= self.product['quantity1']:
                                payable_amount = self.cal_promo1()

                            elif self.product['promo_offer2'] != 'None' and self.count >= self.product['quantity2']:
                                payable_amount = self.cal_promo2()
                            else:
                                payable_amount = self.count*self.product['price']

                            self.cart_total += payable_amount
                            self.amount_due = self.cart_total
                        # break
                    break
        change = self.payment_due()

    # Function to calculate amount on promotional offer1
    def cal_promo1(self):
        qty = self.count
        f_qty = True
        rem_amount = 0
        amount = 0
        while f_qty == True:
            if qty >= self.product['quantity1']:
                rem_qty = qty - self.product['quantity1']
                qty = rem_qty
                amount = amount + self.product['promo_price1']
                f_qty = True
            else:
                rem_amount = qty*self.product['price']
                f_qty = False

        payable_amount = amount + rem_amount
        return payable_amount

    # Function to calculate amount on promotional offer1    
    def cal_promo2(self):
        qty = self.count
        f_qty = True
        rem_amount = 0
        amount = 0
        while f_qty == True:
            if qty >= self.product['quantity2']:
                rem_qty = qty - self.product['quantity2']
                qty = rem_qty
                amount = amount + self.product['promo_price2']
                f_qty = True
            else:
                rem_amount = qty*self.product['price']
                f_qty = False

        payable_amount = amount + rem_amount
        return payable_amount

    def payment_due(self):
        amount_to_pay = self.cart_total
        print("\nAmount due: £"+str(amount_to_pay))
        change = self.payment_paid(amount_to_pay)
        self.generate_receipt()
        return change
        
    # Function to accept the payment from used and calculate the change    
    def payment_paid(self, amount_to_pay):
        amt_paid = float(0.0)
        total_paid = float(0.0)
        due_amt = float(0.0)
        total = amount_to_pay
        due = True
        
        while due == True:
            try:
                amt_paid = float(input("\nPlease enter amount to pay: "))
                if(amt_paid < 0.0):
                    print("We don't accept negative money..!\n")
                    continue
                else:
                    total_paid += amt_paid
                    self.total_paid = total_paid
                    if(amt_paid < total):
                        due_amt = total - amt_paid
                        total = due_amt
                        print("Payment due: £"+str(due_amt))
                        due = True
                        continue   
                    else:
                        change = amt_paid - total
                        self.change = change
                        return change
                    break
                break
                    
            except ValueError:
                print('Please enter a valid floating point value.')

        return change

    # Function to generate the receipt           
    def generate_receipt(self):

        print("\n----- Your Receipt -----\n")
        print("Date :", self.checkout_date)
        print("\nItem Name| Qty | Unit Price | Tot Price | Payable amount")
        print("-------------------------------------------------------------")

        for item in self.unique_item_list:
            for en, self.product in enumerate(self.checkout_items):
                if item == self.product['bar_code']:
                    for i in self.item_qty:
                        if i == self.product['bar_code']:
                            self.count = 0
                            self.amount = 0
                            self.count = self.item_qty[self.product['bar_code']]
                            total_amount = self.count*self.product['price']
                            if self.product['promo_offer1'] != 'None' and self.count >= self.product['quantity1']:
                                payable_amount = self.cal_promo1()
                                promo_amount = self.count*self.product['price'] - payable_amount
                                print(self.product['name'], "\t *", self.count, "\t", self.product['price'], "\t\t ", total_amount)
                                print("\t\t Promo Offer", "\t-", promo_amount, "\t\t", payable_amount)
                                
                            elif self.product['promo_offer2'] != 'None' and self.count >= self.product['quantity2']:
                                payable_amount = self.cal_promo2()
                                promo_amount = self.count*self.product['price'] - payable_amount
                                print(self.product['name'], "\t *", self.count, "\t", self.product['price'], "\t\t ", total_amount)
                                print("\t\t Promo Offer", "\t-", promo_amount, "\t\t", payable_amount)
                            else:
                                payable_amount = total_amount
                                print(self.product['name'], "\t *", self.count, "\t", self.product['price'], "\t\t ", total_amount, "\t\t", payable_amount)
                    break
                            
                              

        print("\n")
        print("Total amount due: ",'     £'+str(self.amount_due))
        print("Amount Received: ",'       £'+str(self.total_paid))
        print("Change Given: ",'          £'+str(self.change),'\n')