
def tribonacci(signature, n):
    res = []
    # Handle bad inputs
    if len(signature) != 3 or n <= 0:
        return res
    # Cases where n is less than size of signature   
    if n < 3:
        return signature[:n]
    # All inputs are good - calc Tribonacci.    
    res = signature
    (a, b, c) = signature
    for _ in range(n-3):
        sum = a + b +c
        res.append(sum)
        (a, b, c) = (b, c, sum)
    return res
    
def test_bad_signature():
    assert tribonacci([], 3) == []
    assert tribonacci([1], 3) == []
    assert tribonacci([1,1], 3) == []

def test_bad_n():
    assert tribonacci([1,1,1], 0) == []

def test_one():
    assert tribonacci([1, 1, 1], 1) == [1]

def test_two():
    assert tribonacci([1, 1, 1], 2) == [1, 1]

def test_three():
    assert tribonacci([1, 1, 1], 3) == [1, 1, 1]

def test_ten_001():
    assert tribonacci([1, 1, 1], 10) == [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]

def test_ten_011():
    assert tribonacci([0, 1, 1], 10) == [0, 1, 1, 2, 4, 7, 13, 24, 44, 81]

def test_ten_100():
    assert tribonacci([1, 0, 0], 10) == [1, 0, 0, 1, 1, 2, 4, 7, 13, 24]

def test_ten_000():
    assert tribonacci([0, 0, 0], 10) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def test_ten_123():
    assert tribonacci([1, 2, 3], 10) == [1, 2, 3, 6, 11, 20, 37, 68, 125, 230]

def test_ten_321():
    assert tribonacci([3, 2, 1], 10) == [3, 2, 1, 6, 9, 16, 31, 56, 103, 190]

def test_one_111():
    assert tribonacci([1, 1, 1], 1) == [1]

def test_zero_300():
    assert tribonacci([300, 200, 100], 0) == []

def test_30_05():
    assert tribonacci([0.5, 0.5, 0.5], 30) == [0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5, 52.5, 96.5, 177.5, 326.5, 600.5, 1104.5, 2031.5, 3736.5, 6872.5, 12640.5, 23249.5, 42762.5, 78652.5, 144664.5, 266079.5, 489396.5, 900140.5, 1655616.5, 3045153.5, 5600910.5, 10301680.5]

"""    
Test.assert_equals(tribonacci([0, 0, 1], 10), [0, 0, 1, 1, 2, 4, 7, 13, 24, 44])
Test.assert_equals(tribonacci([0, 1, 1], 10), [0, 1, 1, 2, 4, 7, 13, 24, 44, 81])
Test.assert_equals(tribonacci([1, 0, 0], 10), [1, 0, 0, 1, 1, 2, 4, 7, 13, 24])
Test.assert_equals(tribonacci([0, 0, 0], 10), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
Test.assert_equals(tribonacci([1, 2, 3], 10), [1, 2, 3, 6, 11, 20, 37, 68, 125, 230])
Test.assert_equals(tribonacci([3, 2, 1], 10), [3, 2, 1, 6, 9, 16, 31, 56, 103, 190])
Test.assert_equals(tribonacci([1, 1, 1], 1), [1])
Test.assert_equals(tribonacci([300, 200, 100], 0), [])
Test.assert_equals(tribonacci([0.5, 0.5, 0.5], 30), [0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5, 52.5, 96.5, 177.5, 326.5, 600.5, 1104.5, 2031.5, 3736.5, 6872.5, 12640.5, 23249.5, 42762.5, 78652.5, 144664.5, 266079.5, 489396.5, 900140.5, 1655616.5, 3045153.5, 5600910.5, 10301680.5])
"""