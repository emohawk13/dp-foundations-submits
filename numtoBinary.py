def func_a(num):
  if num % 2 == 0:
    return num - 1
  return num + 2

print(func_a(func_a(func_a(10))))