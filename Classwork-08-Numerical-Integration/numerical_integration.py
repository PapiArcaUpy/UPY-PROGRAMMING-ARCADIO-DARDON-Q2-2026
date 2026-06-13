import math

# INPUT

left_endpoint = input("Write the left endpoint of the interval: ")
right_endpoint = input("Write the right endpoint of the interval: ")
function_expression = input("Write the function to integrate: ")
method = input("Write the integration method (LRM/RRM/MRM/TRAP): ").upper()

# PROCESS

if "pi" in left_endpoint:
left_endpoint = eval(left_endpoint.replace("pi", str(math.pi)))
else:
left_endpoint = float(left_endpoint)

if "pi" in right_endpoint:
right_endpoint = eval(right_endpoint.replace("pi", str(math.pi)))
else:
right_endpoint = float(right_endpoint)

n = 1000
step_size = (right_endpoint - left_endpoint) / n
integral = 0.0

if method == "LRM":

```
for i in range(n):
    x = left_endpoint + i * step_size
    fx = eval(function_expression.replace("x", str(x)))
    integral += fx * step_size
```

elif method == "RRM":

```
for i in range(1, n + 1):
    x = left_endpoint + i * step_size
    fx = eval(function_expression.replace("x", str(x)))
    integral += fx * step_size
```

elif method == "MRM":

```
for i in range(n):
    midpoint = left_endpoint + i * step_size + step_size / 2
    fx = eval(function_expression.replace("x", str(midpoint)))
    integral += fx * step_size
```

elif method == "TRAP":

```
left_value = eval(function_expression.replace("x", str(left_endpoint)))
right_value = eval(function_expression.replace("x", str(right_endpoint)))

integral = (left_value + right_value) / 2

for i in range(1, n):
    x = left_endpoint + i * step_size
    fx = eval(function_expression.replace("x", str(x)))
    integral += fx

integral *= step_size
```

else:
print("Invalid method selected.")
exit()

# OUTPUT

print(f"The approximate integral of {function_expression} is {integral}")
