# 1. Install from :
# https://github.com/UB-Mannheim/tesseract/wiki
# 2. Add enviromental PATH with tesseract folder
# 3. pip install pytesseract
# 4. Add: pytesseract.pytesseract.tesseract_cmd = r'C:\Users\lzmi14\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image, ImageEnhance
import pytesseract
import numpy as np


def Change_Contrast(img_path, factor=2):
    img = Image.open(img_path)
    enhancer = ImageEnhance.Contrast(img)
    im_output = enhancer.enhance(factor)
    enhancer_bright = ImageEnhance.Brightness(im_output)
    im_output = enhancer_bright.enhance(factor)
    # angle = 270
    # im_output = im_output.rotate(angle, expand=True)
    im_output.save('images\changed-image.jpg')


# filename = 'images\image01.jpeg'

# Change_Contrast(r'images\1.JPG', 2)
def read_Text_From_Image(filename):
    img1 = np.array(Image.open(filename))
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(img1)
    print(text)
    return text

read_Text_From_Image(r"C:\Łukasz\wycinek.png")
#  i = 0
# PDF

# for page in pages:
#     i = i + 1
#     print(i)
#     page.save(os.path.join('scans' ,( str(i) + 'out.jpg')), 'JPEG')