#Ab_NLC_1.0
#Global
import math
def calculate_expression(expression):
    math_functions = {
        'log': math.log10,
        'ln': math.log,
        'sqrt': math.sqrt,
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'e': math.e,
        'pi': math.pi,
        'cbrt': lambda x: x**(1/3)
    }
    expression = expression.replace('^', '**')
    try:
        for func in math_functions:
            expression = expression.replace(func, f'math_functions["{func}"]')
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}."

#Main
print("Natural language calculator.")
while True:
    user_input = input("Enter an operation or ""exit"" to close: ")
    if user_input.lower() == 'exit':
        break
    result = calculate_expression(user_input)
    print("Result:", result)