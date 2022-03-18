l1 = [1,2,3,4,5,6,7,8]

print({l1[i]:l1[i+1] for i in range(0,len(l1),2)})

l2=['a','b','c','d','e','f','g','h','i','j','k','l']
print({i:j for i,j in enumerate(l2,1)})
