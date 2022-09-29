N = int(input())
arrayList = []

for _ in range(N):
    strInput = input()
    arrayList.append([strInput, len(strInput)])

arrayList.sort(key=lambda x:(x[1],x[0]))

result = []
for s, n in arrayList:
    if s not in result:
        print(s)
        result.append(s)

