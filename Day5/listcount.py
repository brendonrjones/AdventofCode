import collections
compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
with open('counter.csv', 'r') as array:
    numbers=list()
    N=0
    ind=0
    count=0
    for val in array:
        numbers.append(val)
    numbers = list(map(int, numbers))
    while ind<len(numbers):
        N=numbers[ind]
        if N>=3:
            numbers[ind]=numbers[ind]-1
        else:
            numbers[ind]=numbers[ind]+1
        ind=ind+N
        count=count+1
    print("Steps: ",count)
