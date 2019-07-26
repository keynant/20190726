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



def getUnique(*args):
    newList = []
    for num in args:
        if args.count(num) == 1:
            newList.append(num)
    return tuple(newList)

def getNonUnique(*args):
    newList = []
    for num in args:
        if args.count(num) != 1:
            newList.append(num)
    return tuple(set(newList))

print(getUnique(1,2,3,1,2,3,1,5,7,9,6,6,6,8,7))
print(getNonUnique(1,2,3,1,2,3,1,5,7,9,6,6,6,8,7))

list1 = [1,2,3,4,5,6,7,1,3,5,7]

list2 = [n for n in list1 if list1.count(n) == 1]  # same as get unique
list3 = [n for n in list1 if list1.count(n) != 1]  # same as get non unique
print(list2)
print(sorted(set(list3)))
