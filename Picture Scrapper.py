# import needed libraries
import os  # used to find files in a folder
import numpy as np
import matplotlib.pylab as plt  # shows image

# initialization
folder = "photos/"  # directory in which pictures are

# working
# loading all the files
allfiles = [f
            for f in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, f))]  # loads all the file names in the folder
nparray = np.zeros((len(allfiles), 300, 300, 4))

print("Reading :", len(allfiles), "files")  # tells how much files are there

for i in range(len(allfiles)):  # loads all the files into a list
    #  print("Loading :", allfiles[i])
    nparray[i] = plt.imread(folder + allfiles[i])[:300, :300, :]  # clips and stores into an nparray

#  print(nparray)  # prints all the arrays

np.save("npfile", nparray)  # saving into a file for later use

plt.imshow(nparray[1])  # shows one of the pictures
plt.show()  # opens a window to show image
