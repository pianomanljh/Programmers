def solution(phone_book):
    phone_book = set(phone_book)
    for item in phone_book:
        for i in range(len(item)):
            if item[:i] in phone_book:
                return False
    return True