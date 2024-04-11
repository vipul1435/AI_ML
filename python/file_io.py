#Read and write data in files
# Syntex for read file

# file = open("file_name", "mode")

fi = open("demo.txt","r")
print(fi.read())

# Modes in file handling
# r = read, it will read the file
# r+ = read and write, it will read and write the file and it will not create a file if it does not exist -> reading pointer is at the start of the file
# w = write, it will overwrite the file i.e. it will delete the previous data
# w+ = write and read, it will write and read the file and it will create a file if it does not exist -> reading pointer is at the start of the file and it will overwrite the file i.e. it will delete the previous data
# a = append, it will add data in the end of the file
# x = create, it will create a file and open it for writing


#readline() method, it used to read the file line by line

# Note -> if we read any data from file, we cant read it again, we have to open the file again to read it again-> this is because the file pointer is at the end of the file

line = fi.readline()

#closing file
fi.close()


#delete the file
# to delete the file we have to import os module and use remove() method

import os

os.remove("demo.txt")

#write data in file
# to write data in file we have to open the file in write mode
