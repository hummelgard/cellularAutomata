#!/usr/bin/python
version = 0.91

import numpy as np
import time
from PIL import Image
from PIL import ImageOps

RATIO = 1                          # given in percent.
SIZE = 500                         # Size/side of matrix.
RUNS = 100                         # Number of iterations in machine.
ALGORITHM = 'ink'                  # What type of algorithm to use XOR4, 
                                   # XOR8, INK, etc.
FILE_PATH = './data5/'             # Were to save everything.
MATRIX_TXT_FILE = ''               # If given, this matrix is loaded.
MATRIX_IMAGE_FILE = ''#'matrix.png'# Same, but loads a image data file instead.


def load_txt_matrix(fileName):
    """Load a matrix from a text file, this is the same format as the ones
        being saved during iterations."""
    # Loads a txt-matrix that looks like this
    #
    #  0 0 1 0
    #  0 1 1 1
    #  1 1 0 0
    #
    file = open(fileName,'r')
    matrix = np.array([map(int,line.split()) for line in file], dtype=np.bool)    
    width = matrix.shape[0]
    height = matrix.shape[1]    
    return matrix


def load_image_matrix(fileName):
    """Load an image file and black-white pixels is converted to a matrix."""
    image = Image.open(fileName)
    width = image.size[0]
    height = image.size[1]
    # Create an array of equal size as the image.
    matrix = np.array(ImageOps.invert(image), dtype=np.bool)
    return matrix    

class QuadTree:
    def __init__(self,matrix):
        self.matrixWidth = matrix.shape[0]
        self.matrixHeight = matrix.shape[1]
    
        self.matrixDeep = np.log2(min(matrix.shape[0],matrix.shape[1]))
    
    
    
class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    description = "This shape has not been described yet"
    author = "Nobody has claimed to make this shape yet"
    def area(self):
        return self.x * self.y
    def perimeter(self):
        return 2 * self.x + 2 * self.y
    def describe(self,text):
        self.description = text
    def authorName(self,text):
        self.author = text
    def scaleSize(self,scale):
        self.x = self.x * scale
        self.y = self.y * scale


s=Shape(100,45)

np.random.seed(1)
    
# Create a 2d array of random bools, with a ratio defined by RATIO and SIZE.
matrix = np.array(np.floor(np.random.sample(size=(SIZE,SIZE))+RATIO/100.0),
                  dtype=bool)
    
tstart = time.time()
for i in range(RUNS):
    print i
    fileStr='data%d.txt' %(i)
    fileData = open(FILE_PATH + fileStr,'w')
    matrix=np.roll(matrix,1, axis=0)^np.roll(matrix,-1, axis=0)^
                   np.roll(matrix,1, axis=1)^np.roll(matrix,-1, axis=1)
    for y in range(SIZE):
        for x in range(SIZE):
            fileData.write('%d ' % (matrix[x][y]))
        fileData.write('\n')
    fileData.close()
print (time.time()-tstart)/RUNS