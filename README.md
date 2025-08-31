# Climate Calculus Simulator

A lightweight command-line climate simulator for CO2, temperature, and sea level rise.

## Installation
```bash
cd climate_calculus_fixed
pip install -e .
```

## Usage
Run a single simulation:
```bash
python -m climate_calculus.cli --years 2020 2100
```

Run with uncertainty (Monte Carlo 50 runs):
```bash
python -m climate_calculus.cli --years 2020 2100 --uncertainty 50
```

Outputs are saved as `climate_output.csv`.
