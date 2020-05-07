scores = []
with open("name_score.txt") as f:
    for line in f:
        name, score = line.split(':')
        scores.append((int(score)))

for onlyscore in scores:
    print(onlyscore)