import io
import os

from google.cloud import vision
from google.cloud.vision import types

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

#specify filename from front end etc.
def get_labels(filename = "rs118.jpg"):
    credential_path = "../cred.json"
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
        print(label.description)
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
    


    cottonComp = int(input("% of Cotton: "))/100 
    polyesterComp = int(input("% of Polyester: "))/100  
    nylonComp = int(input("% of Nylon: "))/100
    
    weights = {tshirt: 130, shirt: 160, hoodie: 250, blouse: 200, outerwear: 240}
    
    for num in weights:
        if shirtType == 'T-shirt':
            cotton_tshirt = weights[tshirt] * cottonComp
            polyester_tshirt = weight[tshirt] * polyesterComp
            nylon_tshirt = weight[tshirt] * nylonComp
            
        if shirtType == 'Hoodie':
            cotton_hoodie = weights[hoodie] * cottonComp
            polyester_hoodie = weight[hoodie] * polyesterComp
            nylon_hoodie = weight[hoodie] * nylonComp
            
        if shirtType == 'Blouse':
            cotton_blouse = weights[blouse] * cottonComp
            polyester_blouse = weight[blouse] * polyesterComp
            nylon_blouse = weight[blouse] * nylonComp

    CO2 = (10.85*cotton_tshirt) + (10.137*polyester_tshirt) + (15.177*nylon_tshirt)
    print (CO2)

#where you specify the filename
shirtType = get_labels()

computeEmissions(shirtType)