def solution(s):
    answer = True

    if (len(s) == 4) or (len(s) == 6):
        try: 
            s = int(s)

        except Exception as E:
            answer = False

    else:
        answer = False

    return answer

def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)