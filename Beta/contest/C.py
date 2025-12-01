n, m = map(int, input().split())
last_team = {} 

for _ in range(m):
    team_number, word = input().split()
    last_team[word] = int(team_number)

answers = [0] * n

for team in last_team.values():
    answers[team - 1] += 1

print(' '.join(map(str, answers)))
