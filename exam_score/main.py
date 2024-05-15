def check_exam(arr1,arr2):
    result = [answer for i, answer in enumerate(arr2) if answer == arr1[i] or answer == ""]
    mark = sum(list(map(lambda result : 0 if result == "" else 4, result)))
    return mark + (len(arr1)-len(result))*-1 if mark + (len(arr1)-len(result))*-1>0 else 0


print(check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]))