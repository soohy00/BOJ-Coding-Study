n = int(input())    # 수의 범위를 받아옴
a = 0   # 한수의 갯수를 세줄 변수

for i in range(1, n+1):     # 1부터 n까지 중에서 한수의 갯수를 구함
    if i<100:
        a += 1
    elif( (i//100-(i%100//10)) == ((i%100//10)-i%10) ):    # 100이 넘는수는 백의자리 수와 십의 자리 수의 차이가 십의 자리 수와 일의 자리 수의 차이가 같은지 확인하고 같으면 한수로 취급한다.
        a += 1
print(a)
