def solution(money, minratio, maxratio, ranksize, threshold, months):
    answerMoney = money

    for i in range(months):

        # 백의 자리까지 버림
        tempMoney = answerMoney - (answerMoney % 100)

        # 세율이 0인 경우
        if minratio == 0 and maxratio == 0:
            break;

        # 소유 가정 금액이 threshold 미만인 경우 -> 더이상 변동 없음, 종료
        if tempMoney < threshold:
            break;

        # 이제 진짜 시작
        plusPercent = tempMoney - threshold
        plusPercent = plusPercent // ranksize

        rate = minratio + plusPercent

        if rate > maxratio:
            rate = maxratio

        sendMoney = tempMoney * rate // 100
        answerMoney -= sendMoney

    return answerMoney