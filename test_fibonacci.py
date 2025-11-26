# Function created only for testing purpose
def fib_sum(n):
    a = 0
    b = 1
    total = 0

    for i in range(n):
        total += a
        a, b = b, a + b

    return total


def test_fib_sum():
    assert fib_sum(1) == 0          
    assert fib_sum(2) == 1          
    assert fib_sum(5) == 7          
    assert fib_sum(7) == 20         
    assert fib_sum(0) == 0          