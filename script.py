# Your code below:
#challenge 1 
first_names = ["Ainsley", "Ben", "Chani", "Depak"]

#challenge 2
preferred_size = ["Small", "Large", "Medium"]

#challenge 3
preferred_size.append("Medium")
print(preferred_size)

#challenge 4
customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)

#challenge 5
customer_data[-2][-1] = False
print(customer_data)

#challenge 6
customer_data[1].remove(False)
print(customer_data)

#challenge 7
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)
