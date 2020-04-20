
def almost_everywhere_zero_bak(n, k, verbose=False):
  total = 0
  str_num = str(n).lstrip('0')
  d = len(str_num)
  if verbose:
    print(f'  n {n} has {d} digits.  Want {k} non zero digits.  String form of number: {str_num}')
  if k==0:
    return 1
  if d < k or k==0:
    return 0
  items_n = [int(v) for v in str_num]
  if verbose:
    print(f'  Array form items_n {items_n}')
  digit = items_n[0]
  # First digit zero. K remaining vary from 1 to 9.
  if d > 1 and d != k:
    permutations = binomialCoeff(d-1, k)
    nines = int(pow(9, k))
    total = permutations * nines
    if verbose:
      print(f'  Case first digit ZERO. binomialCoeff({d-1}, {k})={permutations} nines={nines} sub_total={total}')
  # First digit non-zero. K-1 remaining vary from 1 to 9.  
  permutations = binomialCoeff(d-1, k-1)
  nines = int(pow(9, k-1))
  sub_total = (digit-1)*nines*permutations
  if verbose:
    print(f'  Case first digit NOT zero. binomialCoeff({d-1}, {k-1})={permutations} first={digit} nines={nines} sub_total={sub_total}')
  total = total + sub_total
  if verbose:
    print(f'  Total: {total}')
  if len(str_num)>1:
    if verbose:
      print(f'  calling back into almost_everywhere_zero_analytic2({str_num[1:]}, {k-1}, {verbose})')
    total = total + almost_everywhere_zero_bak(int(str_num[1:]), k-1, verbose)
  else:
    total = total + 1
  return total

def binomialCoeff(n, k): 
    res = 1
    if (k > n - k) : 
        k = n - k 
    for i in range(0 , k) : 
        res = res * (n - i) 
        res = res // (i + 1) 
    return res 

def almost_everywhere_zero(n, k):
  total = 0
  str_num = str(n).lstrip('0')
  d = len(str_num)
  if k==0:
    return 1
  if d < k:
    return 0
  lead_digit = int(str_num[0])
  # First digit zero. K remaining vary from 1 to 9.
  if d > 1 and d != k:
    permutations = binomialCoeff(d-1, k)
    nines = int(pow(9, k))
    total = permutations * nines
  # First digit non-zero. K-1 remaining vary from 1 to 9.  
  permutations = binomialCoeff(d-1, k-1)
  nines = int(pow(9, k-1))
  sub_total = (lead_digit-1)*nines*permutations
  total = total + sub_total
  if len(str_num)>1:
    total = total + almost_everywhere_zero(int(str_num[1:]), k-1)
  else:
    total = total + 1
  return total

def test_small_values():
    assert almost_everywhere_zero(11,2) == 1
    assert almost_everywhere_zero(100,1) == 19
    assert almost_everywhere_zero(11,2) ==  1
    assert almost_everywhere_zero(20,2) ==  9
    assert almost_everywhere_zero(101,2 ) == 82
    assert almost_everywhere_zero(10001,2) == 487
    
def test_large_values():
    assert almost_everywhere_zero(10001000,2) == 1729
    assert almost_everywhere_zero(500309160,2) == 2604
    assert almost_everywhere_zero(10000000000000000000000, 3) == 1122660

def test_verylarge_values():
    assert almost_everywhere_zero(10000000000000000000000, 21) == 2407217760893271902598