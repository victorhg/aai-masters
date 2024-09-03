score = [199,97, 97, 93, 90, 87, 81,  75, 60]

totalSum = 0 
for x in score:
    totalSum += x

mean = totalSum / len(score)

print(mean)
