#!/usr/bin/python3
from PIL import Image
import pytesseract 
import os
import sys
import readline
#the readline is used to set path completion by hitting tab
readline.set_completer_delims(' \t\n=')
readline.parse_and_bind("tab: complete")
#we are going ti extract text from an image and write the text to a file

#ask the user for the name of the file to write the text
def fileName():
	print("Name of the file to copy the text to")
	file_name = input().strip()
	if not file_name:
		file_name = 'imageText'
	return file_name	
def imagePath():	
	print("specify the path of the image to extract text from")
	image_path = input()
	if os.path.exists(image_path):
		image_path = image_path
	else:
		print(f"The file {image_path} does not exist")
		imagePath()
	return image_path

if __name__ == '__main__':
	try:
		file_name = fileName()

		image = imagePath()
		while os.path.exists(image) != True:
			image = imagePath()

		with open(file_name,"w") as f:
			itx = pytesseract.image_to_string(image,lang='eng')
			f.write(itx)
	except KeyboardInterrupt:
		print("---interrupted---")
		sys.exit()
	except Exception as e:
		print("try again")
		sys.exit()
