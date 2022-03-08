#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template
import joblib

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        Nikkei = request.form.get('Nikkei')
        print(Nikkei)
        model1 = joblib.load('model1_STIREG')
        predict1 = model1.predict([[Nikkei]])
        str1 = f'The prediction for STI using Regression is: {str(round(predict1[0][0], 2))}'
        return(render_template('index.html', result1=str1))
    else:
        return(render_template('index.html', result1='2'))


# In[4]:


if __name__ == '__main__':
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




