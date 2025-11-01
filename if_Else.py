# This program reads an integer from input and prints "Weird" or "Not Weird"
n = int(input())
if n % 2 != 0:
    print("Weird")
else:
    if n >= 2 and n <= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    else:
        print("Not Weird")
#for my leaning references

