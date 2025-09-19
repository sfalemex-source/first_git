import pytest
import allure

@allure.step("Сложение {a} и {b}")
def add(a, b):
    return a + b

@allure.title("Тест сложения положительных чисел")
def test_add_positive():
    with allure.step("Выполняем сложение 2 + 3"):
        result = add(2, 3)
    assert result == 5

@allure.title("Тест сложения отрицательных чисел")
def test_add_negative():
    with allure.step("Выполняем сложение -1 + 1"):
        result = add(-1, 1)
    assert result == 0

@allure.title("Тест сложения с нулем")
def test_add_with_zero():
    with allure.step("Выполняем сложение 5 + 0"):
        result = add(5, 0)
    assert result == 5

if __name__ == "__main__":
    pytest.main(["-v", "--alluredir=./allure-results"])