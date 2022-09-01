import sys

N = int(sys.stdin.readline())   # 줄의 갯수를 받아온다.
num = list(map(int, sys.stdin.readline().split()))  # 연산자를 끼워넣을 수를 받아온다.
operators = list(map(int, sys.stdin.readline().split()))  # 받아오는 순서대로 +, -, *, //의 갯수이다.

mx, mn = -1e9, 1e9  # 항상 -10억보다 크거나 같다. 혹은 10억보다 작거나 같다.


def dfs(depth, total, plus, minus, multiplication, division):   # 각각 깊이, 총 합, 연산자의 계산을 하여 갯수를 소비했는지를 기록한다.
    global mx, mn
    if depth == N:
        mx = max(mx, total)  # -10억 ~ total 값에서 최대 값을 찾는다.
        mn = min(mn, total)  # 10억 ~ total 값에서 최소 값을 찾는다.
        return

    if plus:    # 3번째 줄 1번 째 수가 양수일 경우
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiplication, division)
    if minus:   # 3번째 줄 2번 째 수가 양수일 경우
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiplication, division)
    if multiplication:  # 3번째 줄 3번 째 수가 양수일 경우
        dfs(depth + 1, total * num[depth], plus, minus, multiplication - 1, division)
    if division:    # 3번째 줄 4번 째 수가 양수일 경우
        dfs(depth + 1, int(total // num[depth] if total > 0 else -((-total)//num[depth])), plus, minus, multiplication, division - 1)


dfs(1, num[0], operators[0], operators[1], operators[2], operators[3])

print(mx)
print(mn)