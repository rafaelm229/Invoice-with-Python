# Create a list of products
product1_name,product1_price = "Computer", 500 
product2_name, product2_price = "Video Card", 250
product3_name, product3_price = "Monitor", 100

# Company name and information
company_name = "Mr.Robot, inc"
company_adress = "12 fifth avenue "
company_city = "New York"

# Ending message
message = "thanks for shopping with us today!"


#top border
print("*" * 50)


# Company information format
print("\t\t{}".format(company_name.title()))
print("\t\t{}".format(company_adress.title()))
print("\t\t{}".format(company_city.title()))

#line between sections

print("=" * 50)


# Header for section of items
print("\tProduct name\tProduct Price")


# print for each item
print("\t{}\t\t${}".format(product1_name.title(), product1_price))
print("\t{}\t${}".format(product2_name.title(), product2_price))
print("\t{}\t\t${}".format(product3_name.title(), product3_price))

# print a line between sections
print("=" * 50)

# print out header for section of total
print("\t\t\tTotal")

# calculate total price and print out
total = product1_price + product2_price + product3_price
print("\t\t\t${}".format(total))

# print a line between sections
print("=" * 50)

# output thank you 
print("\n\t{}\n".format(message))

# create a bottom border
print("*" * 50)