from pdf2image import convert_from_path
from PIL import Image
import pytesseract
# Convert PDF to images
images = convert_from_path("C:/Users/souvi/OneDrive/Documents/CPWD assignment.pdf")

# Save each page as an image
for i in range(len(images)):
    images[i].save('page' + str(i) + '.jpg', 'JPEG')

# Extract and print text from each page
for i, image in enumerate(images):
    text = pytesseract.image_to_string(image)
    print(f"\n--- Text from Page {i+1} ---\n")
    print(text)
