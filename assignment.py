#first importing libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

#function for resizing image
def resize(img):
    return cv2.resize(img,(200,200))

#function for creating array
def create_array(length):
    return np.zeros((length,200,200,3))

#function for length of array
def length_of_array(files):
    return len(files)
    
#variable for image directory
img_dir='C:/Users/abdul wahab/Desktop/piaic 2nd sem/photos/'

#main function
def main():
    #check if path exists
    if os.path.exists(img_dir):
        #getting number of file in image directory
        for (root,dirs,files) in os.walk(img_dir, topdown=True): 
            pass
        
        no_of_file=length_of_array(files)
        images=create_array(no_of_file)
        
        #looping through each file
        for i in range(len(files)):
            img=plt.imread(img_dir+files[i])
            img=resize(img)
            images[i]=img
            plt.figure()
            plt.imshow(images[i].astype(np.uint8))
    else:
        print('path is wrong')
if __name__=="__main__":
    main()
   
