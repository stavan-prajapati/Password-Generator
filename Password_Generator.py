import random
import string
digits = string.digits
upper_case = string.ascii_uppercase
lower_case = string.ascii_lowercase
special_chars = "!@#$%^&*()_-+"

print("Welcome to Password Generator!!!")
print("""
For secure and reliable passwords, follow these recommendations:

- 8 to 12 Characters: Suitable for general accounts like social media, shopping websites, and personal apps. Recommended to include:
  - 2-3 Uppercase letters
  - 3-4 Lowercase letters
  - 2 Digits
  - 1-2 Special Characters

- 12 to 16 Characters: Ideal for sensitive accounts such as emails, financial services, and business platforms. Strongly recommended to include:
  - 3-5 Uppercase letters
  - 4-6 Lowercase letters
  - 3-4 Digits
  - 2-3 Special Characters
""")

num_of_passwords=int(input("How many password do you want ?\n"))
if num_of_passwords<=0:
    print("❗Error: Please enter a positive number for the number of passwords.")
else:  
    num_of_uppercase=int(input("How many Uppercase letters ?\n "))
    num_of_lowercase=int(input("How many Lowercase letters ?\n "))
    num_of_digits=int(input("How many Digits ?\n "))
    num_of_special_char=int(input("How many Special characters ?\n "))
    if num_of_lowercase<=0 or num_of_digits<=0 or num_of_special_char<=0 or num_of_uppercase <=0:
        print("❗Error: All character categories must have at least one character. Please try again.")
    else:    
        for i in range (1,num_of_passwords+1):
            password=(
            random.choices(digits, k=num_of_digits) + random.choices(upper_case, k=num_of_uppercase) + random.choices(lower_case, k=num_of_lowercase)+
            random.choices(special_chars, k=num_of_special_char))
            random.shuffle(password)
            print(f"Password {i} : {"".join(password)}")
