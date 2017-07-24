import csv

products = [] #1. create empty list called product

csv_file_path = "data/products.csv"

# READ PRODUCTS CSV

#we will loop through each product
with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file) #3. using csv.DictReader function, each row will be dictionary like
    for row in reader: #2. when reading the file, iterating through each "row"
    #each row corresponds to a product
        products.append(row) #4 append each "row" to "products"

menu = """
    Hi.

    Welcome to the products app.

    There are {0} products.

    Please choose an operation:

       Operation | Description
   --------- |-------------
   'List'    | Display a list of product identifiers and names.
   'Show'    | Show inofrmation about a product.
   'Create'  | Add a new product.
   'Update'  | Edit an existing product.
   'Destroy' | Delete an existing product.

""".format(len(products)) #this is a string format.  "len(product)" give the number of items in "products"
#this is similar to what learned in the "meetup"
#this is "STRING INTERPULATION"
chosen_operation = input(menu)
#input is the same function as last project but wrote out the text instead of "menu"
chosen_operation = chosen_operation.title()
# .title() allows for accepting lower case.

#to access the list --> looping through each product and print the name
#for product in products:
#    print(product["id"],product["name"])

def list_products():
    print("THERE ARE " + str(len(products)) + " PRODUCT(S):")
    for p in products:
        print("+ ID:" + p["id"] + "; NAME:" +p["name"]+ "; AISLE:" +p["aisle"]+ "; DEPT:" + p["department"]+ "; PRICE:" + p["price"])
        #print(list(products.items())

def show_product():

    id_entry = input("Please specify the product's identifier:")

    def lookup_id(id_entry):
        matching = [id_prod for id_prod in products if id_prod["id"] == id_entry]
        return (matching[0])

    product = lookup_id(id_entry)  #invoking special function created.  product is a dictionary
    product_show = list(product.items())
    print("SHOWING A PRODUCT HERE!")
    print(product_show)
#STILL NEED AN IF ERROR STATEMENT

def create_product():
    print("CREATING A PRODUCT")
    product_name = input("name is:") #Invoking inputs
    product_aisle = input("aisle is:")
    product_department = input("department is:")
    product_price = input("price is:")
    new_product = {
        "id": len(products) + 1,
        "name": product_name,
        "aisle": product_aisle,
        "department": product_department,
        "price": product_price
    }
    print("NEW PRODUCT IS", new_product)
    products.append(new_product)

def update_product():

    id_entry = input("Please specify the product's identifier:")
    chg_item = next((item for item in products if item['id'] == id_entry), None)
    index_num = products.index(chg_item)

    show_name = products[index_num]["name"]
    new_name = input("Change name from {} to:".format(show_name))
    products[index_num]["name"] = new_name

    show_aisle = products[index_num]["aisle"]
    new_aisle = input("Change aisle from {} to:".format(show_aisle))
    products[index_num]["aisle"] = new_aisle

    show_dept = products[index_num]["department"]
    new_dept = input("Change department from {} to:".format(show_dept))
    products[index_num]["department"] = new_dept

    show_price = products[index_num]["price"]
    new_price = input("Change price from {} to:".format(show_price))
    products[index_num]["price"] = new_price

def destroy_product():
    id_entry = input("Please specify the product's identifier:")
    #TRY 4
    del_item = next((item for item in products if item['id'] == id_entry), None)
    index_num = products.index(del_item)
    products.pop(index_num)

#CHANGE ID
    # id_entry = input("Please specify the product's identifier:")
    # chg_item = next((item for item in products if item['id'] == id_entry), None)
    # index_num = products.index(chg_item)

    # for val in products:
    #     products["id"] = products.index(val) + 1

#try 1:
    # if products["id"] == id_entry
    #     print(id_entry)

#try 2:
    # for k, v in products.items():
    #      if v == id_entry:
    #         del products[k]

#try 3:
    # def lookup_id(id_entry):
    #     matching = [id_prod for id_prod in products if id_prod["id"] == id_entry]
    #     return (matching[0])
    #
    # product = lookup_id(id_entry)  #invoking special function created.  product is a dictionary
    # print("SHOWING A PRODUCT HERE!")
    # print(product)

#TRY 5
    # id_entry_num = int(id_entry)
    # print(products["id"].index(id_entry_num))






if chosen_operation == "List": list_products()
elif chosen_operation == "Show": show_product()
elif chosen_operation == "Create": create_product()
elif chosen_operation == "Update": update_product()
elif chosen_operation == "Destroy": destroy_product()
else: print("OOPS. PLEASE CHOOSE ONE OF THE RECOGNIZED OPERATIONS.")

#list, show, destroy all require to find product identifier-->APPROACH IS TO USE LIST FILTERING


#(WANT TO EXECUTE LAST)
# OVERWRITING INVENTORY CSV FILE
#assumes CSV file headers are the same
#if got error msg "'list' object has no attribute keys OR 'str' object has no attribute keys"-->WE ARE MISSING A KEY WHICH ONLY IN DICTIONARY
#other_path = "data/other_products.csv" # THIS WAS TO TEST IF WRITING NEW FILE WORKED
with open(csv_file_path, "w") as csv_file:  #csv_file_path = "data/products.csv"
    writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
    writer.writeheader() # uses fieldnames set above
    for product in products: #to loop through each statement
        writer.writerow(product)
