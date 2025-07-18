# tool_calculator.py

from langchain.tools import tool

@tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@tool
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b

@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

@tool
def divide(a: float, b: float) -> float:
    """Divide a by b. Returns error if b is 0."""
    if b == 0:
        return "❌ Cannot divide by zero."
    return a / b

# Export tools as list
calculator_tools = [add, subtract, multiply, divide]

