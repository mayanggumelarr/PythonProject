''' === CONVERTER  JPG TO PNG ==='''

from PIL import Image
import os

def convert(jpg_file):
    if not jpg_file.lower().endswith('.jpg'):
        return  print("Format file bukan JPG")
    
    try:
        with Image.open(jpg_file) as img:
            png_file = jpg_file.rsplit('.',1)[0] + '.png'
            
            # simpan
            img.save(png_file,'PNG')
            print("sukses konversi")
    except Exception as e:
        print("Error")

if __name__ == "__main__":
    jpg_file = input("Nama file JPG: ")
    convert(jpg_file)
        
