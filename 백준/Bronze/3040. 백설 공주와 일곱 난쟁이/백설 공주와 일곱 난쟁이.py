import sys

acc = []
a, b = 0, 0

for i in range(9):  # 아홉 난쟁이의 키를 alist라는 리스트에 받아온다
    acc.append(int(sys.stdin.readline()))

all = sum(acc) - 100    # 일곱 난쟁이의 키의 합은 100이다.

for j in range(9):   # 가짜 두 난쟁이의 키의 합이 40이 되는 경우를 찾아 리스트에서 제거한다.
    for k in range(j+1, 9): # j = k 일 수 있기 때문에
        if acc[j] + acc[k] == all:
            a = acc[j]
            b = acc[k]

acc.remove(a)
acc.remove(b)
acc.sort()

for v in acc:   # 일곱 진짜 난쟁이들을 키 오름차순으로 출력한다.
    print(v)

