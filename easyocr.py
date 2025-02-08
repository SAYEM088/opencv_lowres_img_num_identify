import easyocr
reader=easyocr.Reader(['en'])
output=reader.readtext(r"D:\RR246\ocr\opencv-testkit\proimg.jpg")
output