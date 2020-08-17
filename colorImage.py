import cv2
import numpy

#'''The class colorImage is created and the cases are defined where the user inserts or not the path of the image'''

class colorImage:

    def __init__ (self, route = None): #Initialization
      if route is None: # When the user does not enter the path of the image, it is inserted by default
          self.route = 'C:/Users/aleja/OneDrive/Documentos/GitHub/colorImage.AAC/lena.png' #The file is loaded
      else:
          self.route =route
      self.image = cv2.imread(self.route) #Saved image

    #'''For view the image properties'''

    def displayProperties(self):
        height, wide, comp = self.image.shape #Save the imagen data: height, wide and components
        print('Heigh and Wide of the photo', height, 'x', wide, '.') #Print the image data: height and wide

#'''For view the image in grayscale '''

    def makeGray(self):
        grayscale = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) #Converting the image to gray scale using BGRGRAY code
        cv2.imshow('Gray Image', grayscale) #Shoe the image in gray scale
        cv2.waitKey(0)

#'''For get at colorized image'''

    def colorizeRGB(self, comp= None):

        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) #Converting the image to gray scale using BGRGRAY code again

        # the code leaves the red color for default when the user doesn't enter the color
        if comp is None:
            self.comp = 'red_color'
        else:
            self.comp = comp

        #For show the red component of the image the code creates a copy of the image in red and them makes zeroes the other components
        if self.comp == 'red_color':
            image_in_red = numpy.copy(self.image)
            image_in_red[:, :, 0] = 0
            image_in_red[:, :, 1] = 0
            cv2.imshow('Image: Red Component', image_in_red)
            cv2.waitKey(0)

        #For show the green component of the image the code creates a copy of the image in green and them makes zeroes the other components
        elif self.comp == 'green_color':
            image_in_green = numpy.copy(self.image)
            image_in_green[:, :, 0] = 0
            image_in_green[:, :, 2] = 0
            cv2.imshow('Image: Green Component', image_in_green)

        #For show the blue component of the image the code creates a copy of the image in blue and them makes zeroes the other components          cv2.waitKey(0)
        elif self.comp == 'blue_color':
            image_in_blue = numpy.copy(self.image)
            image_in_blue[:, :, 1] = 0
            image_in_blue[:, :, 2] = 0
            cv2.imshow('Image: Blue Component', image_in_blue)
            cv2.waitKey(0)
        else:
            print('None of the entered values is valid')

   #For highlight the tones in the image (HUE)
    def makeHue(self):
        HSV_function = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV) #Using cv2.COLOR_BGR2HSV code the image is converted from BGR to HSV
        HSV_function[:, :, 1] = 255  # S component to 255
        HSV_function[:, :, 2] = 255  # V component to 255
        hue_image = cv2.cvtColor(HSV_function, cv2.COLOR_HSV2BGR)
        cv2.imshow('HUE_image', hue_image)
        cv2.waitKey(0)