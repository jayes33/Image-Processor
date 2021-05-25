import PySimpleGUI as sg
from PIL import Image, ImageEnhance
import os

sg.theme('DarkAmber')
#Image enhancement tab
layout = [[sg.Text('Select your image')],
          [sg.FileBrowse(key='-FILE-', enable_events=True,), sg.Input(key='-IN-')],
          [sg.Radio('Color Balance', 'Option', default=True, key='color_balance'), sg.Slider(range=(0,100), size=(30,10), orientation='h', key='bal')],
          [sg.Radio('Contrast', 'Option', default=False, key='contrast'), sg.Slider(range=(0, 100), size=(30,10), orientation='h', key='con')],
          [sg.Radio('Brightness', 'Option',default=False, key='brightness'), sg.Slider(range=(0, 100), size=(30,10), orientation='h', key='bright')],
          [sg.Radio('Sharpness', 'Option',default=False,key='sharpness'), sg.Slider(range=(0, 100), size=(30,10), orientation='h', key='sharp')],
          [sg.Button('Submit'), sg.Button('Quit')]]
#Image file format converter tab
layout2 = [[sg.Text('Convert image to desire file type')],
           [sg.Radio('JPG', 'Option',default=False,key='jpg')],
           [sg.Radio('PNG', 'Option', default=False, key='png')],
           [sg.Radio('GIF', 'Option', default=False, key='gif')],
           [sg.Text('Image 1'), sg.FileBrowse(key='-IMAGE1-'), sg.Input(key='-COMB1-')],
           [sg.Button('Submit', key='sub3'), sg.Button('Quit')]]
#Images resizer tab
layout3 = [[sg.Text('Resize an entire folder of images at once')],
           [sg.FolderBrowse(key='-FOLDER-'), sg.Input(key='-DIR-')],
           [sg.Text('Enter the desired dimensions of your images')],
           [sg.Text('Width'), sg.Input('0',key='rWidth'), sg.Text('Height'), sg.Input('0', key='rHeight')],
           [sg.Button('Submit', key='sub'), sg.Button('Quit')]]
#Images compressor tab
layout4 = [[sg.Text('Compress an entire folder of images at once')],
           [sg.Radio('Low', 'Option',default=False,key='low')],
           [sg.Radio('Medium', 'Option', default=False, key='med')],
           [sg.Radio('High', 'Option', default=False, key='high')],
           [sg.Text('Select your folder of Images')],
           [sg.FolderBrowse(key='-FOLDER2-'), sg.Input(key='-DIR2-')],
           [sg.Button('Submit', key='sub2'), sg.Button('Quit')]]

group = [[sg.TabGroup([[sg.Tab('Image Enhancer', layout), sg.Tab('Format Conversion', layout2), sg.Tab('Image Resizer', layout3), sg.Tab('Image Compressor', layout4)]])]]
window = sg.Window('JK Image Processor', group)

try:
    while True:
        event, values = window.read()

        if event == 'Quit':
            print('User exited program')
            break

        if event == 'None':
            break

        #image resizer
        if event == 'sub':
            width = int(values['rWidth'])
            height = int(values['rHeight'])
            f = values['-DIR-']
            for file in os.listdir(f):
                imgs = f + "/" + file
                img = Image.open(imgs)
                img = img.resize((width, height))
                img.save(imgs)
            break
        #image compression
        if event == 'sub2':
            f = values['-DIR2-']
            for file in os.listdir(f):
                imgs = f + "/" + file
                img = Image.open(imgs)
                if values['low'] == True:
                    img.save(imgs, optimize=True, quality=25)
                    sg.Popup('Images compressed successfully')
                    break
                elif values['med'] == True:
                    img.save(imgs, optimize=True, quality=50)
                    sg.Popup('Images compressed successfully')
                    break
                elif values['high'] == True:
                    img.save(imgs, optimize=True, quality=75)
                    sg.Popup('Images compressed successfully')
                    break
            break
        #format conversion
        if event == 'sub3':
            img = Image.open(values['-IMAGE1-'])
            rgb = img.convert("RGB")
            if values['jpg'] == True:
                rgb.save('converted-image.jpg')
                sg.Popup('Image converted successfully')
                break
            if values['png'] == True:
                rgb.save('converted-image.png')
                sg.Popup('Image converted successfully')
                break
            if values['gif'] == True:
                rgb.save('converted-image.gif')
                sg.Popup('Image converted successfully')
                break
            break

        #Prevents users from pressing submit without adding an image
        if event == 'sub' and values['-DIR-'] == '':
            sg.popup('Please select a folder containing images')
        if event == 'sub2' and values['-DIR2-'] == '':
            sg.popup('Please select a folder containing images')
        if event == 'sub3' and values['-IMAGE1-'] == '':
            sg.popup('Please select an image')
        if event == 'Submit' and values['-FILE-'] == '':
            sg.popup('Please select an image')

        if event == 'Submit':
            img: object = values['-FILE-']
            im = Image.open(values['-FILE-'])
            if values['color_balance'] == True:
                color_balance = float(values['bal'])
                vBal = 0.02 * color_balance
                color_balance = ImageEnhance.Color(im)
                color_balance.enhance(vBal).save('enhanced-image.jpg')
                sg.Popup('Color balance changed', 'Image saved as enhanced-image.jpg')
                break
            if values['contrast'] == True:
                contrast = float(values['con'])
                vCon = 0.02 * contrast
                contrast = ImageEnhance.Contrast(im)
                contrast.enhance(vCon).save('enhanced-image.jpg')
                sg.Popup('Contrast enhanced', 'Image saved as enhanced-image.jpg')
                break
            elif values['brightness'] == True:
                brightness = float(values['bright'])
                vBright = 0.02 * brightness
                brightness = ImageEnhance.Brightness(im)
                brightness.enhance(vBright).save('enhanced-image.jpg')
                sg.Popup('Brightness enhanced', 'Image saved as enhanced-image.jpg')
                break
            elif values['sharpness'] == True:
                sharpness = float(values['sharp'])
                vSharp = 0.02 * sharpness
                sharpness = ImageEnhance.Sharpness(im)
                sharpness.enhance(2).save('enhanced-image.jpg')
                sg.Popup('Sharpness enhanced', 'Image saved as enhanced-image.jpg')
                break
except Exception as e:
    sg.popup_error("ERROR!", e)



