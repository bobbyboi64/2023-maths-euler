#it gets the answer 
count =0
for i in range(3,1000):
    x = (360*(i-2))/i
    
    if x//0.5 == x/0.5:
        count+=1
        print(i,x)
print(count)