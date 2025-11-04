# Parameter values

Selection of appropriate parameter values for validation or application of a model is not always simple.
In some cases they can be determined from theory, but often measurements are needed.
The information presented below includes some approximate estimates for some common parameters for simple systems and approaches for making estimates for other systems.

## Typical numeric values

|Parameter                    | Typical symbol  | Conditions                  | Units                                       |  Value               | Source                       |
|------                       |-------          |-------                      |-------                                      |-------               | -------                      | 
|Diffusivity                  | $D$             | $\text{O}_2$ in water       |  $\text{m}^2 ~ \text{s}^{-1}$               | $2.1 \cdot 10^{-9}$  | Cussler (2009)               |
|Diffusivity                  | $D$             | $\text{NaCl}$ in water      |  $\text{m}^2 ~ \text{s}^{-1}$               | $1.6 \cdot 10^{-9}$  | Cussler (2009)               |
|Diffusivity                  | $D$             | $\text{CO}_2$ in air        |  $\text{m}^2 ~ \text{s}^{-1}$               | $1.4 \cdot 10^{-5}$  | Cussler (2009)               |
|Mass transfer coefficient    | $k_c$           | Air blowing over flat plate |  $\text{m} ~ \text{s}^{-1}$                 | $0.001 - 0.01$       | Calculated from correlations |
|Heat transfer coefficient    | $h$             | Gases, free and forced      |  $\text{W} ~ \text{m}^{-2} ~ \text{K}^{-1}$ |  $2 - 250$           | Incropera (2003)             |
|Heat transfer coefficient    | $h$             | Liquids, free and forced    |  $\text{W} ~ \text{m}^{-2} ~ \text{K}^{-1}$ |  $50 - 20,000$       | Incropera (2003)             |
|Heat transfer coefficient    | $h$             | With a phase change         |  $\text{W} ~ \text{m}^{-2} ~ \text{K}^{-1}$ |  $2,500 - 100,000$   | Incropera (2003)             |

## Mass transfer coefficients and diffusivity

If the primary resistance to mass transfer is through a thin film, diffusivity and the film thickness can be combined to estimate a mass transfer coefficient.
The film may be real (e.g., a plastic membrane) or hypothesized (e.g., the stagnant fluid films at interfaces between phases).
The appropriate equation can be derived from Fick's law under steady-state conditions, 

$$$
k_c = \frac{D}{L},
$$$

where $L$ is the film thickness (length, typically m), and $D$ is diffusivity (typically $\text{m}^2 ~ \text{s}^{-1}$).

Film thickness is usually calculated based on measurements of mass transfer, but once determined, can be instead used by modelers like us.
For designated liquid mass transfer systems, values are usually around $1 \cdot 10^{-4}$ m (Cussler, 2009).
For ponds, lakes, or oceans, effective values of the film thickness can be multiple mm, so up to, say, $5 \cdot 10^{-3}$ m.

## Reaction rates

First-order reaction constants can be estimated given some knowledge (or a guess) about how fast a reaction proceeds.
For a rough estimate, the relative rate of reaction can be taken directly as the rate constant.
So, for example, if some reactant disappears at a rate of 3.5% per hour, the rate constant is around 0.035 $\text{hr}^{-1}$.
This approach fails if the measured change is large, e.g., 50% over some period.
Instead, use the exact analytical approach:

$$$
k = - \frac{ln(\text{relative change})}{\Delta t}.
$$$


