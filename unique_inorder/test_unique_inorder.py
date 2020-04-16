# Codewars Kata solution for Unique In Order
#
# Run using,
# 
# pytest -s test_unique_inorder.py


def unique_in_order(items):
    res = []
    for item in items:
        if len(res) == 0 or res[-1] != item:
            res.append(item)
    return res

def test_upper_string():
    print(unique_in_order('AAAABBBCCDAABBB'))
    assert unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']

def test_mixed_string():
    print(unique_in_order('ABBCcAD'))    
    assert unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D']

def test_list():
    print(unique_in_order([1,2,2,3,3]))
    assert unique_in_order([1,2,2,3,3]) == [1,2,3]

def test_empty_list():
    assert unique_in_order([]) == []
