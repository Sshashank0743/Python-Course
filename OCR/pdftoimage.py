from pdf2image import convert_from_path
from pytesseract import image_to_string
from PIL import Image
import os
from pytesseract import pytesseract

# Configure paths
POPPLER_PATH = r'C:\poppler-24.08.0-0\Library\bin'
PDF_PATH = 'cyber.pdf'
OUTPUT_FOLDER = 'output_images'
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Ensure the output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Step 1: Convert PDF pages to images
def pdf_to_images(pdf_path, output_folder):
    images = convert_from_path(pdf_path, poppler_path=POPPLER_PATH, dpi=300)
    image_paths = []
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f"book_{i + 1}.jpg")
        image.save(image_path, 'JPEG')
        image_paths.append(image_path)
    return image_paths

# Step 2: Perform OCR on the images
def ocr_from_images(image_paths):
    ocr_results = {}
    for image_path in image_paths:
        text = image_to_string(Image.open(image_path))
        ocr_results[os.path.basename(image_path)] = text
    return ocr_results

# Run the conversion and OCR
if __name__ == '__main__':
    print("Converting PDF to images...")
    image_paths = pdf_to_images(PDF_PATH, OUTPUT_FOLDER)
    
    print("Performing OCR on images...")
    ocr_results = ocr_from_images(image_paths)
    
    # Save OCR results to a text file
    with open('ocr_results.txt', 'w', encoding='utf-8') as f:
        for image_name, text in ocr_results.items():
            f.write(f"--- {image_name} ---\n")
            f.write(text + '\n\n')
    
    print("OCR process completed. Results saved to ocr_results.txt.")
