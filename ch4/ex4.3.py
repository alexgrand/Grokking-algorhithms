def find_max(ls):
    if len(ls) == 1:
        return ls[0]
    
    if ls[0] < ls[1]: ls.pop(0)
    else: ls.pop(1)
        
    return find_max(ls)

# def find_max(ls):
#     if len(ls) == 2:
#         return ls[0] if ls[0] > ls[1] else ls[1]
#     sub_max = find_max(ls[1:])
#     return ls[0] if ls[0] > sub_max else sub_max


ls = [1, 72, 19, 44, 2, 72, 5, 9]
print(find_max(ls[:]))
