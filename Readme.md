**This software is made with python3 **
A python script which helps to generate certificate for the attendee in jpg or pdf

Original from @rahulsinha036
https://github.com/rahulsinha036/Generate-Certificate-using-Python3

Script modified by Samuel R Osuna https://srosuna.github.io
Twitter @srosuna1
If you consider a donation, please send paypal to https://paypal.me/srojas1974[https://paypal.me/srojas1974](https://www.paypal.com/paypalme/srojas1974) 
or to this BTC address 19Tf35zTRuJ9kijWWv2ZTUSq7zkmgAGEVf
This motivates us to continue developing

**Warning:**
The modification and development of this script was tested on an operating system with Linux kernel, (Ubuntu Studios 20.04), in theory it should work on other platforms such as Windows or Mac, however I have not tested it on those platforms nor do I want to, theoretically, With all the python packages installed in the prerequisites, you should have no problem running on a non-Linux system.

**Requirements.**
You must have the following python packages installed
"Panda" and "Pillow"
run in a terminal
*$ pip install panda*
*$pip install pillow*

To deal with Open Document Format documents or LibreOffice Ods extensions, you must install the "odfpy" package
*$ pip install odfpy*

Instructions:
Download or clone the repository to your hard drive.
execute in terminal 
$ sudo chmod -R +x attendance-certificates-python3/

The files are in the same folder, a jpg/ or pdf/ folder should be created according to your preference.

The file called "gen.xlsx" and "gen.ods" contain the demonstrative examples that all the data must be in the first column of excel, if you have another file with the separated data you must choose them and arrange them so that they are in one same column.

Follow the instructions in the commented lines in the scripts to replace the examples with the files that ideally would be better if they were in the same folder, otherwise, just indicate the path to the file. This is applied to the jpg source image of the certificate of attendance as well as the ttf source.

The colors to choose for printing the font must be R,G,B type

The coordinates where the names will be written are available as X & Y coordinates, this can be found using a graphics editor

The generated files depending on your preference, if they are in pdf, they will be generated in the /pdf/ folder
If you choose jpg image, they will be generated in the /jpg/ folder.

You must create a folder in the root of the project according to your preferences.
If you want it in pdf files, create a folder called pdf/

If you want a jpg image, create a folder called jpg/

**For Running Script**
****JPG Format:****
1) If you want to generate the certificates from an XLXS source for JPG, run:

*$python3 certificate-generator-xlsx-jpg.py*

2) If you want to generate the certificates from an ODS source for JPG, run:

*$python3 certificate-generator-ods-jpg.py*

The generated files will be saved in the jpg/ folder.

****PDF Format****
3) If you want to generate the certificates from an ODS source for PDF, run:

*$python3 certificate-generator-ods-pdf.py*

4) If you want to generate the certificates from an XLSX source for PDF, run:

*$python3 certificate-generator-xlsx-pdf.py*

The generated files will be saved in the pdf/ folder.


enjoy this!!!
Shalom