import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio
import matplotlib as pylab
import seaborn as sns
import numpy as np
import io
from PIL import Image




st.set_page_config(
    page_title="Data Analysis App",
    page_icon="📊"
)

col1, col2= st.columns([2,1])

col1.header('Data Analysis App')

im = Image.open("nm.png")
col2.image(im)

st.write("Welcome to the Data Analysis App!")
st.write("This app allows you to explore, visualize, and analyze your data in a user-friendly interface.")
st.write("To get started, simply upload a CSV file and start exploring. You can preview the data, visualize it using different plot types, and perform various analyses.")
st.write("We hope you find this app useful and we encourage you to play around and discover new insights about your data.")



uploaded_file = st.file_uploader("Choose a CSV file",type='csv')
generate= st.button('Analyize')

customized_button = st.markdown("""
    <style >
    div.stButton > button:first-child {
        background-color: #0099ff;
        color:#ffffff;
    }
    div.stButton > button:hover {
        background-color: #00ff00;
        color:#ffffff;
        }
    </style>""", unsafe_allow_html=True)

if 'load_state' not in st.session_state:
    st.session_state.load_state = False

if generate or st.session_state.load_state:
    st.session_state.load_state = True

    if uploaded_file is not None:

        # with codecs.open(file_name, 'r', encoding='utf-8',
        #         errors='ignore') as fdata:
        dataframe = pd.read_csv(uploaded_file)

        st.subheader("Data Preview")
        col1, col2, col3 = st.columns([1,10,1])

        with col1:
            st.write("")

        with col2:
            st.dataframe(dataframe)

        with col3:
            st.write("")

        st.markdown("""<hr style="height:3px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([10,3,10])

        with col1:
            st.subheader("Data Describe")

        with col2:
            st.write("")

        with col3:
            st.subheader("Data Info")


        col1, col2,col3 = st.columns([17,4,25])

        with col1:
            st.write(dataframe.describe())

        with col2:
            st.write("")

        with col3:
            buffer = io.StringIO()
            dataframe.info(buf=buffer)
            s = buffer.getvalue()

            st.text(s)
        
        st.markdown("""<hr style="height:3px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

        st.subheader('Null Values Ratio')
        
        def null_ratio(df):

            data= [(col,dataframe[col].isnull().sum()/len(dataframe)*100)
                for col in dataframe.columns if dataframe[col].isnull().sum()>0]

            columns= ['col', 'ratio']
            missing_data= pd.DataFrame(data,columns=columns)

            fig = px.bar(missing_data, x='col', y='ratio')
            st.write(fig)

        null_ratio(dataframe)


        st.markdown("""<hr style="height:2px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

        
        st.subheader("Convert Non-Numeric Data to Numeric")
        col = st.selectbox("Select a column to convert", dataframe.columns)
        if col:
            dataframe[col] = pd.to_numeric(dataframe[col], errors='coerce')
            # st.write("Column converted to numeric data type")
        # if (dataframe[col].dtype == np.float64 or dataframe[col].dtype == np.int64):
            Convert= st.button('Convert')
            if Convert:
                if (dataframe[col].dtype == np.float64 or dataframe[col].dtype == np.int64):
                    st.success('Column converted to numeric data type')
    
        # st.markdown("""<hr style="height:2px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
        
        st.subheader("null values")
        col = st.selectbox("Select a column to Impute or Delete", dataframe.columns[dataframe.isna().any()].tolist())
        if col:
            option = st.selectbox("Select a visualization type", ["Mean", "Mode", "Median", "Delete Null Values"])
            if (option == "Mean" and (dataframe[col].dtype == np.float64 or dataframe[col].dtype == np.int64)):
                dataframe[col].fillna(dataframe[col].mean(),inplace=True)

            elif option == "Mode" and dataframe.dtypes[col] == 'object':
                dataframe[col].fillna(dataframe[col].mode()[0],inplace=True)

            elif option == 'Median' and (dataframe[col].dtype == np.float64 or dataframe[col].dtype == np.int64):
                dataframe[col].fillna(dataframe[col].median(), inplace=True)

            elif option == "Delete Null Values":
                dataframe.dropna(subset=[col],inplace=True)
        
            Fill= st.button('Fill')
            if Fill:
                if (dataframe.dtypes[col] == 'object' and option == 'Mean' or option == 'Median'):
                    st.error('Chose another methhod')

                elif option == "Delete Null Values":
                    st.success('Null values deleted')
                    null_df= dataframe.isnull().sum()
                    columns= ['Null_values_count']
                    missing_data= pd.DataFrame(null_df,columns=columns)
                    st.write(missing_data.T)

                else:
                    st.success('Column filled')
                    null_df= dataframe.isnull().sum()
                    columns= ['Null_values_count']
                    missing_data= pd.DataFrame(null_df,columns=columns)
                    st.write(missing_data.T)

        
        st.markdown("""<hr style="height:2px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

        st.subheader("Graphs")

        col1, col2, col3 = st.columns([1,1,1])
        
        categ= [col for col in dataframe.columns if dataframe.dtypes[col] == 'object']

        box_1= col1.selectbox('Select Column 1', categ)
        box_2= col2.selectbox('Select Column 2 ', categ)
        box_3= col3.selectbox('Select Column 3', categ)

        col4, col5, col6 = st.columns([1,1,1])

        numer= [col for col in dataframe.columns if (dataframe[col].dtype == np.float64 or dataframe[col].dtype == np.int64)]

        box_4= col4.selectbox('Select Column 4', numer)
        box_5= col5.selectbox('Select Column 5 ',numer)
        box_6= col6.selectbox('Select Column 6', numer)
        

        graphs = st.container()

        with graphs:
            #COLUMNS FOR CHARTS
            col1, col2, col3 = st.columns([1,1,1])

            fig1= px.pie(dataframe, values=box_4, names=box_1 ,hole=0.5)
            fig1.update_layout(
                showlegend=False,
                margin=dict(l=1,r=1,t=1,b=1),
                height=200,
                yaxis_scaleanchor="x",)
            col1.plotly_chart(fig1, use_container_width=True)

            fig2= px.pie(dataframe, values=box_5, names=box_2 ,hole=0.5)
            fig2.update_layout(
                showlegend=False,
                margin=dict(l=1,r=1,t=1,b=1),
                height=200,
                yaxis_scaleanchor="x",)
            col2.plotly_chart(fig2, use_container_width=True)

            fig3= px.pie(dataframe, values=box_6, names=box_3 ,hole=0.5)
            fig3.update_layout(
                showlegend=False,
                margin=dict(l=1,r=1,t=1,b=1),
                height=200,
                yaxis_scaleanchor="x",)
            col3.plotly_chart(fig3, use_container_width=True)
            
        st.markdown("""<hr style="height:2px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)


        option = st.selectbox("Select a visualization type", ["Bar plot", "Box plot", "Violin plot", "Scatter plot","line"])

        if option == "Bar plot":
            col1, col2 = st.columns([1,1])
            x = col1.selectbox("Select a column for the x-axis", categ)
            y = col2.selectbox("Select a column for the y-axis", numer)
            fig= px.bar(dataframe,x=x, y=y, title='Bar Plot For {} and {}'.format(x,y))
            # st.set_option('deprecation.showPyplotGlobalUse', False)
            st.write(fig)

        elif option == "Box plot":
            col1, col2 = st.columns([1,1])
            x = col1.selectbox("Select a column for the x-axis", categ)
            y = col2.selectbox("Select a column for the y-axis", numer)
            fig = px.box(dataframe, x=x, y=y,title='Box plot Given {} and {}'.format(x,y))
            st.write(fig)

        elif option == "Violin plot":
            col1, col2 = st.columns([1,1])
            x = col1.selectbox("Select a column for the x-axis", categ)
            y = col2.selectbox("Select a column for the y-axis", numer)
            fig = px.violin(dataframe, x=x, y=y,box=True, points="all", title='Violin plot Given {} and {}'.format(x,y))
            # fig.update_layout(paper_bgcolor="rgb(7,8,8)", plot_bgcolor="rgb(10,10,10)")
            st.write(fig)

        elif option == "Scatter plot":
            col1, col2 = st.columns([1,1])
            x = col1.selectbox("Select a column for the x-axis", categ)
            y = col2.selectbox("Select a column for the y-axis", numer)
            fig = px.scatter(dataframe,x=x,y=y,title='Scatter plot Given {} and {}'.format(x,y))
            # fig.update_layout(paper_bgcolor="rgb(7,8,8)", plot_bgcolor="rgb(10,10,10)")
            st.write(fig)

        elif option == "line":
            col1, col2 = st.columns([1,1])
            x = col1.selectbox("Select a column for the x-axis", categ)
            y = col2.selectbox("Select a column for the y-axis", numer)
            fig = px.line(dataframe,x=x,y=y,title='Line plot Given {} and {}'.format(x,y))
            # fig.update_layout(paper_bgcolor="rgb(7,8,8)", plot_bgcolor="rgb(10,10,10)")
            st.write(fig)
