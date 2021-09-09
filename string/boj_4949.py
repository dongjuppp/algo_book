def checkString(target):
    lt = list(target)
    small = []

    for i in range(len(lt)):
        if lt[i] == '(' or lt[i] == '[':
            small.append(lt[i])

        if lt[i] == ')':
            if len(small) == 0:
                return False
            top = small.pop()
            if top == '[':
                return False
        if lt[i] == ']':
            if len(small) == 0:
                return False

            top = small.pop()
            if top == '(':
                return False
    if len(small) == 0:
        return True
    else:
        return False

while True:
    target = input()
    if target=='.':
        break

    if checkString(target):
        print('yes')
    else:
        print('no')
    