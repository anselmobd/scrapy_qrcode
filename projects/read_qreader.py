import sys
import cv2
from qreader import QReader
from pprint import pprint


image_name = sys.argv[1]
print(image_name)

# Create a QReader instance
qreader = QReader()

# Get the image that contains the QR code
image = cv2.cvtColor(cv2.imread(image_name), cv2.COLOR_BGR2RGB)

# Use the detect_and_decode function to get the decoded QR data
decoded_text = qreader.detect_and_decode(image=image)

pprint(decoded_text)
