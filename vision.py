import io
import os

from google.cloud import vision
from google.cloud.vision import types

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

def get_labels(filename = "004.jpg"):
    credential_path = "cred.json"
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
    return labels

get_labels()