# 계단 오르기 게임은 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 가는 게임이다.
# <그림 1>과 같이 각각의 계단에는 일정한 점수가 쓰여 있는데 계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 된다.
# <그림 1>
# 예를 들어 <그림 2>와 같이 시작점에서부터 첫 번째, 두 번째, 네 번째, 여섯 번째 계단을 밟아 도착점에 도달하면 총 점수는 10 + 20 + 25 + 20 = 75점이 된다.
# <그림 2>
# 계단 오르는 데는 다음과 같은 규칙이 있다.
# 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 마지막 도착 계단은 반드시 밟아야 한다.
# 따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다.
# 하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 첫 번째, 두 번째, 세 번째 계단을 연속해서 모두 밟을 수는 없다.
# 각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.

# 입력의 첫째 줄에 계단의 개수가 주어진다.
# 둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다.
# 계단의 개수는 300이하의 자연수이고, 계단에 쓰여 있는 점수는 10,000이하의 자연수이다.

# 첫째 줄에 계단 오르기 게임에서 얻을 수 있는 총 점수의 최댓값을 출력한다.

c = int(input())
dp = []

n = []
for _ in range(c):
    n.append(int(input()))

# 1. 계단은 한 칸 혹은 두 칸씩 오를 수 있다.
# 2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. => 한 칸씩 두 번 오른 뒤엔 반드시 다음은 두 칸 올라가야함.
# 3. 마지막 도착 계단은 반드시 밟아야 한다. => step이 2개 남아있을 때 end-1 밟기 가능, 1개 남아있을 때 end-1 밟기 불가능.
#    -> 밟은 계단이 "end-1"일 경우 "end-2" 계단은 밟은 상태이면 안 된다. - case A
#    -> 밟은 계단이 "end-2"일 경우는 상관 없다. - case_B

# dp에 지금까지 밟는 스텝 중 가장 높은 값을 누적해서 저장시킴.
# 처음 절차는 손으로 넣어주는 이유
# - 그 이후 스텝은 건너뛰기와 건너뛰지 않은 것 중 큰 값을 저장시킬 것인데, 그러기 위한 초기 dp 세팅값이 필요하기 때문.

# 첫 스텝은 그냥 저장.
dp.append(n[0])

if c > 1:
    # 첫 칸 두 칸 진행한 값을 저장.
    dp.append(n[0] + n[1])
if c > 2:
    # 첫 스텝 + 두 칸 뛰기랑 한 칸 뛰기 + 두 칸 뛰기 중 뭐가 더 나은지 계산해서 더 높은걸로 저장.
    dp.append(max(n[0] + n[2], n[1] + n[2]))

    # 이후는 남은 스텝이 1인 케이스(한 계단 건너뛰어서 도착한 케이스)와 남은 케이스가 0(이전 계단을 밟은 케이스)인 것 중 큰 값으로 저장.
    # 내부 계산식은 메모이제이션 인덱스를 2~3개 이전을 참조하는 식으로 취해줬는데, 이것은 마지막 계단을 반드시 밟도록 하기 위해서임.
    # 마지막 계단을 밟을 수 있는 경우의 수
    # 1. c - 1 지점에서 스텝이 1 남은 경우
    # 2. c - 2 지점에 서있는 경우.
    # 즉, ex) c = 30이라면, [28, 30] 케이스 및 [27, 29, 30] 케이스여야만 함.
    for i in range(3, c):
        dp.append(max(dp[i - 2] + n[i], dp[i - 3] + n[i] + n[i - 1]))

# 리스트에 값이 누적되면 마지막 값이 최대값이 됨. pop 하면 끝
print(dp.pop())