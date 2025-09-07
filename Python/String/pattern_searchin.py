a = input("Enter a string")
b = input("Enter the pattern to be searched")
pos = a.find(b)
while pos>=0:
    print(pos," ")
    pos = a.find(b,pos+1)
