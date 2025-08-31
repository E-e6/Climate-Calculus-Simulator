import streamlit as st
import pandas as pd
from climate_calculus.simulate import monte_carlo

st.title("Climate Calculus Simulator")

# User input
uncertainty = st.slider("Uncertainty (%)", 0, 100, 50)

# Run simulation
df = monte_carlo(n=200, year_start=2020, year_end=2024, c0=420, r=0.0055, lambda_ecs=3.0, beta=2.1e-4, ocean_depth_m=3700.0, ice_coeff_cm_per_C=18.0, seasonal_amp=uncertainty)

st.subheader("Simulation Results")
st.dataframe(df)

st.download_button(
    label="Download CSV",
    data=df.to_csv(index=False),
    file_name="climate_output.csv",
    mime="text/csv"
)