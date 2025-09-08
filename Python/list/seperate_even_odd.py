l = input("Enter list").split()
for i in range(len(l)):
    l[i]= int(l[i])
    

def seperate_even_odd(l):
    even=[]
    odd=[]
    for x in l:
        if x%2==0:
            even.append(x)
        else:
            odd.append(x)
    return even, odd
even,odd = seperate_even_odd(l)
print(even)
print(odd)

    