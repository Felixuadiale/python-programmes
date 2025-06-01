import math

def calculate_lcm(numbers):
  """Calculates the least common multiple (LCM) of a list of numbers.

  Args:
    numbers: A list of numbers.

  Returns:
    The LCM of the numbers in the list.
  """

  if not numbers:
    return 0  

  result = numbers[0]
  for num in numbers[1:]:
    result = (result * num) // math.gcd(result, num)
  return result


numbers = [12,4]
lcm_result = calculate_lcm(numbers)
print(f"The LCM of {numbers} is: {lcm_result}")