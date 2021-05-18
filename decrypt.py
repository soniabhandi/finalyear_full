import cv2
from tkinter import filedialog, Tk, Button, Label
from PIL import Image, ImageTk
import numpy as np
import req
import os

image_display_size = 500, 350


def decipher(num,d):
    #lst  222
    print(num)
    print(d)
    num = num.split(" ")
    num.remove("")
    for i in range(len(num)):
        Y.append((int(num[i])**d)%n)
    print("Y",Y)

def Decryptor(message):
    global i,j,Y,d,n
    Y=[]
    tempp = ""
    # for i in range(len(message)):
    #     tempp += str(message[i])
    d = 0
    print(path_image)
    for i in range(len(req.json_object)):
    	if (name_image == req.json_object[i]["name"]):
    		d = req.json_object[i]["d"]
    		n = req.json_object[i]["n"]
    print(d)
    decipher(message,d)
    numD=[]
    for i in range(len(Y)):
        # i = 0
        for j in range(len(req.number)):
            # j = 0
            if(Y[i]==int(req.number[j])):
                #if(1==01)
                numD.append(req.letter[j])
    tap = ""
    for i in numD:
        tap += i
    return tap


def decrypt():
	global path_image,name_image
	path_image = filedialog.askopenfilename()
	print(path_image)
	name_image = os.path.basename(path_image)
	print(name_image)
	load = Image.open(path_image)
	load.thumbnail(image_display_size, Image.ANTIALIAS)
	load = np.asarray(load)
	load = Image.fromarray(np.uint8(load))
	render = ImageTk.PhotoImage(load)
	img = Label(app, image=render)
	img.image = render
	img.place(x=100, y=50)

	filename = os.path.basename(path_image)
	img = cv2.imread(filename)
	data = []
	stop = False
	for index_i, i in enumerate(img):
		i.tolist()
		for index_j, j in enumerate(i):
			if((index_j) % 3 == 2):
				data.append(bin(j[0])[-1])
				data.append(bin(j[1])[-1])
				if(bin(j[2])[-1] == '1'):
					stop = True
					break
			else:
				data.append(bin(j[0])[-1])
				data.append(bin(j[1])[-1])
				data.append(bin(j[2])[-1])
		if(stop):
			break
	message = []
	print("1")
	for i in range(int((len(data)+1)/8)):
		message.append(data[i*8:(i*8+8)])
	message = [chr(int(''.join(i), 2)) for i in message]
	message = ''.join(message)
	print("message",message)
	message = Decryptor(message)
	desc = Label(app,text="Decrypted Text is:  ", bg='lavender', font=("Arial", 15))
	message_label = Label(app, text=message, bg='lavender', font=("Arial", 15))
	desc.place(x = 10,y=450)
	message_label.place(x=180, y=450)

# Defined the TKinter object app with background lavender, title Decrypt, and app size 600*600 pixels.
app = Tk()
app.configure(background='lavender')
app.title("Decrypt")
app.geometry('600x600')
# Add the button to call the function decrypt.
main_button = Button(app, text="Select the Encrypted Image", bg='white', fg='black', command=decrypt)
main_button.place(x=250, y=10)
app.configure(background='skyblue')

app.mainloop()