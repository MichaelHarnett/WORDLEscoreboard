import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from plotly import tools
from plotly.subplots import make_subplots

from multiapp import MultiApp


from pages import home, family, savages

app = MultiApp()

st.markdown("<h1 style='text-align: center; color: white;'>WORDLE SCOREBOARD</h1>", unsafe_allow_html=True)


st.markdown("""
# WORDLE SCOREBOARD

I followed [Chanin Nantasenamat's](https://github.com/dataprofessor) guide to multi-page streamlit apps [here](https://github.com/dataprofessor/multi-page-app). This is the credit he posted on his app:
This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
""")

# Add all your application here
app.add_app("Who's asking?", home.app)
app.add_app('Family', family.app)
app.add_app('Savages', savages.app)
# The main app
app.run()


# st.info(st.markdown("""
# # WORDLE SCOREBOARD

# I followed [Chanin Nantasenamat's](https://github.com/dataprofessor) guide to multi-page streamlit apps [here](https://github.com/dataprofessor/multi-page-app). This is the credit he posted on his app:
# This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
# """))

st.info('I followed [Chanin Nantasenamat\'s](https://github.com/dataprofessor) guide to multi-page streamlit apps [here](https://github.com/dataprofessor/multi-page-app). This is the credit he posted on his app:  \n"This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4)." ')