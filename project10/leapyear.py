# if year divide by 4 its leap year
# if year divide by 4 but not by 100
# if year divide by 100 but not 400
start=2000
end=2400

for i in range(start,end,1):
    if((i%4==0) or (i%100!=0) and (i%4==0)):
      print(i," is leapyear")
