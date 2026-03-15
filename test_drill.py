"""
Module 2 — Drill 2: Learner Test File

Write your two pytest test functions below.
The autograder will run these as part of the CI check.
"""

import pandas as pd
import numpy as np
from drill_functions import clean_column, compute_revenue


def test_clean_column():
       
    s = pd.Series([1, np.nan, 3])
    result = clean_column(s)
    
           
    assert not result.isna().any()
    

    assert result[1] == 2


def test_compute_revenue():

    qty = pd.Series([2, 3, 4])
    price = pd.Series([10, 20, 30])
    
    
    result = compute_revenue(qty, price)
    
    
    expected = pd.Series([20, 60, 120])
    
    
    assert result.equals(expected)