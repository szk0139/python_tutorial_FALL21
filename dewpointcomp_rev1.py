from mysciW4.readdata import read_data
from mysciW4.printing import print_comparison
from mysciW4.computation import compute_dewpoint

#Column names and column indices to read

columns = {'date':0, 'time': 1, 'tempout':2, 'humout':5, 'dewpt':6}

# Data types for each column (only if non-string)

types = {'tempout': float, 'humout':float, 'dewpt':float}

data = read_data(columns, types = types)

dewpointtemp = [compute_dewpoint(t, h) for t, h in zip(data['tempout'], data['humout'])]

print_comparison('DEWPOINT', data['date'], data['time'], data['dewpt'], dewpointtemp)
             

