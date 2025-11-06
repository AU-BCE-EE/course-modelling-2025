
Check rates code

The code:
```{python}
        # Calculate heat flow (W) through individual pathways
        # All are positive for heat flow in (this is arbitrary)
        Q_solar = a_top * q_sol                                     # Solar energy
        Q_top = a_top * u_top * (temp_air - temp_pool)              # Convection from top
        Q_sub = a_wall * u_wall * (temp_sub - temp_pool)            # Conduction to/from substrate (soil or whatever is there)
        Q_renew = cp * dens * flow_renew * (temp_pool - temp_renew) # Net energy coming in from renewal water
        
        # And sum them
        Q_net = Q_solar + Q_top + Q_renew + Q_sub

        # Express as temperature change
        dtemp_dt = Q_net / (cp * dens * vol)
```

Conceptual check of

1. Conservation
2. Constitutive equations

Conservation first.

During model formulation we came up with this energy conservation equation:

```
Rate of energy accumulation = solar + air/top + soil/substrate + renewal
```

All in W.

And the code has this:

```{python}
        Q_net = Q_solar + Q_top + Q_renew
```

OK?

Now for a conceptual check of the constitutive equations.

The code:
```{python}
        # Calculate heat flow (W) through individual pathways
        # All are positive for heat flow in (this is arbitrary)
        Q_solar = a_top * q_sol                                     # Solar energy
        Q_top = a_top * u_top * (temp_air - temp_pool)              # Convection from top
        Q_sub = a_wall * u_wall * (temp_sub - temp_pool)            # Conduction to/from substrate (soil or whatever is there)
        Q_renew = cp * dens * flow_renew * (temp_pool - temp_renew) # Net energy coming in from renewal water
```

The check
```{python}
        #         Area  * flux -> OK
        Q_solar = a_top * q_sol                                     # Solar energy

        #        Area *  CHTC * delta T -> OK
        Q_top = a_top * u_top * (temp_air - temp_pool)              # Convection from top
        #       Area  * ------flux------------------- -> OK
        Q_top = a_top * u_top * (temp_air - temp_pool)              # Convection from top
        #                         High    -  low ->    postitive -> heat transfer into pool -> OK
        Q_top = a_top * u_top * (temp_air - temp_pool)              # Convection from top
```


Unit check:
```{python}
        # All are positive for heat flow in (this is arbitrary)
# 1. Solar 
#                  m^2 *  W/m^2 -> W
        Q_solar = a_top * q_sol                                     # Solar energy


# 2. Air/top
#    u_top : float
#        Overall heat transfer coefficient from the upper water surface (W/m2-K)
#                 m^2  * W/m2-K * K ->  W
        Q_top = a_top * u_top * (temp_air - temp_pool)              # Convection from top

# 3.
#               Area   * CHTC   *     delta temperature --> OK
#                 m2      W/m2-K     K  ---> W
        Q_sub = a_wall * u_wall * (temp_sub - temp_pool)            # Conduction to/from substrate (soil or whatever is there)

# 4.
        Q_renew = cp * dens * flow_renew * (temp_pool - temp_renew) # Net energy coming in from renewal water
        
# 5.
        # And sum them
        Q_net = Q_solar + Q_top + Q_renew
```

Conceptual check.
```{python}
        # Express as temperature change
  # temp change = energy in / (dt/dH-M ... ) 
        dtemp_dt = Q_net / (cp * dens * vol)
  # Hmmm, maybe go to xopp file for this one!
        dtemp_dt = Q_net / (cp * dens * vol)
```

And unit check.
```{python}
        # Express as temperature change
        #          J/s   / K/J-kg * ...
        dtemp_dt = Q_net / (cp    * dens * vol)
```


