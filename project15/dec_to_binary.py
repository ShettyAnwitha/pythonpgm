print("enter the decimal number to convert it to binary: ")
dec_no = int(input())
i = 0
bin_no = []
while dec_no!=0:
    rem = dec_no%2
    bin_no.insert(i, rem)
    i = i+1
    dec_no = int(dec_no/2)

i = i-1
print("\n binary value for equivalent decimal no:")
while i>=0:
    print(end=str(bin_no[i]))
    i = i-1
print()
