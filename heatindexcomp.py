
#Column names and column indices to read

columns = {'date':0, 'time': 1, 'tempout':2, 'humout':5, 'heatindex':13}

# Data types for each column (only if non-string)

types = {'tempout': float, 'humout':float, 'heatindex':float}

#Initialize my data variable
data = {}
for column in columns:
    data[column] = []


# Initialize my data variable
#data = {'date':[], 'time':[], 'tempout':[]}
#time = data['time']


# Reading the data file
filename = "./data/wxobs20170821.txt"

with open(filename, "r") as datafile:
    # read first three line (header)
    for _ in range(3):
        #print(_)
        datafile.readline()
        
 
    # Read and parse the rest of the file
    for line in datafile:
        split_line = line.split()
        for column in columns:
            i = columns[column]
            t = types.get(column, str)
            value = t(split_line[i])
            data[column].append(value)


# compute the heatindex

def compute_heatindex(t, hum):
    a = -42.379
    b = 2.04901523
    c = 10.14333127
    d = -0.22475541
    e = -0.00683783
    f = -0.05481717
    g = 0.00122874
    h = 0.00085282
    i = -0.00000199    
    

    rh = hum/100

    hi = (a + (b*t) + (c * rh) + (d *t*rh) + (e * t ** 2)+
          (f * rh **2) + (g * t**2 * rh) + (h * t * rh **2)+
          (i * t**2 * rh **2))

    return hi
 


#print(data['tempout'])
#exit()

# running the function to computer windchill
heatindex = []
for temp, humout in zip(data['tempout'], data['humout']):
    heatindex.append(compute_heatindex(temp, humout))


# debug
#print(windchill)

# DEBUG
#for wc_data, wc_comp in zip(data['windchill'], windchill):
#    print(f'{wc_data:.5f} {wc_comp:.5f} {wc_data-wc_comp:.5f}')


# output comparision data
print('              ORIGINAL   COMPUTED')
print(' DATE   TIME  HEATINDEX  HEATINDEX DIFFERENCE')
print('------- ------ --------- --------- ----------')

zip_data = zip(data['date'], data['time'], data['heatindex'], heatindex)
for date, time, hi_orig, hi_comp in zip_data:
    hi_diff = hi_orig - hi_comp
    print(f'{date} {time:>6} {hi_orig:9.6f} {hi_comp:9.6f} {hi_diff:10.6f}')


             




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

