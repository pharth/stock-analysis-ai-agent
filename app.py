import warnings
warnings.filterwarnings('ignore')

import streamlit as st

from pathlib import Path
import datetime
import os
import sys
import io

st.subheader(":robot_face: Stock Analysis Ai Agent")

os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'

with st.sidebar:
    
    with st.expander(label='User Inputs', expanded=False):

        OPENAI_API_KEY = st.text_input("OPENAI API KEY", key="key1", type="password")
        os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

        SERPER_API_KEY = st.text_input("SERPER API KEY", key="key2", type="password",help="Allows the Agents to do Google Search")
        os.environ["SERPER_API_KEY"] = SERPER_API_KEY

        temperature = st.slider(label='Temperature',min_value=0.0,max_value=2.0,value=0.0,step=0.1,help='Lesser value means less randomness in the output and makes output reproducible.')
        
        company = st.text_input(label='Company Name',value='AAPL')

        start_date = st.date_input(label='Start Date',value=datetime.date(2024,1,1))

        end_date = st.date_input(label='End Date',value=datetime.date.today())

        
    analyze_button = st.button(label='Analyze')

    reset_button = st.button(label='Reset', type='primary')


  

    st.write('[Get your Serper API key](https://serper.dev/)')

    st.write('[Get your OpenAI API key](https://platform.openai.com/account/api-keys)')

    

if reset_button:
    st.rerun()

if analyze_button:

    if len(OPENAI_API_KEY)>0 and len(SERPER_API_KEY)>0:

        with st.spinner('Waiting for output...'):

            try:

                from crew import run_crew
                            
                inputs = {
                    'stock': company,
                    'start_date': str(start_date),
                    'end_date' : str(end_date),
                }

                original_stdout = sys.stdout
                sys.stdout = io.StringIO()

                result = run_crew(inputs=inputs,temperature=temperature)

                verbose = sys.stdout.getvalue()
                sys.stdout = original_stdout

                with st.expander(label='Verbose',expanded=False):
                    st.markdown(verbose)

                with st.expander(label='Final Result',expanded=True):
                    st.markdown(result)

            except Exception as e:

                st.error(e)

    else:

        st.info('Please enter your OPENAI_API_KEY and SERPER_API_KEY!')