# x = int(input('Enter the first number: '))
# y = int(input('Enter the second number: '))
# print(x/y)

# try:
#     x = int(input('Enter the first number: '))
#     y = int(input('Enter the second number: '))
#     print(x/y)
# except ZeroDivisionError:
#     print('The second number cannot be zero!')

class MuffledCalculator:
    muffled = False
    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print('Division by zero is illegal')
            else:
                raise # raise the exception to the caller

calculator = MuffledCalculator()
calculator.calc('10/2')
calculator.muffled = True
calculator.calc('10/0')