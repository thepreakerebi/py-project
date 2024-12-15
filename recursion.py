# def recur(num):
#     if num >= 9:
#         return num + 1
    
#     total = num + 1
#     print(total)

#     return recur(total)


# recur(0)

def recur_loop(num):
    for i in range(num, 9):
        total = i + 1
        print(total)
        return recur_loop(total)

recur_loop(0)