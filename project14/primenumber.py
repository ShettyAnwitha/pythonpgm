
p=int(input('Enter the number to check whether it is prime or not:'))
for i in range(2,p):
    if p%i !=0:
        continue
    else:
        print("Its not a prime number")
        break 
else:
    print("Its a prime number")
        
