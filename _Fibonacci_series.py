start_num = int(input("Enter the first number: "))
end_num = int(input("Enter the end number: "))
First_val = 0
Second_val = 1
for i in range(start_num, end_num+1):
           if i <= 1:
                      num = i
           else:
                      num = First_val + Second_val
                      First_val = Second_val
                      Second_val = num
           print(num)
