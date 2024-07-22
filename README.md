<p align="center">
  <img src="https://raw.githubusercontent.com/cedricmoorejr/dollarwave/main/dollarwave/assets/py_dollarwave_logo.png" alt="dollarwave Logo" width="700"/>
</p>

### dollarwave Library: Inflation Adjustment Using CPI Data

The `dollarwave` module is a comprehensive library designed for adjusting the value of money across different years using Consumer Price Index (CPI) data. It offers extensive capabilities to handle and process CPI data, ensuring accurate inflation adjustments.

#### Table of Contents
1. [Why dollarwave?](#why-dollarwave)
2. [Key Features](#key-features)
3. [Usage Examples](#usage-examples)
    - [Calculating Inflation-Adjusted Values](#calculating-inflation-adjusted-values)
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

## Usage Examples

### Calculating Inflation-Adjusted Values

Use the `InflationCalculator` to calculate the equivalent value of money across different years:

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

## Installation

To install the `dollarwave` library, use pip:

```bash
pip install dollarwave
```

## Contributing

Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


