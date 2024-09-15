# textextractor
Extract text from imaged pages into a text file using pytesseract



Known issues:

* This code is not production code and has no error trapping. 
* Some book chapters begin with a large character.   The OCR engine, tesseract_ocr, does not handle this well and may skip the character or otherwise introduce weirdness.
* The OCR engine may inject characters if it sees line drawings.  Normal illustrations are usually ok.
