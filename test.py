import pandas as pd
import io
import csv
import plotly.graph_objects as go
import streamlit as st

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

file_path = 'Streamlit_dev/vehicles.csv'
my_dict = create_dict_for_each_row(file_path)
#print(my_dict)

data_dict = my_dict
target_key = 'Age'

values = [d[target_key] for d in data_dict if target_key in d]
print(values)

# Create data for the diagram
labels = ['A', 'B', 'C', 'D', 'E']
values = [20, 30, 15, 10, 25]

# Create the diagram using Plotly
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

# Set the layout of the diagram
fig.update_layout(
    title='My Round Diagram',
    font=dict(size=16),
    width=500,
    height=500
)

# Display the diagram in Streamlit
#st.plotly_chart(fig)