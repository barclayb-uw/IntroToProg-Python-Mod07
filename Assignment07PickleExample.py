#---------------------------------------------------------------------
# Title: Assignment 7
# Desc: Script that shows examples of pickling and handling exceptions
# Changelog: (Who, Date, info)
# BBicksler, 11-30-2020, created file, added pickling example
#----------------------------------------------------------------------


# example of using pickle to save a dictionary

# Step 1 - import Pickle into your python code
import pickle

# Step 2 - create my dictionary

my_dict = {'Frank': 47, 'Jane': 35, 'Butch': 27, "Linda": 51}

# now I have 3 peoples names and ages.

# Specify a filename to write to and then open the file for binary writing

filename = 'people'

outfile = open(filename,'wb')

# then use pickle.dump() to write to the file

pickle.dump(my_dict,outfile)
outfile.close()

# Now I will open the file to verify the data was saved correctly

infile = open(filename,'rb')
new_dict = pickle.load(infile)
infile.close()

# I will print the new dictionary to validate the data

print(new_dict)
# I can also compare it to my other dictionary
print(new_dict==my_dict)
