# python script name without .py extension and then the function name

from readdata import read_data

#Column names and column indices to read

columns = {'date':0, 'time': 1, 'tempout':2, 'windspeed':7, 'windchill':12}

# Data types for each column (only if non-string)

types = {'tempout': float, 'windspeed':float, 'windchill':float}

# Read data from file

data = read_data(columns, types=types)


# compute the wind chill temperature

def compute_windchill(t, v):
    a = 35.74
    b = 0.6215
    c = 35.75
    d = 0.4275
    
    v16 = v ** 0.16
    wci = a + (b*t)-(c*v16)+(d*t*v16)
    return wci



#print(data['tempout'])
#exit()

# running the function to computer windchill
windchill = []
for temp, windspeed in zip(data['tempout'], data['windspeed']):
    windchill.append(compute_windchill(temp, windspeed))


# debug
#print(windchill)

# DEBUG
#for wc_data, wc_comp in zip(data['windchill'], windchill):
#    print(f'{wc_data:.5f} {wc_comp:.5f} {wc_data-wc_comp:.5f}')


# output comparision data
print('              ORIGINAL   COMPUTED')
print(' DATE   TIME  WINDCHILL  WINDCHILL DIFFERENCE')
print('------- ------ --------- --------- ----------')

zip_data = zip(data['date'], data['time'], data['windchill'], windchill)
for date, time, wc_orig, wc_comp in zip_data:
    wc_diff = wc_orig - wc_comp
    print(f'{date} {time:>6} {wc_orig:9.6f} {wc_comp:9.6f} {wc_diff:10.6f}')


             




# DEBUG
#for i, j in zip([1, 2], [3, 4, 5]):
#    print(i, j) 


 

# DEBUG
#print(data['tempout'])




#DBUG
#for datum in data:
#    print(datum)
#print(data[0])
#print(data[9])
#print(data[-1])
#print(data[0:10])
#for datum in data[0:10]:
#    print(datum)
#for datum in data[:10:2]:
#    print(datum)
#print(data[8][4])
#print(data[8][4][0])
#print(data[8][:5])
#print(data[8][:5:2])
#print(data[5:8][0])
#print(data[5])

