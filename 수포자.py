def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer=[]
    points =[0,0,0]
    for i in range(len(answers)):
        if answers[i] == one[i%5]:
            points[0]+=1
        if answers[i] == two[i%8]:
            points[1]+=1
        if answers[i] == three[i%10]:
            print(answers[i])
            points[2]+=1
    print(points)        
    max_val = max(points)
    for i in range(3):
        if points[i] == max_val:
            answer.append(i+1)
    return answer

def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result