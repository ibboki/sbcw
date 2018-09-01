xs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

## Problem 1.1
def square(xs):
    rstSquare = []
    for i in xs:
        rstSquare.append(i**2)
    return rstSquare
   
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(square(xs))

## Problem 1.2
def even(xs):
    rstEven = []
    result = square(xs)
    for i in result:
        if i%2 == 0:
            rstEven.append(i)
    return rstEven    

#[4, 16, 36, 64, 100]
print(even(xs))

## Problem 2
def convert(text):
    text = 'alejandro, britney, christina, dennis, emily'

