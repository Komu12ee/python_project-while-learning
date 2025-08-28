import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


password=[]

print("Wellcom, to password generator")
ltr=int(input("how many letter in password you want?"))
num=int(input("how many number in password you want?"))
sym=int(input("how many symbol in password you want?"))

maxi=max(ltr,num,sym)
while maxi>0:
    if ltr:
     password.append(random.choice(letters))
     ltr-=1
    
    if num:
     password.append(random.choice(numbers))
     num-=1
    
    if sym:
     password.append(random.choice(symbols))
     sym-=1  
     
     maxi-=1 
print(password)   

# List to string  
# password=''.join(password) 
# print(password)

# different way to convert list in to string via loop
s = ''

# Loop through each character in list 'a' and add it to string 's'
for c in password:
    s += c

print(s)
