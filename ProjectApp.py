from tkinter import PhotoImage
import joblib,os
from rsa import sign
import streamlit as st
import keras
from PIL import Image
import tensorflow as tf
from keras.preprocessing import image
import numpy as np
from keras import models
from keras.applications.vgg16 import preprocess_input
import matplotlib.pyplot as plt
import cv2 as cv

def model(model_file):
	return joblib.load(open(os.path.join(model_file),"rb"))
def verify(file):
        image = Image.open(file)
        image = tf.image.resize(image, [224,224]) 
        image = tf.keras.preprocessing.image.img_to_array(image)
        image = image / 255.0      
        image = tf.expand_dims(image, axis=0)   
        model = tf.keras.models.load_model("FinalModel.h5")
        features = model.predict(image)
        thresholded = (features>0.5)*1
        ind = np.argmax(thresholded)
        return ind


def verification(fphoto,sphoto,a,b):
    if((fphoto=="face")and(sphoto=="signature")):
       st.write("Upoaded Correctly")
       disp(a,b,fphoto,sphoto)
    elif((fphoto=="none")and(sphoto=="none")):
        disp(a,b,fphoto,sphoto)
    elif((fphoto=="face")and(sphoto=="none")):
        disp(a,b,fphoto,sphoto)
    elif((fphoto=="none")and(sphoto=="signature")):
        disp(a,b,fphoto,sphoto)
        st.error("Face photo is not uploaded")
    elif((fphoto=="signature")and sphoto=="none"):
        disp(a,b,fphoto,sphoto)
        st.error("signature is uploaded in face slot and signature slot is empty")
    elif((fphoto=="none")and sphoto=="face"):
        disp(a,b,fphoto,sphoto)
        st.error("face is uploaded in signature slot and face slot is empty")
    elif((fphoto=="signature")and sphoto=="face"):
        st.error("Photos uploaded in wrong slots")
        swap(a,b)
    elif((fphoto=="face")and sphoto=="face"):
        st.error("Face Photo is uploaded in both slots")
        merge(a,b,"Signature")
    elif((fphoto=="signature")and sphoto=="signature"):
        st.error("Face Photo is uploaded in both slots")
        merge(b,a,"Face")


def disp(photo,sign,ps,ss):
    if(ps=="face" and ss=="signature"):
        st.image(photo,caption="Face",width=300)
        st.image(sign,caption="Signature",width=300)
    elif(ps=="none" and ss=="none"):
        st.error("Face and Signature not uploaded")
    elif(ps=="face" and ss=="none"):
        st.image(photo,caption="Face",width=300)
        st.error("Signature photo not uploaded")
    elif(ps=="none" and ss=="signature"):
        st.image(photo,caption="Face",width=300)
        st.error("Signature photo not uploaded")




def swap(photo,sign):
     a=photo
     photo=sign
     sign=a
     st.write("Face Photo")
     st.image(photo, width=300)
     st.write("Signature Photo")
     st.image(sign, width=300)
    
def merge(face,photo,p):
    a=face;
    photo=None
    st.write("Upload ",p)

def main():
    st.title("Signature and Photo Verification")
    st.write("---")
    photo=st.file_uploader("Upoad your photo")
    sign=st.file_uploader("Upload your Signature")
    predict= st.button("Submit")
    if predict:
        if photo is None:
            ind=2
        else:
            ind=verify(photo)
        if sign is None:
            ind1=2
        else:
            ind1=verify(sign)
        label = ['face','signature','none']
        verification(label[ind],label[ind1],photo,sign)

        
   
if __name__=='__main__':
    main()