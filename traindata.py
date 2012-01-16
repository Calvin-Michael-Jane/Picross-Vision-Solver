import os
import Image
 
path = 'images/train/'
listing = os.listdir(path)
with open('data/ocr.train', 'w') as f:
    f.write('%d\n' % len(listing))
    for filename in listing:
        img = Image.open(path+filename)
        digit_image = img.convert("L")
        digit_image = digit_image.resize([14, 14])
        digit_pixels = digit_image.load()
        width, height = digit_image.size
    
        # clamp values to 0, 255
        #trainex = []
        for x in range(width):
            for y in range(height):
                if digit_pixels[x, y] < 127:
                    digit_pixels[x, y] = 0
                else:
                    digit_pixels[x, y] = 255;
                #trainex.append(float(digit_pixels[x, y])/255.0)
                f.write('%f ' % (digit_pixels[x, y] / 255.0))
    
        # add real value
        #trainex.append(filename[-5])
        if filename[-6] != '_':
            f.write('10\n')
        else:
            f.write('%d\n' % int(filename[-5]))