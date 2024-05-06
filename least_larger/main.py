def least_larger(a:list, index:int):
    target = a[index]

    temp = sorted(a)
    target_index = temp.index(target)

    if target_index + 1 >= len(temp):
        return -1
    else:
        return a.index(temp[target_index + 1])
    
def least_larger_solution(a, i):
    b = [x for x in a if x>a[i]]
    return a.index(min(b)) if b else -1