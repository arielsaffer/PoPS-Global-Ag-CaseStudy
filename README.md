# Data Exploration for PoPS Global 
... to apply to agricultural pest/pathogen case studies

Points to explore:

- Temporally variable agricultural host map
- Traded commodities as agricultural inputs (vs. human consumption)
- Asynchrony of entry and establishment
- Annual vs. monthly model run 
- Assess viability of candidate case studies

## Notebooks

 - **MonthlyCropHost**: methods to incorporate a "crop calendar" and EarthStat data layers to allow for spatially variable host presence 
 - **AnnualExploration**: assess how running PoPS Global on annual vs. monthly time steps affects the selection and calibration of the *lamda* and *alpha* parameters, using simulated data.
 - **FaoData**: calculate portion of crop/crop group using FAO data and classifications - as data for host percent area or *lamda weight*
 - **StatisticalModel**: exploratory data anlysis using simplified model inputs to aid in pathway, driver, and case study selection 