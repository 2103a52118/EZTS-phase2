n=int(input("Enter size of row"))
d=int(input("Enter size of column"))
l1=[]
z=-1
for j in range(n*d):
        k=int(input("Enter matrix numbers"))
        l1.append(k)
print("Diagonal")
for i in range(n):
    for j in range(d):
        z+=1
        if(i==j):     
           print(l1[z],end=" ")
        else:
           print(" ",end=" ")
    print("")
print("Non diagonal")
z=-1
for i in range(3):
    for j in range(3):
        z+=1
        if(i!=j):     
           print(l1[z],end=" ")
        else:
           print(" ",end=" ")
    print("")
print("Upper matrix")
z=-1
for i in range(3):
    for j in range(3):
        z+=1
        if(i>=j):     
           print(l1[z],end=" ")
        else:
           print(" ",end=" ")
    print("")
print("Lower Matrix")
z=-1
for i in range(3):
    for j in range(3):
        z+=1
        if(i<=j):     
           print(l1[z],end=" ")
        else:
           print(" ",end=" ")
    print("")
