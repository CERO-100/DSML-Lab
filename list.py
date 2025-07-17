my_list=[]
num_elements=int(input("How many elements do you want to enter?"))
for i in range(num_elements):
    element=input(f"enter Element {i+1}:")
    my_list.append(element)
print("The list is:",my_list)