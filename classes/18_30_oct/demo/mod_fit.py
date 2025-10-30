"""
File name: mod_fit.py
Author: Sasha D. Hafner
Course: Modelling 2025

Description:
    This module defines some functions for model fit statistics.

Usage:
    See the melt_demo.py file for examples.
"""

import numpy as np

def nse(obs, pred):
    """ 
    Nash-Sutcliffe model efficiency. 

    Parameters
    ----------
    obs : array
        Observed (measured) values of response variable for particular 
        times etc. 
    pred : array
        Model predictions for same response variable as `obs` for same
        times etc.

    Returns
    _______
    float 
        Value of Nash-Sutcliffe model efficiency. 
        
    """
    return 1 - np.sum((pred - obs)**2) / np.sum((obs - np.mean(obs))**2)

def rmse(obs, pred):
    """ 
    Root mean square error (often abbreviated RMSE). 

    Parameters
    ----------
    obs : array
        Observed (measured) values of response variable for particular 
        times etc. 
    pred : array
        Model predictions for same response variable as `obs` for same
        times etc.

    Returns
    _______
    float 
        Value of RMSE. 
    """
    return np.sqrt(np.mean((pred - obs)**2))

def mae(obs, pred):
    """ 
    Mean absolute error (often abbreviated MAE). 

    Parameters
    ----------
    obs : array
        Observed (measured) values of response variable for particular 
        times etc. 
    pred : array
        Model predictions for same response variable as `obs` for same
        times etc.

    Returns
    _______
    float 
        Value of MAE. 
    """
    return np.mean(np.abs(pred - obs))

def mbe(obs, pred):
    """ 
    Mean bias error (often abbreviated MBE).

    Parameters
    ----------
    obs : array
        Observed (measured) values of response variable for particular 
        times etc. 
    pred : array
        Model predictions for same response variable as `obs` for same
        times etc.

    Returns
    _______
    float 
        Value of MAE. 
    """
    return np.mean(pred - obs)
