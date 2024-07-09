# 11-3 Employee
# # Without using a fixture
# from employee import Employee
#
#
# def test_give_default_raise():
#     """Test that the amount of a default raise is correct."""
#     test_employee = Employee('john', 'locke', 10000)
#     test_employee.give_raise()
#     assert test_employee.annual_salary == 15000
#
#
# def test_give_custom_raise():
#     """Test that the amount of a custom raise is correct."""
#     test_employee = Employee('john', 'locke', 10000)
#     test_employee.give_raise(6000)
#     assert test_employee.annual_salary == 16000


# Write a fixture, so you don’t have to create a new employee instance in each test function.
import pytest
from employee import Employee


@pytest.fixture
def create_test_employee():
    """An employee that will be available to all test functions."""
    test_employee = Employee('john', 'locke', 10000)
    return test_employee


def test_give_default_raise(create_test_employee):
    """Test that the amount of a default raise is correct."""
    create_test_employee.give_raise()
    assert create_test_employee.annual_salary == 15000


def test_give_custom_raise(create_test_employee):
    """Test that the amount of a custom raise is correct."""
    create_test_employee.give_raise(6000)
    assert create_test_employee.annual_salary == 16000
