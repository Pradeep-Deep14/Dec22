#print program to print first 20 even numbers

nums=list(range(1,21))
filtered_list=list(filter(lambda x: x%2==0,nums))
print(filtered_list)