# textextractor
Extract text from imaged pages into a text file using pytesseract

Getting started:
1. Ensure that Tesseract OCR is available on your system and pytesseract is available in your python.
  * A good guide can be found here:  https://builtin.com/articles/python-tesseract
2. If you are using a language other than English, download the tesseract module for that language.
  * A list of languages is here: https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html
  * The associated language models are in github here:  https://github.com/tesseract-ocr/tessdata
3. Specify settings in config.ini.  In particular, be sure to specify indir, prefix, img_rotate, and lang in the general section.  
4. Pages scan best when things in the margins are cropped out.  Use test_crop.py to help identify the best crop settings.  You can try different settings by editing the test section of config.ini.  Sometimes right and left pages require different crop settings.  When you have found the best settings, enter them into the evencrop and oddcrop section of the config.ini.  

Known issues:

* This code is not production code and has no error trapping.
* This code has only been tested on png images although it probably works with other formats.
* This code assumes that your OCR pages are saved with the format <some prefix>_<some number>.PNG
* When a word is broken at the end of a line with a hypen, the code cannot distinguish between a hypenated word and a word where a hyphen has been injected.  It will remove the hypen when it removes the line breaks introduced by OCR.
* Some book chapters begin with a large character.   The OCR engine, tesseract_ocr, does not handle this well and may skip the character or otherwise introduce weirdness.
* The OCR engine may inject characters if it sees line drawings.  Normal illustrations are usually ok.
* The OCR engine does not always see numbered chapter headings and may also skip breaks in a chapter.
