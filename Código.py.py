#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install cutecharts')


# In[28]:


import pandas as pd
import cutecharts.charts as ctc


# In[29]:


data = {'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
       'This week': [12, 10, 9, 9, 10, 3, 3],
        'Last week': [15, 12, 8, 9, 11, 4, 3]
       }
df_coffee = pd.DataFrame(data, columns = ['Day', 'This week', 'Last week'])


# In[5]:


chart = ctc.Radar('Cup of coffe consumed per day')
chart.set_options(
    labels=list(df_coffee['Day']),
    is_show_legend=True,
    legend_pos='upRight'
    )
chart.add_series('This Week', list(df_coffee['This week']))
chart.add_series('Last Week', list(df_coffee['Last week']))


# In[6]:


chart.render_notebook()


# In[ ]:




