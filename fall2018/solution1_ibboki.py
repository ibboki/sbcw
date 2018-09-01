xs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

## Problem 1.1
def square(xs):
    result = []
    for i in xs:
        result.append(i**2)
    return result
   
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(square(xs))

## Problem 1.2
def even(xs):
    result = []
    resultSqure = square(xs)
    for i in resultSqure:
        if i%2 == 0:
            result.append(i)
    return result

#[4, 16, 36, 64, 100]
print(even(xs))

## Problem 2
text = 'alejandro, britney, christina, dennis, emily'
textAddr = '@gmail.com; '

def convert(text):
    rstSplit = []
    rstSplit = text.split(", ")
    result = textAddr.join(rstSplit)
    return result + "@gmail.com"

#alejandro@gmail.com; britney@gmail.com; christina@gmail.com; dennis@gmail.com; emily@gmail.com
print(convert(text))

## Problem 3
## Problem 3.1
xs = [5, 10, 15, 20, 25, 30, 35, 40]
ys = [9, 2, 3, 8, 10, 5, 21, 7]

def intersection(xs, ys):
    result = []
    for i in xs:
        if i in ys:
            result.append(i)     
    return result

#[5, 10]
print(intersection(xs, ys))

## Problem 3.2
xs = [1, 2, 3, 4]
ys = [3, 4, 5, 6]

def union(xs, ys):
    result = []
    xs.extend(ys)
    rstExtend = xs
    rstExtend.sort()

    j = 0
    for i in rstExtend:
        if i == j:
            rstExtend.remove(i)
            i += 1
        j = i
    result = rstExtend
    return result
#[1, 2, 3, 4, 5, 6]
print(union(xs, ys))

## Problem 4
inventory = {
    'avocado': 236,
    'apple': 0,
    'orange': 172,
    'mango': 368,
}
prices = {
    'avocado': 0.99,
    'apple': 0.69,
    'orange': 0.33,
    'mango': 0.79
}
def net_asset_value(inventory, prices):
    result = []
    rstSum = 0
    for i in inventory.keys():
        for j in prices.keys():
            if i == j:        
                rstSum += inventory.get(i) * prices.get(i)
    result = rstSum
    return result

print(net_asset_value(inventory, prices))