import cv2

def read_qr_code(image_path):
    image = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(image)
    
    return data if data else "QR Code not found"

# Example usage
print(read_qr_code("images/number-labels-including-code-code-code_645391-647.jpg"))
