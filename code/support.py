from os import walk

def import_folder(path):
    surface_list = []
    
    for _, _, img_files in walk(path):
        for image in img_files:
            print(image)
    
    return surface_list