"""Command line interface for climate calculus simulator."""
import argparse
import numpy as np
from .simulate import simulate, monte_carlo

def main():
    parser = argparse.ArgumentParser(description="Climate Calculus Simulator")
    parser.add_argument("--years", type=int, nargs=2, default=[2020, 2100],
                        help="Start and end year, e.g. --years 2020 2100")
    parser.add_argument("--uncertainty", type=int, default=0,
                        help="Number of Monte Carlo runs (0 = single run)")
    parser.add_argument("--c0", type=float, default=420.0,
                        help="Initial CO2 concentration (ppm)")
    parser.add_argument("--seasonal-amp", type=float, default=3.0,
                        help="Seasonal CO2 amplitude (ppm)")
    args = parser.parse_args()

    years = np.arange(args.years[0], args.years[1] + 1)

    if args.uncertainty > 0:
        env = monte_carlo(n=args.uncertainty, year_start=years.min(),
                          year_end=years.max(), c0=args.c0, seasonal_amp=args.seasonal_amp)
    else:
        env = simulate(years, c0=args.c0, seasonal_amp=args.seasonal_amp)

    print(env.head())
    out_file = "climate_output.csv"
    env.to_csv(out_file, index=False)
    print(f"Results saved to {out_file}")

if __name__ == "__main__":
    main()
