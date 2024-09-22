no = int(input("Enter Initial Number: "))
iteration = int(input("Enter No. of Iterations: "))
commondiff = int(input("Enter Common Difference: "))

sum_equals = 0  
product_equals = 1

sequence = ""
for i in range(iteration):
    term = no + i * commondiff
    sum_equals += term
    product_equals *= term

    sequence += f"{term} + "
    if i < iteration - 1:
        sequence += f"{term} +"
    else :
        sequence += f"{term} +"

print(f"\nSum: {sequence} = {sum_equals}")
print(f"\nProduct: {sequence} = {product_equals:,}")
