def email_validator(a):
    if "@example.com" in a or "@gmail.com" in a or "@email.com" in a or ".com"in a:
      return "Valid Mail Address "
    else:
      return "Not a Valid Address" 
    
a=input("Enter your email ID: ")
print(email_validator(a))