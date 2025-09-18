# main.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    print("Все тесты пройдены!")

if __name__ == "__main__":
    test_add()