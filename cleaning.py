import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
st.set_page_config(layout="wide")



url='https://drive.google.com/file/d/1vvtD_o59OXwJrBwiJATzEuquizzUowP-/view?usp=share_link'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
data = pd.read_csv(url)

#path=r'C:\Users\muhammad.faiz\Downloads\graded assingment 3/'
#filename='athlete_events.csv'
#filepath=path+filename
#data=pd.read_csv(filepath)
#data=pd.read_csv(filename)

data['Age'].fillna(data['Age'].mean(), inplace=True )
data['Height'].fillna(data['Height'].mean(),inplace=True)
data['Weight'].fillna(data['Weight'].mean(),inplace=True)
data['Medal'].fillna('No Medal', inplace= True)
data['Age'] = data['Age'].astype(np.int64)
data = data[data["Medal"] != 'No Medal']
data.info()



st.title('Olympic History Dashboard')
st.subheader("Muhammad Faiz Naveed")


unique_country= sorted(data['Team'].unique())
selected_country = st.selectbox('Select Country',unique_country)

subset_country_data=data[data['Team']==selected_country]
total_participation=subset_country_data.shape[0]
total_gold= subset_country_data[subset_country_data['Medal']=='Gold'].shape[0]
total_silver= subset_country_data[subset_country_data['Medal']=='Silver'].shape[0]
total_bronze= subset_country_data[subset_country_data['Medal']=='Bronze'].shape[0]

 
st.header('Olympics - {}'.format(selected_country))
col1, col2, col3, col4, = st.columns(4)
col1.metric('Total Participation', total_participation)
col2.metric('Gold Medals', total_gold)
col3.metric('Silver Medals', total_silver)
col4.metric('Bronze Medals', total_bronze)

st.set_option('deprecation.showPyplotGlobalUse', False)
with st.container():
  linechart, barchart , table = st.columns(3)
   
medal_data = subset_country_data[subset_country_data["Medal"].isin(['Gold', 'Silver', 'Bronze'])] 
  
with linechart: 
  linechart.header('Single Line Chart')
  #sns.set_style("whitegrid")
  sns.lineplot(x="Year", y="Medal", hue="Medal", data=medal_data)
  plt.xlabel("Total Year")
  plt.ylabel("Medal Count")
  linechart.pyplot()
  
  #when we do group-by the data converts into keyvalue pairs we have to call them using index and valeus
#athelte_data= data.groupby('Name')['Medal'].count().sort_values(ascending=False).head(5)


athelte_data= subset_country_data.groupby('Name')['Medal'].count().sort_values(ascending=False).head(5)
with barchart:
    barchart.header('bar Line Chart')
    sns.barplot(x=athelte_data.values, y= athelte_data.index, orient='h')
    plt.xlabel('Name of Athelte')
    plt.ylabel('Total Medals ')
    barchart.pyplot()

table_data=subset_country_data.groupby('Sport')['Medal'].count().sort_values(ascending=False).head(5)    
with table:
    table.header('table Chart')
    st.dataframe(table_data, height=220, width=400)
 
with st.container():
  histogram, piechart , ver_bar = st.columns(3)
 

with histogram: 

       histogram.header('Histogram ')
       sns.histplot(x='Age', data=subset_country_data, bins=10)
       plt.xlabel('Age of Athlete')
       plt.ylabel('Total Medal')
       histogram.pyplot()
       
           
gender_data=subset_country_data.groupby('Sex')['Medal'].count()
with piechart:
    piechart.header('Pie Chart')
    plt.pie(gender_data,labels=gender_data.index,autopct='%.0f%%')
    piechart.pyplot()
    
    
gender_data=subset_country_data.groupby('Season')['Medal'].count()    
with ver_bar:
    ver_bar.header('Vertical Bar C')
    sns.barplot(x=gender_data.values, y= gender_data.index)
    plt.xlabel('Name of Season')
    plt.ylabel('Total Medals ')
    ver_bar.pyplot()
    
    
    