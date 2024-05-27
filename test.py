import streamlit as st
import time
from openai import OpenAI

#############################################################################
client = OpenAI(organization=st.secrets["organization"],
                api_key=st.secrets["api_key"])
#############################################################################

st.write(st.secrets["assist_id"])
