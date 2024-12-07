# Mean Squared Error (MSE) Calculation

This file demonstrates two ways to calculate the Mean Squared Error (MSE) between two lists of values:

1. **Manual Calculation:** 
   - The `mean_squared_error` function calculates the MSE directly by:
     - Checking for equal lengths of input lists.
     - Calculating the squared difference between corresponding values.
     - Summing the squared errors.
     - Dividing the sum of squared errors by the number of data points.

2. **Using scikit-learn:**
   - The `calculate_mse` function leverages the `mean_squared_error` function from the scikit-learn library for efficient and concise MSE calculation.

## Example Usage

Both functions can be used as follows:

```python
actual = [2, 3, 5, 5, 9]
calculated = [3, 3, 8, 7, 6]

# Manual Calculation
mse_manual = mean_squared_error(actual, calculated) 
print(f"Mean Squared Error (Manual): {mse_manual}")

# Using scikit-learn
mse_sklearn = calculate_mse(actual, calculated)
print(f"Mean Squared Error (scikit-learn): {mse_sklearn}")
