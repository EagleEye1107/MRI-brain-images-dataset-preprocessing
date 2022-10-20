# MRI-brain-images-dataset-preprocessing
The aim of this project, is to know how to improve the quality of MRI brain images by preprocessing them and prepare the dataset for Machine Learning &amp; Data Mining process.

![An example of an MRI Brain image](MRI_Brain_Image_Example.jpg)

# Preprocessing steps :
### 1. Standardize images by resizing them
- The idea here is to iterate all the images in our dataset using **os.listdir()**, this function returns the list of files and subdirectories present in the given directory.
- Than, for each each image read with **Image.open** function, we resize it using **resize** function of an **Image** object from **PIL** library
- We store all the resized images in **./resized** folder

### 2. Image equalization
### 3. Brain Tissue segmentation
### 4. Splitting dataset (trainset - testset) 

