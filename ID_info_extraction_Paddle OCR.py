# Libraries Importation
from paddleocr import PaddleOCR,draw_ocr
import os
import cv2
import os
import matplotlib.pyplot as plt
%matplotlib inline


#Initialize the OCR engine
# If you have installed the GPU version of paddleocr, set use_gpu=True
ocr = PaddleOCR(lang='en', show_log=False, use_angle_cls=True, use_gpu=False)


# Get the image
image = cv2.imread(Image Path Here)

# Apply the OCR on the desired image
result = ocr.ocr(image)

# Extract information after application of the OCR engine and Draw bbx
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]

font_path = './PaddleOCR/doc/fonts/simfang.ttf'  # set the font path accoridng to your system
ocr_apply_image = draw_ocr(image, boxes, txts, scores, font_path=font_path) 
 
cv2.imwrite("paddleocr_save_image.png", ocr_apply_image)

img = cv2.cvtColor(ocr_apply_image , cv2.COLOR_BGR2RGB)
plt.figure(figsize=(30,30))
plt.imshow(img)