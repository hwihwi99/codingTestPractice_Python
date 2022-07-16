T = int(input())

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

for i in range(T):
    a,b = map(int, input().split())
    g = gcd(a,b)
    mcd = a * b // g
    print(mcd)
