email = input("Enter your email id :")  # Taking email input from the user
k = 0  # Flag to check if the email contains whitespace
j = 0  # Flag to check if any uppercase letter is present in an invalid way
d = 0  # Flag to check for any invalid character in the email

# Checking if the email length is at least 6 characters
if len(email) >= 6:
    
    # Checking if the first character is an alphabet (must start with a letter)
    if email[0].isalpha():
        
        # Checking if "@" is present exactly once in the email
        if ("@" in email) and (email.count("@") == 1):
            
            # Ensuring the email ends with a proper domain format (.com, .in, etc.)
            # The last "." should be either at -3rd or -4th position from the end
            if (email[-4] == ".") ^ (email[-3] == "."):  # XOR operator (^) ensures one of them is True
                
                for i in email:  # Iterating through each character in the email
                    
                    if i.isspace():  # Checking if the character is a space
                        k = 1  # Setting flag if space is found
                    
                    elif i.isalpha():  # Checking if the character is an alphabet
                        if i.isupper():  # Ensuring it is not uppercase
                            j = 1  # Setting flag if an uppercase letter is found
                    
                    elif i.isdigit():  # Checking if the character is a digit
                        continue  # Digits are allowed, so continue
                    
                    elif i == "_" or i == "." or i == "@":  # Allowing these special characters
                        continue
                    
                    else:
                        d = 1  # If any other character is found, set the invalid flag
                
                # Checking if any invalid flag is set
                if k == 1 or j == 1 or d == 1:
                    print("Wrong Email 5")  # Email contains whitespace, uppercase letters, or invalid characters
                else:
                    print("Right email")  # Email is valid

            else:
                print("Wrong Email 4")  # Invalid domain format (. must be at the correct position)

        else:
            print("Wrong Email 3")  # Either missing "@" or multiple "@" symbols present

    else:
        print("Wrong Email 2")  # Email does not start with an alphabet

else:
    print("Wrong Email 1")  # Email length is less than 6 characters
