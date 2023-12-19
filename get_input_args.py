#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER:  Yashi Gupta
# DATE CREATED: 15/12/2023                         
# REVISED DATE: 19/12/2023
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse

# Define get_input_args function
def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to create and define these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    """
    # Create Parse using ArgumentParser
    parser = argparse.ArgumentParser()

    # Create 3 command line arguments using add_argument() from ArgumentParser method
    parser.add_argument('--dir', type=str, default='pet_images/', 
                        help='path to folder of images')
    # TODO: 1a. EDIT parse.add_argument statements BELOW to add type & help for:
    #          --arch - the CNN model architecture
    #          --dogfile - text file of names of dog breeds
    parser.add_argument('--arch', default = 'vgg' )
    parser.add_argument('--dogfile', default = 'dognames.txt' )
    # Return parsed argument collection created with this function
    return parser.parse_args()


