import streamlit as st
import pandas as pd
import numpy as np
import csv
import os
import spacy

st.title('Streamlit test session')
st.write('Hello from the Streamlit app')

#Button1: read file and create list of dict
def create_dict_for_each_row(file_path):
    result_list = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        keys = next(csv_reader)  # Get the first row as keys
        for row in csv_reader:
            row_dict = {}
            for i, value in enumerate(row):
                key = keys[i]
                row_dict[key] = value
            result_list.append(row_dict)
    return result_list

file_path = os.path.abspath('vehicles.csv')
my_dict = create_dict_for_each_row(file_path)
keys = set().union(*(d.keys() for d in my_dict))

#Button exemple
st.header('Button section')
button1 = st.button('Click Me')
if button1:
    st.write('This is some text')
    st.table(my_dict)

#Checkbox exemple
st.header('Checkbox section')
like = st.checkbox('Do you like this app?')
if like:
    button2 = st.button('Submit')

#Radio button exemple
st.header('Radio button section')
animal_list = ('Lion', 'Bear', 'Wolf')
animal = st.radio('What kinde data do you choose?', animal_list)

#Selectbox exemple
st.header('Selectbox section')
select_key = st.selectbox('What kinde data do you choose?', keys)
button3 = st.button('Submit Data')
if button3:
    for key in keys:
        if select_key == key:
            select_key_table = st.table([d[key] for d in my_dict if key in d])

#Multiselect exemple
st.header('Multiselect section')
data_options = st.multiselect('What data options do you choose?', keys)
button4 = st.button('Submit Data options')
""" if button4:
    for key in keys:
        if data_options == key:
            data_options_table = st.table([d[key] for d in my_dict if key in d]) """

#Slider exemple
st.header('Slider section')
age_slider = st.slider('Choose age', 1,100)
""" if st.button('Submit age'):
    select_age_table = st.table([d['Gender'] for d in my_dict if age_slider in d]) """

#Text input exemple
st.header('Text input section')
user_text = st.text_input('Imput your text')

#Sidebar and expend exemple
def clean_text(text):
    text = text.replace("`", "").replace("-\n", "").strip()
    return text

st.sidebar.image('options.png',)
st.sidebar.header('Options')
text = st.sidebar.text_area('Paste text here')
if st.sidebar.button('Clean text'):
    st.header('Expend exemple')

    colum1, colum2 = st.columns(2)
    colum1_expend = colum1.expander('Expande original')
    with colum1_expend:
        colum1_expend.header('Original text')
        colum1_expend.write(text)

    clean = clean_text(text)
    colum2_expend = colum2.expander('Expend clean')
    with colum2_expend:
        colum2_expend.header('Clean text')
        colum2_expend.write(clean)

#Forms exemple
@st.cache(allow_output_mutation=True)
def load_model(model_name)
    nlp = spacy.load(model_name)
    return nlp

nlp = load_model('en_core_web_lg')

def extract_entities(ent_types, text_ent):
    results = []
    doc = nlp(text_ent)
    for ent in doc.ents:
        if ent.label_ in ent_types:
            results.append((ent.text, ent.label_))
    return results

form1 = st.sidebar.form(key='Params')
form1.header('Params')
ent_type = form1.multiselect('Select the entities you want to extract', ['PERSON', 'ORG', 'GPE'])
st.title('Forms exemple')
form1.form_submit_button('Submit options')
text_ent = st.text_area('Sample text', 'James enjoing play basketball in Florida for the Salvation Army.')
hits = extract_entities(ent_type, text_ent)
st.write(hits)