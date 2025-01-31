L=[4,5,1,2,9,7,10,8]
print("Original List:",L)
count =0

for i in L:
    count =count+i
avg = count/len(L)
print("sum =", count)
print("average =", avg)