import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from IPython.display import display
import calendar
import numpy as np
from IPython.display import HTML
import streamlit_option_menu as option_menu
import streamlit_shadcn_ui as ui
from local_components import card_container
from streamlit_shadcn_ui import slider, input, textarea, radio_group, switch
from dateutil.relativedelta import relativedelta
import streamlit as st
import streamlit_shadcn_ui as ui
import pandas as pd
import numpy as np
from local_components import card_container
from streamlit_shadcn_ui import slider, input, textarea, radio_group, switch


    
# Expander section with adjusted width
with st.expander("DOWNLOAD PREVIOUS MONTH"):
    
    # Create a styled container for expander content
    st.markdown(
        """
        <div style="width: 250px;">
            <p>Here you can download the data from the previous month.</p>
        </div>
        """, 
        unsafe_allow_html=True
        
    )
    # Display the image from the local folder
    st.image("sunrise.jpg", caption="Sunrise by the mountains", width=200)
    
    
    


# with open("docs/introduction.md", "r") as f:
#     st.markdown(f.read())

# ui.date_picker()

st.header("Streamlit Shadcn UI")
ui.badges(badge_list=[("shadcn", "default"), ("in", "secondary"), ("streamlit", "destructive")], class_name="flex gap-2", key="main_badges1")
st.caption("A Streamlit component library for building beautiful apps easily. Bring the power of Shadcn UI to your Streamlit apps!")
st.caption("Get started with pip install streamlit-shadcn-ui")


with ui.element("div", className="flex gap-2", key="buttons_group1"):
    ui.element("button", text="Get Started", className="btn btn-primary", key="btn1")
    ui.element("link_button", text="Github", url="https://github.com/ObservedObserver/streamlit-shadcn-ui", variant="outline", key="btn2")

st.subheader("Dashboard")

ui.tabs(options=['Overview', 'Analytics', 'Reports', 'Notifications'], default_value='Overview', key="main_tabs")

ui.date_picker(key="date_picker1")

cols = st.columns(3)
with cols[0]:
    # with ui.card():
    #     ui.element()
    ui.card(title="Total Revenue", content="$45,231.89", description="+20.1% from last month", key="card1").render()
with cols[1]:
    ui.card(title="Subscriptions", content="+2350", description="+180.1% from last month", key="card2").render()
with cols[2]:
    ui.card(title="Sales", content="+12,234", description="+19% from last month", key="card3").render()




ui_result = ui.button("Button", key="btn")
st.write("UI Button Clicked:", ui_result)


# Slider Component
slider_value = slider(default_value=[20], min_value=0, max_value=100, step=2, label="Select a Range", key="slider1")
st.write("Slider Value:", slider_value)

# Input Component
input_value = input(default_value="Hello, Streamlit!", type='text', placeholder="Enter text here", key="input1")
st.write("Input Value:", input_value)

# Textarea Component
textarea_value = textarea(default_value="Type your message here...", placeholder="Enter longer text", key="textarea1")
st.write("Textarea Value:", textarea_value)

# Radio Group Component
radio_options = [
    {"label": "Option A", "value": "A", "id": "r1"},
    {"label": "Option B", "value": "B", "id": "r2"},
    {"label": "Option C", "value": "C", "id": "r3"}
]
radio_value = radio_group(options=radio_options, default_value="B", key="radio1")
st.write("Selected Radio Option:", radio_value)

# Switch Component
switch_value = switch(default_checked=True, label="Toggle Switch", key="switch1")
st.write("Switch is On:", switch_value)

st.subheader("Alert Dialog")
trigger_btn = ui.button(text="Trigger Button", key="trigger_btn")
ui.alert_dialog(show=trigger_btn, title="Alert Dialog", description="This is an alert dialog", confirm_label="OK", cancel_label="Cancel", key="alert_dialog1")