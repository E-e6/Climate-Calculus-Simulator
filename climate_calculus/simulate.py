"""Climate calculus core simulation functions."""
import numpy as np
import pandas as pd

def co2_pathway(years, c0=420.0, r=0.0055, seasonal_amp=3.0):
    """Generate CO2 concentration pathway with seasonal cycle."""
    t = np.arange(len(years))
    co2 = c0 * np.exp(r * (years - years.min()))
    seasonal = seasonal_amp * np.sin(2 * np.pi * (t % 12) / 12)
    return co2 + seasonal

def climate_response(co2, lambda_ecs=3.0, c0=280.0):
    """Approximate temperature response from CO2 concentration."""
    forcing = 5.35 * np.log(co2 / c0)
    return lambda_ecs * forcing / 3.7

def sea_level_rise(temp, beta=2.1e-4, ocean_depth_m=3700.0, ice_coeff_cm_per_C=18.0):
    """Estimate sea level rise (cm)."""
    thermosteric = beta * ocean_depth_m * 100 * temp
    ice = ice_coeff_cm_per_C * temp
    return thermosteric + ice

def simulate(years, c0=420.0, r=0.0055, lambda_ecs=3.0,
             beta=2.1e-4, ocean_depth_m=3700.0,
             ice_coeff_cm_per_C=18.0, seasonal_amp=3.0):
    """Simulate climate variables for a given set of parameters."""
    co2 = co2_pathway(years, c0=c0, r=r, seasonal_amp=seasonal_amp)
    temp = climate_response(co2, lambda_ecs=lambda_ecs, c0=280.0)
    slr = sea_level_rise(temp, beta=beta, ocean_depth_m=ocean_depth_m,
                         ice_coeff_cm_per_C=ice_coeff_cm_per_C)
    return pd.DataFrame({"Year": years, "CO2": co2, "Temp": temp, "SLR": slr})

def monte_carlo(n, year_start, year_end, **kwargs):
    """Run Monte Carlo simulations by perturbing parameters."""
    rng = np.random.default_rng()
    r_vals = rng.normal(kwargs.get("r", 0.0055), 0.001, n)
    lambda_vals = rng.normal(kwargs.get("lambda_ecs", 3.0), 0.5, n)
    results = []
    for i in range(n):
        params = kwargs.copy()
        params.update({"r": float(r_vals[i]), "lambda_ecs": float(lambda_vals[i])})
        years = np.arange(year_start, year_end + 1)
        df = simulate(years=years, **params)
        df["Run"] = i
        results.append(df)
    return pd.concat(results, ignore_index=True)
