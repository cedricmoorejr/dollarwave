from .calculate import inflation_calculator
from .calculateGUI import InflationCalculatorApp

# Create the app object
GUI = InflationCalculatorApp(inflation_calculator)

__all__=['inflation_calculator', 'GUI']

