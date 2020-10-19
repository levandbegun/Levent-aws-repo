name = str(input ("Please enter your full name without any space :"))
name_list = list(name.lower())

import random

#sampling with replacement

pass1 = random.choices(name_list, k=3)

def nameString(pass1):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in pass1:  
        str1 += ele   
    
    # return string   
    return str1  
  
       
# Driver code     
#print(nameString(pass1))  

pass2 = random.randint(1000,9999)
#print(pass2)

('G','F','E')   G***F***E
print(nameString(pass1)+str(pass2)) 
print("".join(pass1)+str(pass2))



