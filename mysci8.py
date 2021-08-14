
# Initialize my data variable
data = {'date':[], 'time':[], 'tempout':[]}
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
        data['date'].append(split_line[0])
        data['time'].append(split_line[1])
        data['tempout'].append(float(split_line[2]))


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

