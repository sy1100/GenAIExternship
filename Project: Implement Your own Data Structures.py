# Step 1
print("Welcome to the Inventory Manager!\n")
inventory = {"apple": (10,2.5), "banana": (20,1.2)}
print("Current inventory:")

for key, value in inventory.items():
    print("Item:", key, ",", "Quantity:", value[0], ",", "Price:", "$", value[1])

# Step 2
# add
inventory["mango"] =(15,3.0)

# newly added item in inventory
inventory_copy = inventory.copy()
last_item = ''.join(filter(str.isalpha,str(inventory_copy.popitem())))
print("\nAdding a new item: ", last_item)

# delete
del inventory["banana"]
# update
inventory["apple"] =(12,2.8)

# Step 3
print("\nUpdated inventory: ")
for key,value in inventory.items():
    print("Item:", key, ",", "Quantity:", value[0], ",","Price:", "$",value[1])


# Step 4
final_val = 0
for value in inventory.values():
    semi_val = (value[0] * value[1])
    final_val += semi_val
print("Total value of inventory:","$",final_val)


