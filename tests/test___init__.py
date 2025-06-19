import pytest
from src.operations import Addition, Subtraction, Multiplication, Division, Square, SquareRoot

# Mocking external dependencies
class MockDependency:
    @staticmethod
    def method():
        return "mocked"

def test_addition(monkeypatch):
    monkeypatch.setattr('src.operations.Addition.operation', MockDependency().method)
    addition = Addition()
    assert addition.operation("x", "y") == "mocked"

def test_subtraction(monkeypatch):
    monkeypatch.setattr('src.operations.Subtraction.operation', MockDependency().method)
    subtraction = Subtraction()
    assert subtraction.operation("x", "y") == "mocked"

def test_multiplication(monkeypatch):
    monkeypatch.setattr('src.operations.Multiplication.operation', MockDependency().method)
    multiplication = Multiplication()
    assert multiplication.operation("x", "y") == "mocked"

def test_division(monkeypatch):
    monkeypatch.setattr('src.operations.Division.operation', MockDependency().method)
    division = Division()
    assert division.operation("x", "y") == "mocked"

def test_square(monkeypatch):
    monkeypatch.setattr('src.operations.Square.operation', MockDependency().method)
    square = Square()
    assert square.operation("x") == "mocked"

def test_squareroot(monkeypatch):
    monkeypatch.setattr('src.operations.SquareRoot.operation', MockDependency().method)
    squareroot = SquareRoot()
    assert squareroot.operation("x") == "mocked"