import sys

Num = int(sys.stdin.readline()) # 몇번 째 영화를 이름지을지 받아온다.
count = 0   # 몇번째 영화인지 적는다.
six = 666   # 영화 제목에 적힐 종말의 숫자이다

while True:
    if '666' in str(six):   # six에 종말의 숫자가 들어간다면 count +1을 한다.
        count += 1
    if count == Num:    # N번째 영화에 도착했다면 해당 종말의 숫자를 출력하고 반복을 멈춘다.
        print(six)
        break
    six += 1
