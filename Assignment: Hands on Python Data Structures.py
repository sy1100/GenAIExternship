# Task 1
fruit_list = ['strawberry', 'pineapple', 'mango', 'grape','watermelon']
print("Original list: " + str(fruit_list))

fruit_list.append('peach')
print("After adding a fruit: " + str(fruit_list))

fruit_list.remove('pineapple')
print("After removing a fruit: " + str(fruit_list))

print("Reversed list: " + str(fruit_list [::-1])+ "\n")

# Task 2
my_information = {"name":"Snoopy", "age":25 , "city":"Dallas"}
my_information["favorite color"] = "Blue"
my_information["city"] = "Boston"

key_result = ""
for key,value in my_information.items():
    key_text = str(key) + ", "
    key_result += key_text
key_result = key_result[:-2]
print("Keys:", key_result)

value_result = ""
for key,value in my_information.items():
    value_text = str(value) + ", "
    value_result += value_text
value_result = value_result[:-2]
print("Values:", value_result)
