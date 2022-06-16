# Superstore_checkout

Current Work – 
1.	inventory.py 
a.	This class is to manage the inventory Items 
b.	This inventory will be loaded during each transaction hit for checkout

2.	basketcheckout.py
a.	This class access the user’s cart and calculate total payable amount and prints the receipt.
b.	It can accept the items in any order and calculate total amounts including promotional offer.

3.	main.py
a.	This is main class where above both classes are imported to process the store check Out for users.

4.	Inventory.csv
a.	This file contains the Inventory item which is accessed during each transaction.

Test Result – 
I have tested multiple scenarios and One of the sample test scenarios is as below where Items are entered in any sequences
 
 ![image](https://user-images.githubusercontent.com/84037638/174051098-4c75bf64-86dc-4244-bc02-dc9d40aaa267.png)

![image](https://user-images.githubusercontent.com/84037638/174051128-34c0c9de-907f-4fe5-9124-f0721c6856fb.png)


Receipt for these Items looks as below - 
 
![image](https://user-images.githubusercontent.com/84037638/174051159-9280ceec-b598-49f6-bb0c-6b4b721393cb.png)

Future Work – 
	All the Inventory can be store in oracle database and it can be access in python program instead of reading from csv files.
	Currently added 2 promotional offers to each item but it can be changed to add more promotional offers.

