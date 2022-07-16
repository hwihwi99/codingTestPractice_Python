A, B = map(int,input().split())
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

gcd = gcd(A, B)
mcd = A * B // gcd
print(gcd)
print(mcd)