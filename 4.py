import string
x=input("Enter a sentence : ")
print(x)
count=0
count1=0
for y in range(len(x)):
    if (x[y].isdigit()):
    	count1+=1
    else:
    	count+=1			        
        

print(count)
print(count1)        
