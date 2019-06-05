def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = "PYTHON"
k= s.replace("PYTHON","PYTN")

print("The original string  is : ")
print(s)
print("The reversed string is : ")
print(reverse(k))
s = "PYTHON"
print(s)
k=s[:3]+s[5:]
print(k[::-1])