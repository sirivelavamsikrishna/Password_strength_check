import string
import random
def len_7(password,l):
    if password.isdigit():
        print("strength: Week \nPassword must be at least 8 characters long \nSuggestion: Try adding more characters and special characters to make it stronger!")
    elif password.isalpha():  #(isinstance(password,str)):
        print("strength: Week \nPassword must be at least 8 characters long \nSuggestion: Try adding more numbers and special characters to make it stronger!")
        print("")
    elif password.isalnum():
        print("strength: Week \nPassword must be at least 8 characters long \nSuggestion: Try adding more special characters to make it stronger!")
    else:
        password.split()
        a,b,c=0,0,0
        al1 = list(string.ascii_lowercase)
        al2 = list(string.ascii_uppercase)
        nu = list(string.digits)
        s = list(string.punctuation)
        for i in range(len(password)):
            if password[i] not in nu:
                a += 1
        for i in range(len(password)):
            if password[i] not in al1 and password[i] not in al2:
                b += 1
        for i in range(len(password)):
            if password[i] in s:
                c += 1
        if a == l and b == l and c == l:
            print("strength: Week \nPassword must be at least 8 characters long \nSuggestion: Try adding more characters and special characters to make it stronger!")
        elif a == l:
            print("strength: Week \npassword must be at least 8 characters long \nSuggestion: Try adding more numbers to make it stronger!")
        elif b == l:
            print("strength: Week\nPassword must be at least 8 characters long\nSuggestion: Try adding more characters to make it stronger!")
        else:
            print("strength: Week\nPassword must be at least 8 characters long\nSuggestion: Try adding more than 8 characters to make it stronger!")

def len_8(password,l):
    if password.isdigit():
        print("strength: Moderate\nSuggestion: Try adding more characters and special characters to make it stronger!")
    elif password.isalpha():  # (isinstance(password,str)):
        print("strength: Moderate\nSuggestion: Try adding more numbers and special characters to make it stronger!")
    elif password.isalnum():
        print("strength: Moderate\nSuggestion: Try adding more special characters to make it stronger!")
    else:
        password.split()
        a,b,c=0,0,0
        al1 = list(string.ascii_lowercase)
        al2 = list(string.ascii_uppercase)
        nu = list(string.digits)
        s = list(string.punctuation)
        for i in range(len(password)):
            if password[i] not in nu:
                a += 1
        for i in range(len(password)):
            if password[i] not in al1 and password[i] not in al2:
                b += 1
        for i in range(len(password)):
            if password[i] in s:
                c += 1
        if a == l and b == l and c == l:
            print("strength: Moderate\nSuggestion: Try adding characters and numbers to make it stronger!")
        elif a == l:
            print("strength: Moderate\nSuggestion: Try adding numbers to make it stronger!")
        elif b == l:
            print("strength: Moderate\nSuggestion: Try adding characters to make it stronger!")
        else:
            print("strength: Moderate\nSuggestion: Try adding more than 8 characters to make it stronger!")

def len_10(password, l):
    if password.isdigit():
        print("strength: Strong\nSuggestion: Try adding more characters and special characters to make it stronger!")
    elif password.isalpha():  # (isinstance(password,str)):
        print("strength: Strong\nSuggestion: Try adding more numbers and special characters to make it stronger!")
    elif password.isalnum():
        print("strength: Strong\nSuggestion: Try adding more special characters to make it stronger!")
    else:
        password.split()
        a,b,c=0,0,0
        al1 = list(string.ascii_lowercase)
        al2 = list(string.ascii_uppercase)
        nu = list(string.digits)
        s = list(string.punctuation)
        for i in range(len(password)):
            if password[i] not in nu:
                a += 1
        for i in range(len(password)):
            if password[i] not in al1 and password[i] not in al2:
                b += 1
        for i in range(len(password)):
            if password[i] in s:
                c += 1
        if a == l and b == l and c == l:
            print("strength: Strong\nSuggestion: Try adding more characters and more numbers to make it stronger!")
        elif a == l:
            print("strength: Strong\nSuggestion: Try adding numbers to make it stronger!")
        elif b == l:
            print("strength: Strong\nSuggestion: Try adding characters to make it stronger!")
        else:
            print("strength: Strong")
def pass_suggestion():
    # store all characters in lists
    s1 = list(string.ascii_lowercase)
    s2 = list(string.ascii_uppercase)
    s3 = list(string.digits)
    s4 = list(string.punctuation)
   # Ask user about the number of characters
    user_input = input("How many characters do you want in your password? ")
    while True:  # check this input is it number? is it more than 8?
        try:
            characters_number = int(user_input)
            if characters_number < 8:
                print("Your number should be at least 8.")
                user_input = input("Please, Enter your number again: ")
            else:
                break
        except:
            print("Please, Enter numbers only.")
            user_input = input("How many characters do you want in your password? ")
    # shuffle all lists
    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)
    # calculate 30% & 20% of number of characters
    part1 = round(characters_number * (30 / 100))
    part2 = round(characters_number * (20 / 100))
    # generation of the password (60% letters and 40% digits & punctuations)
    result = []
    for x in range(part1):
        result.append(s1[x])
        result.append(s2[x])
    for x in range(part2):
        result.append(s3[x])
        result.append(s4[x])
    random.shuffle(result)
    password = "".join(result)
    return f"Strong Password:  {password}"

u_input = input("Enter your password: ")
len_of_passwd = len(u_input)
# print(f"Length of password: {len_of_passwd}")
listx = ["123456", "123456789", "qwerty", "password", "12345", "12345678", "abc123", "password1", "1234567",
         "1234567890"]
if u_input in listx:
    print("This is common password Please use a different password")
else:
    if len_of_passwd <= 0:
        print("Password cannot be None")
    elif len_of_passwd < 8:
        len_7(u_input, len_of_passwd)
    elif (len_of_passwd >= 8) and (len_of_passwd < 10):
        len_8(u_input, len_of_passwd)
    elif len_of_passwd >= 10:
        len_10(u_input, len_of_passwd)
if input("Do you want a strong password suggestion? (Yes/No): ").strip().lower() == "yes":
    print(pass_suggestion())
else:
    pass