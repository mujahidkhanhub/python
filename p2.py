"""k=1
n=int(input("emter no of rows:"))
for i in range(0,n):
    for j in range(0,n):
        if j<=i:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    for j in range(0,n-i-1):
            print(" ",end='')
    for j in range(0,n ):
        print("*",end=' ')
    print()
"""
a=1
while(a==1):
    n=int(input("emter no of rows:"))
    m=n+(n-1)
    for i in range(0,n):
        for j in range(0,m):
            if j<=i or j>=m-i-1:
                print("j",end=' ')
            else:
                print(" ",end=' ')
        print()
    for i in range(0,n):
        for j in range(0,m):
            if j<=n-i-1 or j>=2+i:
                print("*",end=' ')
            else:
                print(" ",end=' ')
        print()
    a=int(input("enter 1 to continue:"))

