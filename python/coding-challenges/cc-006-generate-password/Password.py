# import random

# def get_random_string(length):
#     # put your letters in the following string
#     sample_letters = 'abcdefghi'
#     result_str = ''.join((random.choice(sample_letters) for i in range(length)))

#     print("Random string is:", result_str)


# get_random_string(3)

# import random
# import string

# def get_random_alphanumeric_string(letters_count, digits_count):
#     sample_str = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
#     sample_str += ''.join((random.choice(string.digits) for i in range(digits_count)))

#     # Convert string to list and shuffle it to mix letters and digits
#     sample_list = list(sample_str)
#     random.shuffle(sample_list)
#     final_string = ''.join(sample_list)
#     return final_string

# # 5 letters and 3 digits
# print("First random alphanumeric string is:", get_random_alphanumeric_string(3, 4))

# # 6 letters and 2 digits
# print("Second random alphanumeric string is:", get_random_alphanumeric_string(6, 2))


# string = "THIS SHOULD BE LOWERCASE!"
# print(string.lower())

# # string with numbers
# # all alphabets whould be lowercase
# string = "Th!s Sh0uLd B3 L0w3rCas3!"
# print(string.lower())

import random
name = input ("Please enter your full name without any space :")
result=""
while len(result)< 3:
    result+=name[random.randint(0,len(name))].lower()
result+=str(random.randint(1000,9999))
print(result)


