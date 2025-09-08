l = [1,2,3,4,5,6]
x = 5
# print all the elements less htan x
def smaller(l,x):
    res = []
    for i in l:
        if i<x:
            res.append(i)
    return res
x = smaller(l,x)
print(x)
