a = [True]*11150    # 1001*b + 101*c + 11*d + 2*e의 합이 11150이기 때문에
for b in range(10):     # 셀프넘버가 아닌 수를 구하고, 이를 a리스트에서 True > False로 바꾼다
    for c in range(10):
        for d in range(10):
            for e in range(10):
                a[1001*b + 101*c + 11*d + 2*e] = False

for i in range(10000):  # a리스트 내에 10000이하인 수 중에서 True인 수만 출력한다.
    if a[i] == True:
        print(i)