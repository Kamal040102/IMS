import json
import time
import math

fd = open("Inventory.json",'r')
txt = fd.read()
fd.close()
inventory = json.loads(txt)

fd = open("Sales.json",'r')
txt = fd.read()
fd.close()
sales = json.loads(txt)

def addNewProduct():
    print("******This portal is for adding a new product into Inventory******\n")
    prod_id = 110001 + len(inventory)
    prod_name = input("Enter the product name:\t")
    prod_price = int(input("Enter the product price:\t"))
    prod_stock = int(input("Enter the quantity of the product to add:\t"))
    prod_category = input("Enter the category of the product:\t")
    prod_rating = float(input("Enter the product rating:\t"))
    prod_bstbfr = int(input("How much does the product last?\t"))
    prod_pkg = input("When was the product packed?\t")


    inventory[prod_id] = {"name":prod_name, "price":prod_price, "stock":prod_stock, "category":prod_category, "rating":prod_rating, "best-before":prod_bstbfr,"pkg":prod_pkg}

    print("******************************************************************")
    print("The product {} has been added to inventory, Product Id is {}.".format(prod_name, prod_id))

    inventory_json = json.dumps(inventory)

    fd = open("Inventory.json",'w')
    fd.write(inventory_json)
    fd.close()

def updateExistingProduct():
    print("****This portal is for update existing product into Inventory*****\n")
    prod_id = input("Enter the product id\t:")

    for item in inventory:
        if prod_id == item:
            user_Inp = input("What do you want to do with {}:\n\t1.) To change the price\n\t2.) To add more stock\n\t3.) To change Packed Date\n\n\t".format(inventory[item]['name']))
            print("******************************************************************")
            if user_Inp == '1' or user_Inp == 'Price' or user_Inp == 'price':
                print("***************************Change Price***************************")
                new_price = int(input("Enter the new price of {}:\t".format(inventory[item]['name'])))
                inventory[item]['price'] = new_price
                print("******************************************************************")
                print("Price of the product {} has been updated to Rs.{}.".format(inventory[item]['name'], inventory[item]['price']))
            elif user_Inp == '2' or user_Inp == 'Stock' or user_Inp == 'stock':
                print("***************************Update Stock***************************")
                new_stock = int(input("Enter the no of stock want to add of product {}:\t".format(inventory[item]['name'])))
                inventory[item]['stock'] += new_stock 
                print("******************************************************************")
                print("Stock of the product {} has been updated to {} Units.".format(inventory[item]['name'], inventory[item]['stock']))
            elif user_Inp == '3' or user_Inp == 'date' or user_Inp == 'Date':
                print("**************************Update Pkg Date*************************")
                new_pkg = input("Enter the new pkg date of product {}:\t".format(inventory[item]['name']))
                inventory[item]['pkg'] = new_pkg 
                print("******************************************************************")
                print("Pkg Date of the product {} has been updated to {}.".format(inventory[item]['name'], inventory[item]['pkg']))
            else:
                print("Unknown Error Occured")
                break

    inventory_json = json.dumps(inventory)

    fd = open("Inventory.json",'w')
    fd.write(inventory_json)
    fd.close()

def Customer():
    print("*************************Place your Order*************************")
    user_id = input("Enter your user id or e-mail or name:\t")
    prod_id = input("Enter the product id which you want to purchase:\t")
    prod_qty = int(input("Enter the quantity you want to purchase:\t"))

    for item in inventory:
        if prod_id == item:
            print("******************************************************************")
            print("Product Name:\t\t{}".format(inventory[item]['name']))
            print("Product Price:\t\tRs.{}".format(inventory[item]['price']))
            print("We have in stock:\t{} Units".format(inventory[item]['stock']))
            print("Category:\t\t{}".format(inventory[item]['category']))
            print("Rating:\t\t\t{}/5.0".format(inventory[item]['rating']))
            print("Best Before:\t\t{} Days".format(inventory[item]['best-before']))
            print("Packed on:\t\t{}".format(inventory[item]['pkg']))
            print("******************************************************************")
            print("Qty. in your cart:\t{} Units".format(prod_qty))
            total_price = inventory[item]['price'] * prod_qty
            print("Total Amount:\t\tRs.{}".format(total_price))
            if total_price >= 5000:
                discount_amount = total_price * 0.02
                billing_amount = math.floor(total_price - discount_amount)
                print("Discount (@2%):\t\tRs.{}".format(discount_amount))
                print("Billing Amount:\t\tRs.{}".format(billing_amount))
            else:
                discount_amount = 0
                billing_amount = total_price
                print("Billing Amount:\t\tRs.{}".format(billing_amount))
            print("******************************************************************")
            if inventory[item]['stock'] < prod_qty:
                print("We don't have that much quantity of the product {}.".format(inventory[item]['name']))
                break
            else:
                user_validation = input("Press Y to place order or Press C to cancel.\t")
            if user_validation == 'Y' or user_validation == 'y':
                
                tid =str(len(sales) + 536538062050001)

                print("Your order has been placed successfully on {}.\nYour Order ID is {}.\nThank You for shopping with us, {}.".format(time.ctime(),tid,user_id))
                inventory[item]['stock'] = inventory[item]['stock'] - prod_qty

                inventory_json = json.dumps(inventory)

                fd = open("Inventory.json",'w')
                fd.write(inventory_json)
                fd.close()
                
                stock_status = ''
                if inventory[item]['stock'] >= 1000:
                    stock_status = "Good"
                elif inventory[item]['stock'] <= 100:
                    stock_status = "Very Few Left"
                else:
                    stock_status = "Selling Very Fast"

                order_detail = {"Order ID":tid, "Customer Name/Id/E-mail ID":user_id, "Product Id":prod_id, "Product Name":inventory[item]['name'],"Qty. Purchased":prod_qty, "Qty. in Stock":inventory[item]['stock'], "Order Date":time.ctime(),"Order Total Amount":total_price ,"Order Billing Amount": billing_amount, "Discount Offered":discount_amount,"Product Stock Status": stock_status}

                sales[tid] = order_detail

                sales_json = json.dumps(sales)

                fd = open("Sales.json",'w')
                fd.write(sales_json)
                fd.close()

            elif user_validation == 'C' or user_validation == 'c':
                print("User pressed the cancel button.")
                break
            else:
                print("Unknown Error Occured.")
                break
    else:
        print("******************************************************************")
        print("Have a nice Day!!")
        print("******************************************************************")

def Admin():
    userInp = input("What you want to do:\n\t1.) Add new product to the inventory\n\t2.) Update Existing product\n\n\t")
    print("******************************************************************")
    if userInp == '1' or userInp == 'Add' or userInp == 'add':
        addNewProduct()
    elif userInp == '2' or userInp == 'update' or userInp == 'Update':
        updateExistingProduct()
    else:
        print("Unknown Error Occured")
    print("******************************************************************")
    

def checkOrder():
    print("***********************Check Order Details************************\n")
    order_id = input("Enter the order id or Enter your name/id/e-mail id to fetch your orders:\t")

    for item in sales:
        if order_id == item or order_id == sales[item]['Customer Name/Id/E-mail ID']:
            print("******************************************************************")
            print("Order ID is:\t\t{}".format(sales[item]['Order ID']))
            print("Order was placed on:\t{}".format(sales[item]['Order Date']))
            print("Product Name:\t\t{}".format(sales[item]['Product Name']))
            print("Qty. Purchased:\t\t{} Units".format(sales[item]['Qty. Purchased']))
            print("Billing Amount:\t\tRs.{}".format(sales[item]['Order Billing Amount']))
    else:
        print("******************************************************************")
        print("Have a nice Day!!")
        print("******************************************************************")


print("******************************************************************")
userInp = input("Access As:\n\t1.) Customer\n\t2.) Check Order Details\n\t3.) Admin\n\n\t")
print("******************************************************************")
if userInp == 'Customer' or userInp == 'customer' or userInp == '1':
    Customer()
elif userInp == 'Admin' or userInp == 'admin' or userInp == '3':
    Admin()
elif userInp == 'Check' or userInp == 'check' or userInp == '2':
    checkOrder()
else:
    print("Unknown Error Occured")