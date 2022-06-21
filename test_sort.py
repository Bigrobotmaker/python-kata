A = [1, 2, 2, 3.5, 4, 5, 1.0, 3]
B = [0.1, -0.1, 0.2, -0.2, 0.3]
C = [1, 2, 3, 4, 3, 4, 3, 2, 1]
D = [1, 1, 1, 1, 2]

def unique_sort_f(x):
    one = 0
    two = 0
    three = 0
    four = 0
    
    
    x = sorted(x)
    # deep copy list by creating a new one
    z = [i for i in x]
    
    for y in x:
        if y == 1:
            one = one +1
        if y == 2:
            two = two + 1
        if y == 3:
            three = three + 1
        if y == 4:
            four = four + 1
        if one > 1:
            z.remove(1)
            one = one - 1
        if two > 1:
            z.remove(2)
            two = two - 1
        if three > 1:
            z.remove(3)
            three = three - 1
        if four > 1:
            z.remove(4)
            four = four - 1
    return z

def test_unique_sort():
    assert unique_sort_f(C) == [1, 2, 3, 4]
    assert unique_sort_f(D) == [1, 2]
 
