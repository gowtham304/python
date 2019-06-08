def main():
    s=input("enter a string")
    k=string_alternative(s)
    return k


def string_alternative(s):
    b=""
    for i in range(len(s)):
        if (i % 2) == 0:
          b+= s[i]
    return b

print(main())
