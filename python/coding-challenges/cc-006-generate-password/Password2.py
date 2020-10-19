name = input ("Please enter your full name without any space :")
name_list = list(name.lower())

import random

pass1 = random.choices(name_list, k=3)

pass2 = random.randint(1000,9999)

print("".join(pass1)+str(pass2))



