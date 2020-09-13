def input_func(fib_range):
  def wrap_function():
    print("Enter the a number to print Fibonacci series until that range.")
    a = int(input())
    fib_range(a)
  return wrap_function


@input_func
def Fibonacci(num):
    num1 = 0
    num2 = 1
    series = 0
    for i in range(num):
        print(series, end=' ')
        num1 = num2
        num2 = series
        series = num1 + num2

Fibonacci()
