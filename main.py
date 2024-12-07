def mean_squared_error(actual, calculated):
  if len(actual) != len(calculated):
    raise ValueError("Actual and calculated lists must have the same length.")

  errors = [(a - c)**2 for a, c in zip(actual, calculated)]
  return sum(errors) / len(actual)

# Example usage:
actual = [2, 3, 5, 5, 9]
calculated = [3, 3, 8, 7, 6]

mse = mean_squared_error(actual, calculated)
print(f"Mean Squared Error: {mse}")

from sklearn.metrics import mean_squared_error

def calculate_mse(actual, calculated):
  """
  Calculates the Mean Squared Error (MSE) between two lists.

  Args:
    actual: A list of actual values.
    calculated: A list of calculated values.

  Returns:
    The Mean Squared Error.
  """
  return mean_squared_error(actual, calculated)

# Example usage:
actual = [2, 3, 5, 5, 9]
calculated = [3, 3, 8, 7, 6]

mse = calculate_mse(actual, calculated)
print(f"Mean Squared Error: {mse}")