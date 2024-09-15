import configparser

def read_config(test=False):
    """ Read the config file and return a dictionary of values """

    #TODO switch to json and add error trapping
    
    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Read the configuration file
    config.read('config.ini')

    # Access values from the configuration file
    indir = config.get('general', 'indir')
    prefix = config.get('general', 'prefix')
    img_rotate = config.getboolean('general', 'img_rotate')
    lang = config.get('general', 'lang')
    
    if test:
        img_file = config.get('test', 'img_file')
        t_left_indent = config.getint('test', 'left_indent')
        t_top_indent = config.getint('test', 'top_indent')
        t_horiz_x = config.getint('test', 'horiz_x')
        t_vert_y = config.getint('test', 'vert_y')

        config_values = {
            'indir': indir,
            'img_file': img_file,
            'img_rotate': img_rotate,
            't_left_indent': t_left_indent,
            't_top_indent': t_top_indent,
            't_horiz_x': t_horiz_x,
            't_vert_y': t_vert_y
        }
    else:
        e_left_indent = config.getint('evencrop', 'left_indent')
        e_top_indent = config.getint('evencrop', 'top_indent')
        e_horiz_x = config.getint('evencrop', 'horiz_x')
        e_vert_y = config.getint('evencrop', 'vert_y')        
        
        o_left_indent = config.getint('oddcrop', 'left_indent')
        o_top_indent = config.getint('oddcrop', 'top_indent')
        o_horiz_x = config.getint('oddcrop', 'horiz_x')
        o_vert_y = config.getint('oddcrop', 'vert_y')        

        config_values = {
            'indir': indir,
            'prefix': prefix,
            'e_left_indent': e_left_indent,
            'e_top_indent': e_top_indent,
            'e_horiz_x': e_horiz_x,
            'e_vert_y': e_vert_y,
            'o_left_indent': o_left_indent,
            'o_top_indent': o_top_indent,
            'o_horiz_x': o_horiz_x,
            'o_vert_y': o_vert_y,
            'img_rotate': img_rotate,
            'lang': lang
        }

    # Return a dictionary with the retrieved values
    return config_values
