def binary_to_decimal(binary):
  """Converts a binary string to a decimal integer."""
  decimal = int(binary, 2)
  return decimal


binary_number = "101101"
decimal_number = binary_to_decimal(binary_number)
print(f"The decimal equivalent of {binary_number} is {decimal_number}") 