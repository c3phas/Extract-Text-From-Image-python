### script name
imageText.py

### Description
* imageText.py will extract text from a given image.
The text will be saved in the file specified by user

### Installation
* we are going to need several modules to run this example
* we need to install tesseract-ocr on our system
```
On linux do the following:
	sudo apt-get install tesseract-ocr
	sudo apt-get install libtesseract-dev
```	
If you are on windows download the tesseract executable from their website
After installing tesseract on the system ,install the package through pip
##### pip install pytesseract
on linux thats all you have to do to start using the tesseract
On windows one more step is required: 
**we have to tell python where tesseract is installed ie Program files**
```
import pytesseract
	pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
````
#### To run the program:
make sure all the modules are installed on your system
The script should be run on python3
* on the Terminal do the following
```
$python3 imageText.py
```

The system will then guide you.
Enter the filename to save the text
and also specify the path to the image




