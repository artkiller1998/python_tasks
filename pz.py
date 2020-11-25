def calc(a, b, op):
    operations = {
        '+' : int.__add__,
        '-': int.__sub__,
        '*': int.__mul__,
        '/': int.__floordiv__}
    op = operations.get(op)
    return op(a, b)

# def calc(a, b):
#     try:
#         return int(a)+int(b)
#     except ValueError:
#         return 'Ошибка! Неверный тип входных данных.'
#
# def main():
#     print(calc('ada', 44))
#
# if __name__ == '__main__':
#     main()