# ICEL9-data-analysis-workshop

Welcome to the ICEL 2023 workshop in data analysis. 

In this workshop, we will showcase some examples of equine-kinematics analysis procedures using MATLAB and python. 
Hopefully, this will present you with some insights into how this can be done, with some useful code-snippets and 
an attempt to present these comprehensible.

> **Attention!**  
> Keep an eye on updates to this repository. The absolute final version of the code that will be used will be uploaded
> at the latest on the 31<sup>st</sup> of August 2023 by 12:00 CET. This means you can safely download the latest version 
> the night before the workshop.

## Requirements

For the actual workshop you will need the following,
1. Your own laptop.

2. The proper software installed. Either MATLAB or Python. Installation guides for [MATLAB](./matlab/installation.md) and 
[Python](./python/README.md) can be found in their respective folders in this repository.
3. Data sets downloaded. Here are the links for this.
4. Make sure the code in this repository is available and can be run on your laptop. If you are familiar with github
feel free to clone this repository. If you are unfamiliar with github you can download a zip file from this repos main 
page by clicking the green code button above to the right and then click 'Download ZIP' . Make sure you have selected 
the main branch, as seen above to the left of this page. Here is an image of what it should look like,
![image](./resources/download_clone_repo.png)

# Assignment
The assignment is divided in 3 parts, which you can find in each script. MATLAB scripts are in the matlab folder are have the ".mlx" extension. Python scripts are in the python folder and have the ".ipynb" extension.
During the workshop, we are going to go through the first part of the assignment, discuss each step and if we have enough time we will also look at parts 2 and 3. You are welcome to already look at them and try them out for yourself! 

## Part 1:
In part 1, we cover the basics such as loading a data file and plotting the different available signals. We will also look at how to process Motion Capture data and extract basic locomotion asymmetry parameters for one horse.

## Part 2: 
In part 2, we show you how to loop the analysis over several files, remove outliers values, and save the results in a csv file for further analysis.

## Part 3: 
In part 3, instead of looking at the data of one timepoint of all horses, we will compare the data of one horse over time. We will then discuss how to plot data to visualise evolution over time. 
