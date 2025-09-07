a = input("Enter a word")
j =len(a)-1
i =0
while i<j:
    if a[i]==a[j]:
        i=i+1
        j=j-1
    else:
        print("NOPE")
        break
else:
    print("yes")

#     🔹 How else works with loops

# In Python, a loop (while or for) can have an else block.

# The else part runs only if the loop finishes normally (i.e., no break happens).

# If the loop is exited early with break, the else block is skipped.

