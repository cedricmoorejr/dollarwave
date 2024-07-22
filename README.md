<p align="center">
  <img src="https://raw.githubusercontent.com/cedricmoorejr/dollarwave/main/dollarwave/assets/py_dollarwave_logo.png" alt="dollarwave Logo" width="700"/>
</p>

### Dollarwave Library: Inflation Adjustment Using CPI Data

The `dollarwave` module is a comprehensive library designed for adjusting the value of money across different years using Consumer Price Index (CPI) data. It offers extensive capabilities to handle and process CPI data, ensuring accurate inflation adjustments.

#### Table of Contents
1. [Why dollarwave?](#why-dollarwave)
2. [Key Features](#key-features)
3. [Usage Examples](#usage-examples)
    - [Calculating Inflation-Adjusted Values](#calculating-inflation-adjusted-values)
    - [Using the GUI](#using-the-gui)
4. [Installation](#installation)
5. [Contributing](#contributing)
6. [License](#license)

#### Why dollarwave?

- **Accurate Inflation Adjustments**: Utilizes CPI data to calculate the equivalent value of money across different years.
- **Easy to Use**: Provides a straightforward API for calculating inflation-adjusted values.
- **Data Validation**: Ensures the accuracy and consistency of CPI data used in calculations.

#### Key Features

1. **Inflation Adjustment Calculation**:
   - Calculates the equivalent value of an amount of money in different years using CPI data.
   - Automatically switches to yearly averages if monthly data is not available for the most recent comparison year.

2. **Data Handling and Validation**:
   - Validates CPI data to ensure it meets the required criteria.
   - Converts and processes CPI data for easy manipulation and calculation.

3. **Graphical User Interface (GUI)**:
   - User-friendly interface for performing inflation calculations without writing code.

## Usage Examples

### Calculating Inflation-Adjusted Values

Use the `inflation_calculator` to calculate the equivalent value of money across different years:

```python
from dollarwave import inflation_calculator

# Calculate the adjusted value
original_amount = 1
original_year = 1970
target_year = 2024
adjusted_amount = inflation_calculator(original_amount, original_year, target_year)
```
Output:
```
$1 from 1970 is equivalent to $8.04 in 2024 dollars.
8.044961340206186
```

### Using the GUI

You can also use the graphical user interface (GUI) to perform inflation calculations:

```python
from dollarwave import GUI

# Run the GUI
GUI.run()
```

From the GUI, you can:
- Calculate the inflation-adjusted value of an amount from the original year to the target year using CPI data.
- Calculate the historical value change of a given dollar amount over the past n years compared to the current month's CPI.
- Calculate the value of a given amount against the CPI values for each month of the current year where data is available.

#### GUI Screenshots

Here are some screenshots of the GUI in action:

- **Adjusted Value Tab**

![Adjusted Value Tab](https://github.com/cedricmoorejr/dollarwave/blob/v2.0.2/dollarwave/assets/adjusted_value_gui_img.png)

- **Current Year Change Tab**

![Current Year Change Tab](https://github.com/cedricmoorejr/dollarwave/blob/v2.0.2/dollarwave/assets/current_year_change_gui_img.png)

- **Comparison Tab**

![Comparison Tab](https://github.com/cedricmoorejr/dollarwave/blob/v2.0.2/dollarwave/assets/current_year_change_gui_img.png)

Alternatively, you can use the `inflation_calculator` instance directly:

```python
from dollarwave import inflation_calculator

# Calculate the current year change
print(inflation_calculator.current_year_change(amount=5))
```
Output:
```
{'January': 4.94, 'February': 4.97, 'March': 5.0, 'April': 5.02, 'May': 5.03, 'June': 5.03}
```

```python
# Calculate historical comparison
print(inflation_calculator.comparison(amount=10, n_years=3, plot=False))
```
Output:
```
$10 from 2021 is equivalent to $8.68 in 2024 dollars.
$10 from 2022 is equivalent to $9.38 in 2024 dollars.
$10 from 2023 is equivalent to $9.76 in 2024 dollars.
{2021: 8.68, 2022: 9.38, 2023: 9.76}
```

```python
# Calculate adjusted value
adjusted_amount = inflation_calculator.adjusted_value(amount=13, original_year=1991, target_year=2021)
print(f"${13} from {1991} is equivalent to ${adjusted_amount:.2f} in {2021} dollars.")
```
Output:
```
$13 from 1991 is equivalent to $25.86 in 2021 dollars.
25.86
```

## Installation

To install the `dollarwave` library, use pip:

```bash
pip install dollarwave
```

## Contributing

Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

