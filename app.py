

# 1.Convert pdf file into images via pdfium2 

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain 



from pytesseract import image_to_string , pytesseract
from PIL import Image 
from io import BytesIO 

import pypdfium2 as pdfium 

import streamlit as st 

import multiprocessing
from tempfile import NamedTemporaryFile 

import pandas as pd 


from src.utils import tesseract_cmd 

pytesseract.tesseract_cmd = tesseract_cmd()

def convert_pdf_to_images(file_path , scale = 300/72) : 
    pdf_file = pdfium.PdfDocument(file_path)

    page_indices = [i for i in range(len(pdf_file))]

    renderer = pdf_file.render(
        pdfium.PdfBitmap.to_pil , 
        page_indices = page_indices , 
        scale = scale 
    )

    final_images = []

    for i , image in zip(page_indices , renderer) : 

        image_byte_array = BytesIO()
        image.save(image_byte_array , format = 'jpeg' , optimize = True)
        image_byte_array = image_byte_array.getvalue()
        final_images.append(dict({i : image_byte_array}))

    return final_images 


# 2. Extract text from images using pytesseract 

def extract_text_from_img(list_dict_final_images) : 

    image_list = [list(data.values())[0] for data in list_dict_final_images]
    image_content = []

    for index , image_bytes in enumerate(image_list) : 

        image = Image.open(BytesIO(image_bytes))
        raw_text = str(image_to_string(image))
        image_content.append(raw_text)

    return "\n".join(image_content)

def extract_content_through_url(url : str)  : 
    image_list = convert_pdf_to_images(url)
    text_with_pytesseract = extract_text_from_img(image_list)

    return text_with_pytesseract

if __name__ == "__main__" : 
     
    content = extract_content_through_url('project.pdf')
    print(content)
    
    multiprocessing.freeze_support()