import io
import os
from tkinter import *

from google.cloud import vision
from google.cloud.vision import types

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

#specify filename from front end etc.
def get_labels(filename = 'rs118.jpg'):
    credential_path = "Users/kasey/Downloads/cred.json"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.abspath('./' + filename)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')
    for label in labels:
        # print(label.description)
        if label.description == "T-shirt":
            flabel = "T-shirt"
            break
        elif label.description == "Blouse":
            flabel = "Blouse"
            break
        elif label.description == "Hoodie":
            flabel = "Hoodie"
            break
        else:
            #??
            continue
    return flabel


def computeEmissions(shirtType):
    print(shirtType)


    cottonComp = int(input("% of Cotton: "))/100 
    polyesterComp = int(input("% of Polyester: "))/100  
    nylonComp = int(input("% of Nylon: "))/100
    
    weights={'tshirt': 130, 'shirt': 160, 'hoodie': 250, 'blouse': 200, 'outerwear': 240}
    
    for num in weights:
        if shirtType == 'T-shirt':
            cotton_tshirt = weights['tshirt'] * cottonComp
            polyester_tshirt = weights['tshirt'] * polyesterComp
            nylon_tshirt = weights['tshirt'] * nylonComp
            
        if shirtType == 'Hoodie':
            cotton_hoodie = weights['hoodie'] * cottonComp
            polyester_hoodie = weights['hoodie'] * polyesterComp
            nylon_hoodie = weights['hoodie'] * nylonComp
            
        if shirtType == 'Blouse':
            cotton_blouse = weights['blouse'] * cottonComp
            polyester_blouse = weights['blouse'] * polyesterComp
            nylon_blouse = weights['blouse'] * nylonComp

        if shirtType == 'Outerwear':
            cotton_outerwear = weights['outerwear'] * cottonComp
            polyester_outerwear = weights['outerwear'] * polyesterComp
            nylon_outerwear = weights['outerwear'] * nylonComp           


    if shirtType == 'T-shirt':
        tCO2 = (10.85*cotton_tshirt) + (10.137*polyester_tshirt) + (15.177*nylon_tshirt)
        print (tCO2, 'g of CO2 emmited for the manufacturing process of the ' + shirtType)
    elif shirtType == 'Hoodie':
        hCO2 = (10.85*cotton_hoodie) + (10.137*polyester_hoodie) + (15.177*nylon_hoodie)
        print (hCO2, 'g of CO2 emmited for the manufacturing process of the ' + shirtType)
    elif shirtType == 'Blouse':
        bCO2 = (10.85*cotton_blouse) + (10.137*polyester_blouse) + (15.177*nylon_blouse)
        print (bCO2, 'g of CO2 emmited for the manufacturing process of the ' + shirtType)
    elif shirtType == 'Outerwear':
        oCO2 = (10.85*cotton_outerwear) + (10.137*polyester_outerwear) + (15.177*nylon_outerwear)
        print (oCO2, 'g of CO2 emmited for the manufacturing process of the ' + shirtType)
    else:
        print('cannot identify shirt type... try again')

#where you specify the filename
shirtType = get_labels()

computeEmissions(shirtType)