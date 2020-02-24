from gen2 import generate_plate2
from gen2 import load_fonts
import cv2
import sys

code = sys.argv[1]

fonts, font_char_ims = load_fonts('fonts')
char_ims = font_char_ims['palab.ttf']
plate, rect, code = generate_plate2(320, char_ims, code)
out = plate * rect + (1.0 - rect)
cv2.imwrite(code + '.png',out*255)
