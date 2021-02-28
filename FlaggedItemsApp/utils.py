import numpy as np

def find_outliers(values):
    first_quartile = np.percentile(values, 25, interpolation = 'midpoint')
    third_quartile = np.percentile(values, 75, interpolation = 'midpoint')
    inter_quartile_range = third_quartile - first_quartile
    
    lower_limit = first_quartile - (1.5 * inter_quartile_range)
    upper_limit = third_quartile + (1.5 * inter_quartile_range)

    outliers = []
    for value in values: 
        if ((value> upper_limit) or (value<lower_limit)): 
            outliers.append(value)
    
    return outliers