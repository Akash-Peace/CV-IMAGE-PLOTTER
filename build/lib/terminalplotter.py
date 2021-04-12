import cv2
import time
def plot(image, color='default', size='default', clarity='default'):
    try:
        gray_img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
        color_dict = {'black': '\u001b[40;1m', 'red': '\u001b[41;1m', 'green': '\u001b[42;1m', 'yellow': '\u001b[43;1m',
                      'blue': '\u001b[44;1m', 'magenta': '\u001b[45;1m', 'cyan': '\u001b[46;1m',
                      'default': '\u001b[47;1m',
                      'reset': '\u001b[0m'}
        size_dict = {'tiny': (50, 50), 'small': (75, 75), 'default': (100, 100), 'large': (150, 150),
                     'massive': (200, 200)}
        clarity_dict = {'default': 100, 'dark': 125, 'darker': 150, 'light': 75}
        (thresh, bnw) = cv2.threshold(gray_img, clarity_dict[clarity], 255, cv2.THRESH_BINARY)
        bnw = cv2.resize(bnw, size_dict[size])
        text_color = str(color_dict[color]).replace('4', '3', 1)
        print('\u001b[1m' + text_color + (str(image))[:-4] + color_dict['reset'])
        for i in range(bnw.shape[1]):
            plot_lst = []
            plot_str = ''
            for j in range(bnw.shape[0]):
                if bnw.item(i, j) == 255:
                    plot_lst.append('  ')
                else:
                    plot_lst.append(color_dict[color] + '  ' + color_dict['reset'])
            time.sleep(0.1)
            print(plot_str.join(plot_lst))
    except:
        print('\u001b[31m Hey, Received image is none! Check the image is available or the given path is correct.')