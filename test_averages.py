A = [1, 2, 2, 3.5, 4, 5, 1.0, 3]
B = [0.1, -0.1, 0.2, -0.2, 0.3]
C = [1, 2, 3, 4, 3, 4, 3, 2, 1]
D = [1, 1, 1, 1, 2]

def mean_f(x):
    mean = 0.0
    for y in x:
        mean = mean + y

    mean = mean/len(x)
    
    return mean
    
def median_f(x):
    median = 0.0
    x = sorted(x)
    if int(len(x))%2 == 0: 
        median = x[int(len(x)/2)]
        median2 = x[int((len(x)/2)-1)]
        median = (median + median2)/2
    else:
        median = x[int(len(x)/2)]
    return median

def mode_f(x):
    mode = 0
    d = {}
    for y in x:
        d[y] = 0
    
    for y in x:
        d[y] = (d[y] + 1)

    largestv = 0
    for k, v in d.items():    
        print(k, v)
        if v > largestv:
            mode = k
            largestv = v
        
    return mode
    
def range_f(x):
    ran = 0.0
    x = sorted(x)
    ran =(x[len(x)-1] - x[0])
    return ran
def sum_f(x):
    # write some code to add up numbers in a list
    return 0.0

def test_mean():
    assert mean_f(A) == 2.6875
    assert mean_f(B) == 0.06
 
def test_median():
    assert median_f(A) == 2.5
    assert median_f(B) == 0.1
    
def test_mode():
    assert mode_f(C) == 3
    assert mode_f(D) == 1
    
def test_range():
    assert range_f(A) == 4
    assert range_f(B) == 0.5
def test_sum():
    assert sum_f(A) == 21.5
    assert sum_f(C) == 23
    
    
