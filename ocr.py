
from PIL import Image #Image Processing
import numpy as np #Image Processing 
import easyocr as ocr  #OCR
import streamlit as st  #Web App

#title
st.title(" Extract Text from Images")

#subtitle
st.markdown("")

st.markdown("")

#image uploader
image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])


st.cache_data
def load_model(): 
    reader = ocr.Reader(['en','hi'],model_storage_directory='.')
    return reader 

reader = load_model() #load model

if image is not None:

    input_image = Image.open(image) #read image
    st.image(input_image) #display image

    with st.spinner("🤖 AI is at Work! "):
        

        result = reader.readtext(np.array(input_image))

        result_text = [] #empty list for results


        for text in result:
            result_text.append(text[1])

        st.write(result_text)
  
    st.balloons()
else:
    st.write("Upload an Image")

st.caption("Made by @Satyam Sharma and Sakshi Sahu")