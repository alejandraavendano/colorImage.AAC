#Pontificia Universidad Javeriana
#Procesamiento de imagenes y visión
#Alejandra Isabel Avendaño Cortina



#'''main'''

#First, the script is created so that the user can view the image properties

from colorImage import * #The system import the class "colorImage"

if __name__ == '__main__':
    print('Editing an Image') #Print the first string for start the code
    path_file = 'C:/Users/aleja/OneDrive/Documentos/GitHub/colorImage.AAC/lena.png' #The image location is searched
    arch = colorImage(path_file) #The system call colorImage
    arch.displayProperties() #The system call the function