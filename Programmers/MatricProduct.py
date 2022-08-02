def solution(arr1, arr2):

    arr1Row = len(arr1)
    arr1Column = len(arr1[0])

    arr2Row = len(arr2)
    arr2Column = len(arr2[0])

    answer = []
    for i in range(arr1Row):
        answer.append([])
        for j in range(arr2Column):
            temp = 0
            for k in range(arr1Column):
                temp += (arr1[i][k] * arr2[k][j])
            answer[i].append(temp)
    return answer

print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],[[5, 4, 3], [2, 4, 1], [3, 1, 1]]))