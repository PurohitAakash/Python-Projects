n=27364
rev = 0
for i in range(1,n):
    n=n%2
    rev = rev + (rev*n)
    n=n/10
print(rev)

