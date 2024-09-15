import configparser
from PIL import Image, ImageEnhance
from utils import read_config

# for testing crop settings

config_data=read_config(test=True)
img_crop_vals = (config_data['t_left_indent'],config_data['t_top_indent'],config_data['t_horiz_x'],config_data['t_vert_y'])
img_rotate = config_data['img_rotate']
img_file = config_data['img_file']
indir = config_data['indir']

f = "%s/%s" % (indir,img_file)

im=Image.open(f)

if img_rotate:
    imr=im.rotate(-90, expand=1)
    im1=imr.crop(img_crop_vals)
else:
    im1=im.crop(img_crop_vals)

im1.save("%s\\test_crop.png" % indir,format="PNG")

print("Original image dimensions are: %s x %s" % (im.size))
print("Your crop settings are: \n\t%s left indent\n\t%s top indent\n\t%s horizontal crop point\n\t%s vertical crop point" % (img_crop_vals))
print("View test_crop.png and adjust settings in config.ini if needed")
