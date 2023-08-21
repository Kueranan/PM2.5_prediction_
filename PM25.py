import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

add_selectbox = st.sidebar.selectbox(
    "status you?",
    ("Student", "Researcher", "Teacher")
)

st.write("""
# Prediction of particulate matter with a diameter of less than 2.5 microns

Prediction PM2.5 in Thailand!🇹🇭
""")

st.sidebar.header('Prediction PM2.5 in Thailand')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features


def main():
    st.header("Prediction PM2.5 in year 2024")
    
    # Load your data from data.csv
    data = pd.read_csv("data_2024.csv")
    
    st.write("### Select Columns to Plot")
    selected_columns = st.multiselect("Select columns to plot", data.columns)
    
    if selected_columns:
        st.write("### Plot")
        plot_type = st.selectbox("Select plot type", ["Line Plot", "Bar Plot", "Scatter Plot"])
        
        plt.figure(figsize=(10, 6))
        
        if plot_type == "Line Plot":
            for column in selected_columns:
                plt.plot(data.index, data[column], label=column)
            
        elif plot_type == "Bar Plot":
            for column in selected_columns:
                plt.bar(data.index, data[column], label=column)
        
        elif plot_type == "Scatter Plot":
            for column in selected_columns:
                plt.scatter(data.index, data[column], label=column)
        
        plt.xlabel("Index")
        plt.ylabel("Values")
        plt.title(f"{plot_type} of Selected Columns")
        plt.legend()
        st.pyplot(plt)
        
        #st.write("### Data Preview")
        #st.dataframe(data.head())

if __name__ == "__main__":
    main()

# Sample DataFrame

df_1 = pd.read_csv('data_2024_new.csv')

def main():
    st.header('Select the date you want to know the trend of Pm2.5 dust.')

    # Convert the 'Date' column to datetime
    #df_1['date'] = pd.to_datetime(df_1['date'])

    # Select a date
    selected_date = st.selectbox('Select a date:', df_1['date'])

    # Retrieve PM2.5 value for the selected date
    pm25_value = df_1.loc[df_1['date'] == selected_date, ' pm25'].iloc[0]

    # Display the selected date and PM2.5 value
    st.write(f" Choose your PM2.5 value for date '{selected_date}':")
    st.write(f"PM2.5 value: {pm25_value}")
if __name__ == '__main__':
    main()


st.header("A brief history of PM2.5 ")
st.subheader('')
 

image = Image.open('PM2.5.jpg')


st.image(image, caption='https://thainakarin.co.th')
st.markdown("PM stands for Particulate matter it is one of the pollutants, made from a mixture of many chemical species both organic and inorganic. Particles vary widely in size, shape, and chemical composition. It may contain metallic compounds or even carcinogenic compounds. Particles are defined by their diameter for air quality regulatory purposes including those with a diameter of 10 microns or less (PM10), Fine particulate matter that is 2.5 microns or less in diameter (PM2.5)")

st.header("Air quality index")
image_index = Image.open('IMG_6081.jpeg')
st.image(image_index, caption='Air quality index')
#st.header("PM 2.5 Graph of year 2022")
    

def main():
    st.title("PM 2.5 Graph of year 2022")
    
    # Load your data from data.csv
    data = pd.read_csv("BKK-2022.csv")
    
    #st.write("### Data Preview")
    #st.dataframe(data.head())
    
    st.write("### Pm2.5 Plot")
    st.line_chart(data[' pm25'])
    
    # Use st.line_chart() to plot a line chart for each column
    #for column in data.columns:
        #st.write(f"#### {column}")
        #st.line_chart(data[' pm25'])
    
if __name__ == "__main__":
    main()


def main():
    st.title("PM 2.5 Graph of year 2021")
    
    # Load your data from data.csv
    data = pd.read_csv("BKK-2021.csv")
    
    #st.write("### Data Preview")
    #st.dataframe(data.head())
    
    st.write("### Pm2.5 Plot")
    st.line_chart(data[' pm25'])
    
    # Use st.line_chart() to plot a line chart for each column
    #for column in data.columns:
        #st.write(f"#### {column}")
        #st.line_chart(data[' pm25'])
    
if __name__ == "__main__":
    main()


st.header("A Process Flow Diagram")
image_index = Image.open('De.jpg')
st.image(image_index, caption='A Flow dirgram process')



#Dowload flie csv
#df = user_input_features()
#st.subheader('User Input parameters')
#st.write(df)

