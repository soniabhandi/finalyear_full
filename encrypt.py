from tkinter import *
from functools import partial
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog
import cv2
import numpy as np
import math
import req
global path_image
import json 
import ran
import os
from os import path

image_display_size = 300, 300
global value_of_e
global filename

def cipher(num,e):
    for i in range(len(num)):
        # lenofnum = 3
        X.append((int(num[i])**encrypt_data_into_image.value_of_e)%ran.n)


def RSA(data):
    global plaintext, numC, j, X
    X=[]
    # print(l_n)
    print(encrypt_data_into_image.value_of_e)
    # print(no_d)
    plaintext = data
    plaintext = (plaintext.lower())
    numC = []
    for i in range(len(plaintext)):
        # abcd
        for j in range(len(req.letter)):
            # 25
            if(plaintext[i]==req.letter[j]):
                # pt[0] == letter[0]
                # a ==a
                numC.append(req.number[j])
                # num[0]
                # numC = 01,02,03,04
                
    cipher(numC,encrypt_data_into_image.value_of_e)
    return X

def err():
    e_vals = []
    vv = ""
    for i in range(50,ran.phi):
        if (math.gcd(i,ran.phi)==1) and (len(e_vals)<25):
            e_vals.append(i)
    for i in range(len(e_vals)):
        vv = vv +" "+ str(e_vals[i])
    ss = tuple(e_vals)

    n = StringVar()
    err.evalue = ttk.Combobox(app, width = 20, textvariable = n)
    err.evalue['values'] = ss

    err.evalue.grid(column = 5, row = 5)
    err.evalue.place(x=250,y=120)
    # evalue.current()B
    # m_e = evalue.get()
    # print("err",m_e)
    vals_of_e = Label(app, text="Please Select Value of E(public key) from this : "+vv,
                bg='lavender', font=("Arial", 10))
    vals_of_e.place(x=50, y=180)
    # return m_e
def on_click():
    # Step 1.5
    global path_image
    # use the tkinter filedialog library to open the file using a dialog box.
    # obtain the image of the path
    path_image = filedialog.askopenfilename()
    # load the image using the path
    load_image = Image.open(path_image)
    # set the image into the GUI using the thumbnail function from tkinter
    load_image.thumbnail(image_display_size, Image.ANTIALIAS)
    # load the image as a numpy array for efficient computation and change the type to unsigned integer
    np_load_image = np.asarray(load_image)
    np_load_image = Image.fromarray(np.uint8(np_load_image))
    render = ImageTk.PhotoImage(np_load_image)
    img = Label(app, image=render)
    img.image = render
    img.place(x=20, y=300)


def modInverse(e, phi):
    print("*****",e)
    # e = int(e)

    for x in range(50, phi):
        if (((e%phi) * (x%phi)) % phi == 1):
            return x
    return -1


def encrypt_data_into_image():
    # Step 2
    
    encrypt_data_into_image.value_of_e = int(err.evalue.get())
    print(encrypt_data_into_image.value_of_e)

    global path_image

    # re_n = nvalue.get(1.0, "end-1c")
    # re_n=int(re_n)
    # l_n = re_n 
    # re_e = evalue.get(1.0, "end-1c")
    # re_e=int(re_e)
    # if (math.gcd(re_e,ran.phi)==1):
    #     m_e = re_e
    # else:
    # m_e = err()
    # re_e.delete("1.0","end")
        
    # print(encrypt_data_into_image.value_of_e)
    d = modInverse(encrypt_data_into_image.value_of_e, ran.phi)
    # re_d = dvalue.get(1.0, "end-1c")
    # re_d=int(re_d)
    # no_d = re_d
    print("****")
    # print(l_n)
    print(encrypt_data_into_image.value_of_e)
    # print(no_d)

    

    # print("Value of n is Encrypt :" ,req.n)
    # print("Value of e is :" ,req.e)
    # print("Value of d is :" ,req.d)
    data = txt.get(1.0, "end-1c")
    # load the image
    temp = RSA(data)
    data = ""
    for i in range(len(temp)):
        # [01,02,03,04]
        data += str(temp[i])
        data += " "
    print(data)
    # 01 02 03 04
    # data = (data)
    img = cv2.imread(path_image)
    # break the image into its character level. Represent the characyers in ASCII.
    img2 = data
    data = [format(ord(i), '08b') for i in data]
    _, width, _ = img.shape
    # algorithm to encode the image
    PixReq = len(data) * 3

    RowReq = PixReq/width
    RowReq = math.ceil(RowReq)

    count = 0
    charCount = 0
    # Step 3
    for i in range(RowReq + 1):
        # Step 4
        while(count < width and charCount < len(data)):
            char = data[charCount]
            charCount += 1
            # Step 5
            for index_k, k in enumerate(char):
                if((k == '1' and img[i][count][index_k % 3] % 2 == 0) or (k == '0' and img[i][count][index_k % 3] % 2 == 1)):
                    img[i][count][index_k % 3] -= 1
                if(index_k % 3 == 2):
                    count += 1
                if(index_k == 7):
                    if(charCount*3 < PixReq and img[i][count][2] % 2 == 1):
                        img[i][count][2] -= 1
                    if(charCount*3 >= PixReq and img[i][count][2] % 2 == 0):
                        img[i][count][2] -= 1
                    count += 1
        count = 0
    # Step 6
    # Write the encrypted image into a new file
    # save_text_as = filedialog.asksaveasfilename(defaultextension='.png')
    save_text_ass = filedialog.asksaveasfile(mode='w',defaultextension='.png')
    # print(save_text_as)
    print(save_text_ass.name)
    if save_text_ass:
    	filename =  os.path.basename(save_text_ass.name)
    	print(filename)
    	# filename = save_text_as.name
    	# print(filename)
    	# text_to_save = txt.get('1.0', 'end-1c')
    	# save_text_ass.write(filename)
    	# filename = text_to_save.name
    	save_text_ass.close()
    else:
    	messagebox.showinfo("Error", "Cancelled")



    cv2.imwrite(filename, img)
    # Display the success label.
    success_label = Label(app, text="Encryption Successful!",
                bg='lavender', font=("Times New Roman", 20))
    pep = ("  "*100)
    tempo = Label(app, text="Cipher Text Is : "+pep,
                bg='lavender', font=("Arial", 15))
    success_labely = Label(app, text="Cipher Text Is : "+img2,
                bg='lavender', font=("Arial", 15))


    success_label.place(x=160, y=600)
    tempo.place(x=20,y=500)
    success_labely.place(x=20, y=500)

    dictionary =[
    {
        "name" : filename,
        "d" : d,
        "e" : encrypt_data_into_image.value_of_e,
        "n" : ran.n    
    } 
    ]
    flag = 0
    my_path = 'sample.json'

    if path.exists(my_path):
        with open(my_path , 'r') as file:
            previous_json = json.load(file)
            print(len(previous_json))
            for i in range(len(previous_json)):
                print(previous_json[i]['name'])
                if previous_json[i]["name"] == dictionary[0]['name']:
                    flag = 1
                    print("name already exists")
                    break
            if flag == 0:
                dictionary = previous_json + dictionary
    if flag == 1:
        pass
    else:
        with open(my_path , 'w') as file:
            json.dump(dictionary, file, indent=4)









    # with open("sample.json", "w") as outfile: 
    #     json.dump(dictionary, outfile)
# Step 1
# Defined the TKinter object app with background lavender, title Encrypt, and app size 600*600 pixels.
app = Tk()
app.configure(background='lavender')
app.title("ENCRYPTION")
app.geometry('800x800')
# create a button for calling the function on_click
on_click_button = Button(app, text="Choose Image", bg='white', fg='black', command=on_click)
on_click_button.place(x=700, y=300)


# add a text box using tkinter's Text function and place it at (340,55). The text box is of height 165pixels.
txt = Text(app, wrap=WORD, width=30)
txt.place(x=500, y=350, height=165)

# nvalue = Label(app,text = "Enter the value of n").place(x = 90,y = 90)
# nvalue = Text(app, wrap=WORD, width=30)
# nvalue.place(x=300, y=90, height=20)

evalues = Label(app,text = "Enter the value here").place(x = 90,y = 120)
# evalue = Text(app, wrap=WORD, width=30)

# evalue.place(x=300, y=120, height=20)

# dvalue = Label(app,text = "Enter the value of private key(d)").place(x = 90,y = 150)
# dvalue = Text(app, wrap=WORD, width=30)
# dvalue.place(x=300, y=150, height=20)
# txt_n = Text(app,wrap=WORD,width = 10)
# txt_n.place(x=340,y=230,height = 20)
err()
# encrypt_button = Button(app, text="Generate Value of E", bg='white', fg='black', command=err)
# encrypt_button.place(x=550, y=300)


encrypt_button = Button(app, text="Encode", bg='white', fg='black', command=encrypt_data_into_image)
encrypt_button.place(x=500, y=300)
app.configure(background='skyblue')
app.mainloop()







