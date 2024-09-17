# recursion is a technique where a function calls itself to solve a problem
# breaking down a huge problem to small pieces type of thing
# base case stops the recursion

def count_dolls(doll):
    # base case:small doll
    if doll.is_smallest():
        return 1
        # recursive case:larger doll
    else:
        inner_dolls = doll.get_inner_dolls()
        count = 1
        for inner_doll in inner_dolls:
            # recursively count the dolls inside
            count += count_dolls(inner_doll)
        return count

def add_one(num):

    if (num >= 9):
        return num + 1

    total = num + 1
    print(total)

    return add_one(total)


mynewtotal = add_one(0)
print(mynewtotal)