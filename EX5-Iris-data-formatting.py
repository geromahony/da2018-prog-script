# Ger O'Mahony

# Exercise 5 Requirements:
#
# Write a Python script that reads the Iris data set in 
# and prints the four numerical values on each row in a nice format. 
# That is, on the screen should be printed the petal length, 
# petal width, sepal length and sepal width, and these values should 
# have the decimal places aligned, with a space between the columns.

# read file in IrisData folder which is relative to this
# file in repo (./)
with open('./IrisData/iris.data.txt', 'r') as data_in:
    # Print a header to show which column is which
    print('|      Petal     |      Sepal     |')
    print('| Length | Width | Length | Width |')
    # Loop over each line in the data
    for line in data_in:
        # Remove the '/n' newline special character
        # before splitting
        raw_line = line.strip()

        # Split data by comma
        raw_line = raw_line.split(',')

        # Print data using format descriptors.
        # Data is read as a string already so just format that by aligning..
        print('{:<3} {:<3} {:<3} {:<3}'.format(raw_line[0], raw_line[1], raw_line[2], raw_line[3]))

