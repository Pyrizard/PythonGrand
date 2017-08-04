import os
import image_slicer
#Dont forget to download this using         pip install image_slicer


#This is to show that your cwd which could be different
print(os.getcwd())


#Change your directory to where the original image is store
os.chdir("C:/Users/Admin/Desktop")

#Here mention the file name with extension and the no. of splits
image_slicer.slice('Bird.png',5)


#Check the name of output files. The names would be in Matix pattern
