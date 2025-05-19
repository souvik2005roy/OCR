from PIL import Image
import pytesseract

# Load an image
# img = Image.open('C:/Users/souvi/Og')
img = Image.open("C:/Users/souvi/OneDrive/Pictures/Screenshots/Screenshot 2025-05-17 182542.png")

# Extract text from image
text = pytesseract.image_to_string(img)

print(text)