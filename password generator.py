import random 

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz" 
numbers = "0123456789"
symbols = "!@#$%^&*?"

add = upper + lower + numbers + symbols
length = 9
password = "".join(random.sample(add,length))
print("The generated password is ",password)