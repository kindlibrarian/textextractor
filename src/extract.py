import configparser
import glob
import pytesseract
from utils import read_config
from PIL import Image, ImageEnhance


def rotate_and_crop(indir,image_list,img_rotate,evencrop,oddcrop):
    """ Rotate and crop the image.  Sometimes even and odd
        pages require different cropping. """
    
    for (nval,f) in image_list:
        im=Image.open(f)
        if img_rotate:
            imr=im.rotate(-90, expand=1)
            im0=imr.crop(evencrop)
            im0.save("%s/crop_img_%04d_00.png" % (indir,nval),format="PNG")
            im1=imr.crop(oddcrop)
            im1.save("%s/crop_img_%04d_01.png" % (indir,nval),format="PNG")
    
        else:
            if nval % 2 == 0:  # even
                im1=im.crop(evencrop)
            else:
                im1=im.crop(oddcrop)
            im1.save("%s/crop_img_%04d.png" % (indir,nval),format="PNG")

def run_pytesseract_ocr(indir,lang='fra'):
    """ Do the OCR on the cropped images """
    
    l = glob.glob("%s/crop_img_*.png" % indir)
    with open('%s/raw_output.txt' % indir, 'w', encoding="utf8") as outfile:
        for i in l:
            img_txt = pytesseract.image_to_string(Image.open(i), lang)
            outfile.write(img_txt)

def clean_up_text(indir,lang='fra'):
    """ Get rid of line breaks in the OCR; apply some language-specific cleanup. """
    
    # Read in the file
    with open('%s/raw_output.txt' % indir, 'r', encoding="utf8") as file :
        filedata = file.read()

    # Replace the target string to get rid of line breaks
    filedata = filedata.replace('-\n', '')
    filedata = filedata.replace('\n\n', '@')
    filedata = filedata.replace('\n', ' ')
    filedata = filedata.replace('@', '\n\n')

    # get rid of weird i umlauts
    text = chr(139)
    filedata = filedata.replace(text, 'i')
    filedata = filedata.replace('ii', 'i')

    # Write the file out again
    with open('%s/cleaned_output.txt' % indir, 'w', encoding="utf8") as file:
        file.write(filedata)

def extract_text(config_data):
    """ using config data, get a list of images and run them through OCR. """
    
    indir=config_data['indir']
    prefix=config_data['prefix']
    img_rotate=config_data['img_rotate']
    lang=config_data['lang']
    evencrop=(config_data['e_left_indent'],config_data['e_top_indent'],config_data['e_horiz_x'],config_data['e_vert_y'])
    oddcrop=(config_data['o_left_indent'],config_data['o_top_indent'],config_data['o_horiz_x'],config_data['o_vert_y'])  

    # get the list of image numbers
    
    l = glob.glob("%s/IMG_*.PNG" % indir)
    imgno_list = [ int(n.split("_")[-1].split(".")[0]) for n in l ]

    # make a list of the image numbers and corresponding image path
    l = []
    for i in imgno_list:
        l.append((i,'%s/%s_%04d.png' % (indir,prefix,i)))

    # rotate image if needed, and crop
    rotate_and_crop(indir,l,img_rotate,evencrop,oddcrop)

    # run the OCR
    run_pytesseract_ocr(indir,lang)

    # clean up the output
    clean_up_text(indir,lang)

if __name__ == "__main__":
    
    # Call the function to read the configuration file
    config_data = read_config()

    # call the extractor
    extract_text(config_data)

