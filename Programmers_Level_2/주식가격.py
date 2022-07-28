def solution(prices):
    answer = []
    price_length = len(prices)
    for i in range(price_length-1):
        current_price = prices[i]
        for j in range(i+1,price_length):
            if current_price > prices[j]:
                answer.append(j-i)
                #print(j-i)
                break
            else:
                if j == price_length-1:
                    answer.append(j-i)
                    #print(j-i)
    answer.append(0)
    return answer