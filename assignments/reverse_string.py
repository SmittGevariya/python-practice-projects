s=input("enter a string:")
reversed_str = ""

for ch in s:
    reversed_str = ch + reversed_str   

print("Original:", s)
print("Reversed:", reversed_str)
