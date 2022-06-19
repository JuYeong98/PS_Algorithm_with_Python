def solution(phone_number):
    length = len(phone_number)
    phone_number = '*'*(length-4) + phone_number[length-4:]
    return phone_number