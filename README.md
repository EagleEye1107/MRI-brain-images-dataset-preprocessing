# MRI-brain-images-dataset-preprocessing
Magnetic Resonance Imaging (MRI) of the brain is one of the most prevalent image acquisitions performed in the diagnostic centers and hospitals. The acquisition of a brain MRI scan is noninvasive and nondestructive. It involves yielding an arbitrary cross‐section of the brain without radiation exposure.

Brain MRIs demonstrate superior soft‐tissue contrast, high spatial resolution, and reveal the detailed anatomical structures of brains.

The aim of this project, is to know how to improve the quality of MRI brain images by preprocessing them and prepare the dataset for Machine Learning &amp; Data Mining process.

![An example of an MRI Brain image](MRI_Brain_Image_Example.jpg)

# Preprocessing steps

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 1. Standardize images by resizing them
- The idea here is to iterate all the images in our dataset using **os.listdir()**, this function returns the list of files and subdirectories present in the given directory.
- Than, for each each image read with **Image.open** function, we resize it using **resize** function of an **Image** object from **PIL** library
- We store all the resized images in **./resized** folder

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 2. Brain Tissue segmentation [[Paper link]](https://www.researchgate.net/publication/339708961_Conventional_and_Deep_Learning_Methods_for_Skull_Stripping_in_Brain_MRI)
- The inclusion of non‐brain tissue parts in brain region like (skull, dura mater,etc.) can lead to incorrect decision making
- Thus, brain segmentation, also recognized as brain extraction or skull stripping is a critical step for a neuroimaging diagnostic system
- Now let's talk a little bit about **Image Segmentation**
  #### 2.1. Image Segmentation [[medium article]](https://towardsdatascience.com/image-segmentation-using-pythons-scikit-image-module-533a61ecc980)
  - Image Segmentation is essentially the process of partitioning a digital image into multiple segments to simplify and/or change the representation of an image into something that is more meaningful and easier to analyze.
  - There are two approches for image segmentation
  - The first one is the **Supervised Segmentation**, where some prior knowledge, possibly from human input, is used to guide the algorithm.
  - The second approch is the **Unsupervised Segmentation**, where no prior knowledge is required. These algorithms attempt to subdivide images into meaningful regions automatically. The user may still be able to tweak certain settings to obtain desired outputs.
  
  ![image segmentation](image_seg.png)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 3. Image equalization [[Paper link]](https://arxiv.org/ftp/arxiv/papers/2003/2003.06615.pdf)
- Using **RMSHE : Recursive Mean Separated Histogram Equalization**

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 4. Splitting dataset (trainset - testset) 

