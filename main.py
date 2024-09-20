import random
letters = ['a','b','c','d','e','f','g','h','i','j',
           'k','l','m','n','o','p','q','r','s','t',
           'u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J',
           'K','L','M','N','O','P','Q','R','S','T',
           'U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','&','(',')','*','+','-']
print("Welcome to Password Generator !!!")
n_ltrs = int(input("Enter how many letters you want in your password: "))
n_nums = int(input("Enter how many numbers you want in your password: "))
n_syms = int(input("Enter how many symbols you want in your password: "))
password =[]
for i in range(1,n_ltrs+1):
    char = random.choice(letters)
    password += char
for i in range(1,n_nums+1):
    char = random.choice(numbers)
    password += char
for i in range(1,n_syms+1):
    char = random.choice(symbols)
    password += char
print(password)
random.shuffle(password)
print(password)
psd = ""
for el in password:
    psd += el
print(psd)