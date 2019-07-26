def sumArgs(*args):
    sum = 0
    for num in args:
        sum+=num
    return sum


print(sumArgs(1,2,3,4,56,7.345,8,4434634))


def toList(*args):
    lst1 = []
    for item in args:
        lst1.append(item)
    return lst1

print(toList(1,2))

def myStat(key1, **kwargs):
    for k,v in kwargs.items():
        print(f'key is {k}, value is {v}')
    if key1 in kwargs.keys():
        return True
    if key1 in kwargs.values():
        return True
    else: return False



print(myStat("name", name=11,keys = "shleem"))
