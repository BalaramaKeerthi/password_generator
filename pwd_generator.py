"""
we have to ask some questions from user
collect user preferences
-length
-should contain any special characters
-should contain any digits
-should contain any letters

create all available characters 
randomly pick characters up to the length
ensure we have at least one of the each character type
ensure length is valid
"""
import random
import string
def generate_password():
    length=int(input("Enter the desired password length: ").strip())
    include_uppercase=input("Include uppercase letters? (yes/no):").strip().lower()
    include_special=input("Include special characters? (yes/no):").strip().lower()
    include_digits=input("Include digits? (yes/no):").strip().lower()
    include_lowercase=input("Include lowercase letters? (yes/no):").strip().lower()
    if length<4:
        print("Password length must be at least 4 characters.")
        return
    
    lower=string.ascii_lowercase if include_lowercase == "yes" else ""
    upper=string.ascii_uppercase if include_uppercase == "yes" else ""
    special=string.punctuation if include_special=="yes" else ""
    digits=string.digits if include_digits=="yes" else ""
    all_characters=lower+upper+special+digits

    required_characters=[]
    if include_uppercase=="yes":
        required_characters.append(random.choice(upper))
    if include_lowercase=="yes":
        required_characters.append(random.choice(lower))
    if include_special=="yes":
        required_characters.append(random.choice(special))
    if include_digits=="yes":
        required_characters.append(random.choice(digits))
    
    remaining_length=length-len(required_characters)
    password=required_characters

    for _ in range(remaining_length):
        character=random.choice(all_characters)
        password.append(character)
    random.shuffle(password)
    str_password="".join(password)
    return str_password
password=generate_password()
print(password)





