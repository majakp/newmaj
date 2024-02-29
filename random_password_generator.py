#random password generator

from random import choice

def generate_password(number):
    numbers = ['1','2','3','4','5','6','7','8','9']
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v']
    symbols = ['#','%','*','&','^','@','!','|','/']

    chars=numbers+letters+symbols
    pwd = []
    for num in range(number):
        char=choice(chars)
        pwd.append(char)
    password =''.join(pwd)
    return password

pwd = generate_password(15)
print(pwd)
    
    
 

