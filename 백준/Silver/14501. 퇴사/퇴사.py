import sys

N = int(input())    # 상담이 이루어지는 총 기간을 받아온다.
eff = []    # 날과 돈을 계산한다
fullpay = [0] * (N+1)   # 받을 수 있는 최대의 보수를 기록한다.

for i in range(N):  # 상담이 걸리는 시간과 받는 돈에 대한 정보를 받아온다.
    day, pay = map(int, sys.stdin.readline().split())
    eff.append([day, pay])

for a in range(N):  # 일자별로 진행중인 일의 보수와 a일의 보수를 비교하고, 더 나은 방법으로 변경한다.
    for b in range(a + eff[a][0], N+1):
        if fullpay[b] < fullpay[a] + eff[a][1]:
            fullpay[b] = fullpay[a] + eff[a][1]

print(fullpay[-1])
