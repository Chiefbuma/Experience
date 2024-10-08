import streamlit as st
from st_supabase_connection import SupabaseConnection
from supabase import create_client, Client
import pandas as pd
from datetime import datetime, timedelta
from IPython.display import display
import calendar
import numpy as np
import plotly.express as px
from IPython.display import HTML
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.authentication_context import AuthenticationContext
import streamlit_option_menu as option_menu
import plotly.graph_objects as go
import supabase
import streamlit_shadcn_ui as ui
from local_components import card_container
from streamlit_shadcn_ui import slider, input, textarea, radio_group, switch
import main
from postgrest import APIError
from dateutil.relativedelta import relativedelta


import streamlit as st




with card_container():
    colm = st.columns([0.05,2,0.05])
    with colm[1]:
        # Display the image from the local folder
        st.image("sunrise.jpg", caption="Sunrise by the mountains", width=700)
    # Expander section with adjusted width
        with st.expander("DOWNLOAD PREVIOUS MONTH"):
            # Create a styled container for expander content
            st.markdown(
                """
                <div style="width: 200px;">
                    <p>Here you can download the data from the previous month.</p>
                </div>
                """, 
                unsafe_allow_html=True
            )