import pytesseract
from PIL import Image
import cv2
import numpy as np

# Function to extract text using OCR
def extract_text(image_path):
    # Load image
    image = cv2.imread(image_path)
    
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to improve OCR accuracy
    _, binary_image = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    
    # Save preprocessed image
    preprocessed_image_path = "preprocessed_image.png"
    cv2.imwrite(preprocessed_image_path, binary_image)
    
    # Extract text with OCR
    extracted_text = pytesseract.image_to_string(Image.open(preprocessed_image_path))
    
    return extracted_text

# Function to check for document tampering (simplified)
def check_tampering(extracted_text, expected_text):
    if extracted_text.strip() == expected_text.strip():
        return "Document is authentic"
    else:
        return "Document may be tampered with"

# Example usage
if __name__ == "__main__":
    # Path to the document image
    document_path = "document.png"
    
    # Expected text (could be from a template or database)
    expected_text = "This is a sample document text to be matched."

    # Extract text from the document
    extracted_text = extract_text(document_path)

    # Check for tampering
    result = check_tampering(extracted_text, expected_text)
    print(result)

