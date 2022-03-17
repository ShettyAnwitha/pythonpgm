import random
numbers = '1234567890'
print("Enter 1 if you want to create 4 digit OTP")
print("Enter 2 if you want to create 6 digit OTP")

digits = int(input("Enter 1 or 2: "))
if digits == 1:
    ot = random.choices(numbers, k = 4)
    otp=''.join(ot)
    print(otp)
elif digits == 2:
    ot = random.choices(numbers, k = 6)
    otp=''.join(ot)
    print(otp)
    
else:
    print("invalid choice")
