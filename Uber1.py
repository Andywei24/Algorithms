def solution(diffs):
    sum = 1500
    max_score = 1500
    min_score = 1500
    for i in range(len(diffs)):
        sum += diffs[i]
        max_score = max(sum, max_score)
        min_score = min(sum, min_score)
        i += 1
    return [max_score, min_score]
diffs = [-100, 200, 350, 450, -200]
print(solution(diffs))