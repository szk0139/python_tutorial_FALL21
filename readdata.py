

def read_data(columns, types = {}, filename= "data/wxobs20170821.txt"):
    """
    Read data from CU Boulder Weather Stattion data file

    Parameters:
        colums: A dictonary of column names mapping to column indices
        types: A dictonary of column names mapping to the types to which to convert each column of data
        filename: A string path pointing to the CU Boulder Wather Station data file


    """
    #Initialize my data variable
    data = {}
    for column in columns:
        data[column] = []

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

    return data


