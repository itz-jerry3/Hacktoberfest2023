str = input("Enter a string : ")
print(str)
s = input("Enter the word you want to search : ")
x = str.casefold()
s = s.casefold()
c = x.count(s)
print(c," Times")
