# 반복해서 문장을 수행하는 경우 사용하는 while문(조건이 참일 동안 반복)
treeHit = 0 # 10번을 찍었을때 넘어가는 나무의 찍은 횟수를 저장하는 treeHit 변수
while treeHit < 10: # 나무를 찍은 횟수가 10보다 작은 동안 반복
    treeHit = treeHit + 1
    print(f"나무를 {treeHit}번 찍었습니다.")
    if treeHit == 10:
        print(f"{treeHit}번 찍은 나무 넘어갑니다.") # 10번까지 찍고 출력후, 거짓이 되어 문구 출력

# while 문을 통해 커피 판매, break문을 이용하여 강제로 while문 종료
coffee = 10
money = 300
while money:
    print("돈을 받았읜 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if not coffee: # 커피가 모두 떨어지면(not)
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# 조건에 맞지 않는 경우 맨 처음으로 돌아가는 continue문 사용
a = 0
while a<10:
    a = a+1
    if a % 2 == 0:
        continue # a%2의 값이 0일때(즉 짝수일 때) 맨 처음으로 돌아감
    print(a) # 짝수를 제외한 홀수값 출력

# 무한 루프(while True) 항상 참이므로, 무한 수행(break를 통해 중단)
# while True:
    # print("CTRL+C를 눌러야 while문을 빠져나갈 수 있습니다.") # 무한 실행되므로 종료
