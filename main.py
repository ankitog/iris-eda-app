
#EDA pkgs
import pandas as pd
import numpy as np

#Data Viz pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
import seaborn as sns

#core pkgs
import streamlit as st


def main():
    st.title('Semi Auto ML App')
    st.text('using streamlit')

    activities = ["EDA", 'Plot', 'Model Building', 'About']
    choice = st.sidebar.selectbox('Select Activity', activities)

    if choice == 'EDA':
        st.subheader('Exploratory Data Analysis')

        data = st.file_uploader("Upload datset", type=['csv','txt'])
        if data is not None:
            df = pd.read_csv(data)
            st.dataframe(df.head())

            if st.checkbox("Show shape"):
                st.write(df.shape)
            
            if st.checkbox("Show Columns"):
                columns = df.columns.to_list()
                st.write(columns)

            if st.checkbox("Show Columns to show"):
                selected_column = st.multiselect("Selct Columns", columns)
                new_df = st.dataframe(df[selected_column])
                

            if st.checkbox("Show Summary"):
                st.write(df.shape)


    if choice == 'Plot':
        st.subheader('Data Visualization')
        data = st.file_uploader("Upload datset", type=['csv','txt'])
        if data is not None:
            df = pd.read_csv(data)
            st.dataframe(df.head())

            if st.checkbox("Corelation with seaborn"):
                st.write(sns.heatmap(df.corr(), annot= True))
                st.pyplot()
            
            if st.checkbox("Pie chart"):
                columns = df.columns.to_list()
                columns_to_plot = st.selectbox("Select 1 column", columns)
                pie_plot = df[columns_to_plot].value_counts().plot.pie(y='mass', figsize=(5, 5))
                st.write(pie_plot)
                st.pyplot()

            all_columns_names = df.columns.tolist()
            type_of_plot = st.selectbox('Select Type of Plot', ['area', 'bar', 'line', 'hist','kde'])
            selected_columns_names = st.multiselect('Select Columns to plot', all_columns_names)
            
            if st.button("Generate Plot"):
                st.success("Generating Customizable plot of {} for{}".format(type_of_plot, selected_columns_names))

                if type_of_plot =='area':
                    cust_data = df[selected_columns_names]
                    st.area_chart(cust_data)

                elif type_of_plot =='bar':
                    cust_data = df[selected_columns_names]
                    st.bar_chart(cust_data)

                elif type_of_plot =='line':
                    cust_data = df[selected_columns_names]
                    st.line_chart(cust_data)

                elif type_of_plot =='area':
                    cust_data = df[selected_columns_names]
                    st.area_chart(cust_data)

                elif type_of_plot:
                    cust_data = df[selected_columns_names].plot(kind=type_of_plot)
                    st.write(cust_data)
                    st.pyplot()

    if choice == 'Model Building':
        st.subheader('Model Building')

    if choice == 'About':
        st.subheader('About')
    

if __name__ == '__main__':
    main()
