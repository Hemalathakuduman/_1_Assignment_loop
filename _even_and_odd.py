start_num = int(input("Enter the first number: "))
end_num = int(input("Enter the end number: "))
count_odd = 0
count_even = 0
for i in range(start_num, end_num+1):
        if i % 2 == 0:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)