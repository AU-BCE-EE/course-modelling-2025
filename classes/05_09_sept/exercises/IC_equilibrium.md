# Equilibrium of inorganic carbon in pure water

Carbon dioxide ($\text{CO}_2$) dissolves in water and then is hydrated to form carbonic acid ($\text{H}_2 \text{CO}3$), which can give up two hydrogen ions or protons ($\text{H}^+$).

$$
\text{CO}_2\ (aq) + \text{H}_2\text{O} \leftrightharpoons\ \text{H}_2\text{CO}_3
$$

Dissolved carbon dioxide is often grouped with carbonic acid and called $\text{H}_2\text{CO}_3^*$.
We will follow that convention here.
The lumped species gives up one,

$$
\text{H}_2\text{CO}_3^* \leftrightharpoons\ \text{HCO}_3^- + \text{H}^+
$$

and then a second proton.

$$
\text{HCO}_3^- \leftrightharpoons\ \text{CO}_3^{-2} + \text{H}^+
$$

A. Can you develop a simple equilibrium model with pencil and paper to predict the pH of otherwise pure water in equilibrium with atmospheric $\text{CO}_2$?
See below for some constants.
The first is Henry's law constant for the lumped species.

| Parameter   | Value                                |
|-----        |-----                                 |
|$\text{K}_\text{H}$ | $10^{-1.5}$ $\text{mol}$ $\text{kg}^{-1}$ $\text{atm}^{-1}$ |
|$\text{K}_1$ | $10^{-6.3}$                          |
|$\text{K}_2$ | $10^{-10.3}$                         |


B. The concentration of $\text{CO}_2$ has increased from below 300 $\text{ppm}_v$ before the industrial revolution to above 400 $\text{ppm}_v$ presently. 
Using Python, create a plot of equilibrium pH vs. $\text{CO}_2$ mixing ratio.

