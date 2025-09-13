# Black-Scholes Codes

This folder contains two main scripts illustrating the evolution of a commodity price (here, pork) within a simplified Black-Scholes framework.  

---

## 1. `black_scholes_simulation.py`

### Purpose  
Simulates multiple possible trajectories of pork prices based on real data, estimates the bank’s cost (European call option), and generates an animation of the evolutions.  

### 🛠Main steps  
- **Data extraction**: import of historical prices from a CSV file.  
- **Extrapolation**: generation of future trajectories using a normal distribution (parameters: mean, standard deviation, number of simulations).  
- **Bank cost calculation**: estimate of the option value by comparing the final price with the strike price `K`.  
- **Visualization**: animation of simulated trajectories with matplotlib, saved as a `.gif`.  

### Output  
- Console print of the **average bank cost**.  
- Animated plot of price evolutions:  
  - **Red** trajectories if the final price exceeds `K`.  
  - **Green** trajectories otherwise.  

---

## 2. `calcul_alpha.py`

### Purpose  
Illustrates volatility and price evolution using a simple daily random step of ±α.  

### Main steps  
- **Data extraction**: import of historical prices from a CSV file.  
- **Simple extrapolation**: generation of future prices by adding `+α` or `-α` each day.  
- **Visualization**: single plot combining historical and simulated prices, on a black background with custom formatting.  

### Output  
- Single graph showing both real data and extrapolated values according to a fixed volatility (e.g., ±1.8 USD).  

---

## Summary

- **`black_scholes_simulation.py`** → stochastic multi-trajectory simulation + bank cost estimation + animation.  
- **`calcul_alpha.py`** → simple ±α step simulation + single static plot.  
