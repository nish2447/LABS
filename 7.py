import string 
import random
n=8  
res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits,k= n)) 

print("The generated random string : " + str(res)) 