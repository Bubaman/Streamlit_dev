import streamlit as st
import pandas as pd
import csv
import os
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# Get data from the csv file
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

file_path = os.path.abspath('Streamlit_dev/vehicles.csv')
my_dict = create_dict_for_each_row(file_path)
#print(my_dict)

def create_diagram(data_dict, target_key):
    # Data for the diagram
    values = [d[target_key] for d in data_dict if target_key in d]
    #print(values)

    # Create the diagram
    fig, ax = plt.subplots()
    ax.bar(range(len(values)), values)
    ax.set_xticks(range(len(values)))
    ax.set_xticklabels(range(1, len(values) + 1))
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.set_title(f'Diagram for Key: {target_key}')

    # Display the diagram using Streamlit
    plt.show()

# Main function
def main():
    st.title("Diagram Example")
    data_dict = my_dict
    target_key = 'Age'
    create_diagram(data_dict, target_key)

if __name__ == '__main__':
    main()