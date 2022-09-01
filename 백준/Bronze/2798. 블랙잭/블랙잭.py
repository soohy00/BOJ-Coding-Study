import sys

a, b = map(int, input().split())    # 카드 수와 M을 받는다
alist = list(map(int, sys.stdin.readline().split()))    # 카드에 적힌 수를 받는다.
c = 0

for e in range(0, a-2):  # 첫번째 카드
    for f in range(e+1, a-1):   # 두번째 카드
        for g in range(f+1, a):     # 세번째 카드
            if( alist[e] + alist[f] + alist[g] > b ):   # 카드에 적힌 수의 합이 M을 넘는다면 다시
                continue
            else:
                c = max(c, alist[e] + alist[f] + alist[g])  # 충족하는 모든 수들 중 최댓값을 구하기
print(c)