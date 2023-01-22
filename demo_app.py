import streamlit as st

#run C:\Users\murat\PycharmProjects\pythonProject2\demo_app_2.py [ARGUMENTS]
#st.title('Web App')
#st.title('Welcome to Data Science')
#st.title('Geleceğe Tutkuyla Bakanlar')

# Site başlığı ve yazı ekleme
st.title('Web App - Welcom to Data Science')
st.text('Hello Streamlit')

#Başlıklar
st.header('This is a header')
st.subheader('This is a subheader')

#Markdown’la ilgili her şeyi uygulamak mümkün:
st.markdown('This is a normal Markdown')
st.markdown('# This is a bold Markdown')
st.markdown('## This is a thin-bold Markdown')
st.markdown('* This is a Markdown with point')
st.markdown('** This is a small bold Markdown **')
st.markdown('**This is a small bold Markdown**')

#Ön tanımlı stiller ile yazımızı renklendirebiliriz:
st.success('Successful')
st.markdown('`This is a markdown`')
st.info("This is an information")
st.warning('This is a warning')
st.error('This is an error')


"""
Tabi ki etkileşimin doğal bir gereksinimi olarak buton, slider, secim kutucukları gibi bileşenleri de uygulamaya eklemek mümkün. 
Şimdi bunlara kısaca bir göz atalım.
"""

# Tekli seçim kutusu:
st.selectbox('Your Occupation', ['Programmer', 'Data Scientist'])

# Çoklu seçim kutusu:
st.multiselect('Where do you work', ('London','Istanbul','Berlin'))

# Düğmeler:
st.button('Simple Button')

# Kaydırıcılar:
st.slider('What is your level', 0,40, step = 5)


"""
Gördüğünüz gibi, HTML ve CSS kullanmak zorunda değiliz, ancak kullanarak uygulamamızı daha da zenginleştirmek tabi ki mümkün.
"""

html_temp = """

<div style="background-color:tomato;padding:1.5px">

<h1 style="color:white;text-align:center;">Demo Web App </h1>

</div><br>"""

st.markdown(html_temp,unsafe_allow_html=True)
st.title('This is for a good design')
st.markdown('<style>h1{color: red;}</style>', unsafe_allow_html=True)


#Görseller ve çizimler:
#images



import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)



#######################################################################################################################

import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# 2.Ders:
""")




st.write("""
# Simple Iris Flower Prediction App
This app predicts the **Iris flower** type!
""")

st.sidebar.header('User Input Parameters')

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

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])
#st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)



"""import os

key = "streamlit_"
value = os.getenv(key)
print(value)"""






















































