from PIL import Image
import pytesseract
path = '下载.jpg'
captcha = Image.open(path)
result = pytesseract.image_to_string(captcha)
print(result)