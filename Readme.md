<h3>script name</h3> 
<p>imageText.py</p>

<h3>Description</h3>
<p>imageText.py will extract text from a given image.<br>
The text will be saved in the file specified by user</p>
<h3>script name : imageText.py</h3>

<p>imageText.py will extract text from a given image.</p>
<p>The text will be saved in the file specified by user</p>

<h3>Installation</h3>
<p>we are going to need several modules to run this example</p>
<p>we need to install <b>tesseract-ocr</b> on our system</p>
<pre><p>On linux do the following:
	sudo apt-get install tesseract-ocr
	sudo apt-get install libtesseract-dev
</p><pre>	
<b>If you are on windows download the tesseract executable from their website</b>
<p>After installing tesseract on the system ,install the package through pip</p>
<i>pip install pytesseract</i>
<p>on linux thats all you have to do to start using the tesseract<p>
<p>On windows one more step is required: <br>we have to tell python where tesseract is installed ie Program files</p>
<pre>import pytesseract
	pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
</pre>	
<h4>To run the program:</h4>
<i>make sure all the modules are installed on your system</i>
<b>The script should be run on python3</b> 
<p>on the Terminal do the following</p>
<i>python3 imageText.py </i>

<p>"The system will then guide you,Enter the filename to save the text
and also specify the path to the image"</p>
<h4>To run the program:</h4>
<pre><b>make sure all the modules are installed on your system
To install a module use pip3 install <module name>
The script should be run on python3 and on a unix based system
on the Terminal do the following
  python3 imageText.py </b></pre>

"The system will then guide you,Enter the filename to save the text
and also specify the path to the image"


