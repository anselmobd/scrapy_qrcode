from pyzxing import BarCodeReader

def read_qr_code(image_path):
    reader = BarCodeReader()
    results = reader.decode(image_path)
    
    return results[0]['parsed'] if results else "QR Code not found"

# Example usage
print(read_qr_code("images/number-labels-including-code-code-code_645391-647.jpg"))
