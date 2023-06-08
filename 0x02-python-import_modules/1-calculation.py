#!/usr/bin/python3
if __name__ == __main__:
    from calculator import add, sub, mul, div
    a = 5
    b = 10
    print(f"{a} + b = {add(a, b)}")
    print(f"{a} - {b} = {sub(a, b)}")
    print(f"{a} * {b} = {mul(a, b)}")
    print(f"{a} / {b} = {div(a, b)}")
