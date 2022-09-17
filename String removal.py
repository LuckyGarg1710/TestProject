a=input("Enter the string= ")
b=input("Enter the substring= ")
d=input("Enter the replacement= ")
c=a.replace(b,d)       #this is a predefined python function working for strings.First parameter is the string you want to replace and second is the replacement.
if b in a:
    print(c)
else:
    print("The substring does not exist in string")
