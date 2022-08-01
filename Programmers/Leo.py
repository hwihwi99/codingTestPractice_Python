'''
처음에 (width * height == yellow) 이 부분을 안넣고 실행시켰더니
// 2 했을 때 반이 되는 것은 잡지만 yellow와 갯수가 다른 것도 카운트되었다.

그래서 저 조건을 넣어주니까 풀 수 있었다.
b b b b b
b y y y b
b b b b b

무조건 테두리는 브라운이고 가운데는 노란색인데 브라운과 노란색이 들어왔을 때 전체 사각형의 가로, 세로 길이 구하기
무조건 가로 >= 세로임
'''
import math

def solution(brown, yellow):
    answer = []
    half_round = (brown-4)//2
    for i in range(1, int(math.sqrt(yellow))+1):
        width = yellow // i
        height = i
        if (width * height == yellow) and (width + height == half_round):
            answer.append(width+2)
            answer.append(height+2)
            break
    return answer

print(solution(16,9))