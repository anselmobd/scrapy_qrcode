from qreader import QReader
from cv2 import QRCodeDetector, imread
from pyzbar.pyzbar import decode


# Initialize the three tested readers (QRReader, OpenCV and pyzbar)
qreader_reader = QReader()
cv2_reader = QRCodeDetector()
pyzbar_reader = decode

for img_path in [
    'images/number-labels-including-code-code-code_645391-647.jpg']:
    # Read the image
    img = imread(img_path)

    # Try to decode the QR code with the three readers
    qreader_out = qreader_reader.detect_and_decode(image=img)
    cv2_out = cv2_reader.detectAndDecode(img=img)[0]
    pyzbar_out = pyzbar_reader(image=img)
    
    # # Read the content of the pyzbar output (double decoding will save you from a lot of wrongly decoded characters)
    # pyzbar_out = tuple(
    #     out.data.data.decode('utf-8').encode('shift-jis').decode('utf-8')
    #     for out in pyzbar_out
    # )

    # Print the results
    print(f"Image: {img_path}")
    print(f"QReader: {qreader_out}")
    print(f"OpenCV: {cv2_out}")
    print(f"pyzbar: {pyzbar_out}")
