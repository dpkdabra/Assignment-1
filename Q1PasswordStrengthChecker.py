import re

def check_password_strength(p):
    
    valid = True
    
    if len(p) < 8:
        valid = False
        
    if not re.search("[a-z]", p):
        valid = False
        
    if not re.search("[A-Z]", p):
        valid = False
        
    if not re.search("[0-9]", p):
        valid = False
        
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", p):
        valid = False
        
    return valid


user_input = input("Enter password: ")
result = check_password_strength(user_input)

if result == True:
    print("Strong Password")
else:
    print("Weak Password")