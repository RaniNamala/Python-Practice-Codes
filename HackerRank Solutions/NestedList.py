li = []
n = int(input())
for i in range(n):
    name = input()
    score = float(input())
    li.append([name,score])
score = []
for name, score in li:
    score.append(score)
score = list(set(scores))
scores.sort()
secound_smallest = score[i]
names_li = []
for name, score in li:
    if score == second_smallest:
        names_li.append(name)

names_li.sort()    
    
        
                