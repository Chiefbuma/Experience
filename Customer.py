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

with st.container(key="logo"):

        Con_label2 = "Date"
        cols = st.columns(6)

        with cols[0]:
            st.image("logo.png", width=150)

        st.markdown(
                    """
                    <style>
                    /* Apply styles to the form container */
                    div[data-testid="stForm"] {
                        border: 2.0px solid black; /* Bold border */
                        padding: 10px;
                        border-radius: 10px;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True
                )
    
# Display the image from the local folder
with card_container():
    
    with st.container(key="stcontainer"):
        
        coll = st.columns([1,8])
        with coll[1]:
            with ui.element("div", className="flex gap-2", key="buttons_group1"):
                    ui.element(
                    "button", 
                    text="Diabetes Self-Assessment: Could You Be at Risk?", 
                    className="btn btn-primary", 
                    key="btn1",
                    style={
                        "width": "500px",       # Adjust the width
                        "height": "80px",       # Adjust the height
                        "background-color": "#04315b",  # Set a custom background color (green in this case)
                        "color": "white",       # Text color
                        "border-radius": "8px", # Optional: round corners
                        "border": "none",  
                        "font-size": "20px",     # Increase font size
                        "font-weight": "bold"# Remove border if needed
                    }
                )
            with coll[0]:
                with ui.element("div", className="flex gap-2", key="buttons_group2"):
                        ui.element(
                        "button", 
                        text="1.", 
                        className="btn btn-primary", 
                        key="btn1",
                        style={
                            "width": "50px",       # Adjust the width
                            "height": "80px",       # Adjust the height
                            "background-color": "#04315b",  # Set a custom background color (green in this case)
                            "color": "white",       # Text color
                            "border-radius": "8px", # Optional: round corners
                            "border": "none",  
                            "font-size": "20px",     # Increase font size
                            "font-weight": "bold"# Remove border if needed
                        }
                    )
                    

                


        # with open("docs/introduction.md", "r") as f:
#     st.markdown(f.read())

# ui.date_picker()

st.header("Streamlit Shadcn UI")
ui.badges(badge_list=[("shadcn", "default"), ("in", "secondary"), ("streamlit", "destructive")], class_name="flex gap-2", key="main_badges1")
st.caption("A Streamlit component library for building beautiful apps easily. Bring the power of Shadcn UI to your Streamlit apps!")
st.caption("Get started with pip install streamlit-shadcn-ui")
ui.element("image", src="C:\ProgramData\MySQL\DATASCIENCE\Experience\sunrise.jpg", alt="Description of Image", width=200, key="img1")

    


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



st.subheader("Alert Dialog")
import pandas as pd

# Create a dictionary with the data
data = {
    "AREA": [
        "Diabetes", "Diabetes", "Diabetes", "Diabetes", 
        "Pressure", "Pressure", "Pressure", "Pressure",
        "Respiratory", "Respiratory", "Respiratory", "Respiratory",
        "Asthma", "Asthma", "Asthma", "Asthma",
        "CNS", "CNS", "CNS", "CNS"
    ],
    "ASSES": [
        "1. Do you frequently feel very thirsty, even after drinking water?(Excessive thirst is a common sign of high blood sugar levels.)",
        "2. Do you experience frequent urination, especially during the night?(Frequent trips to the bathroom may indicate diabetes.)",
        "3. Do you often feel tired or fatigued, even after adequate rest?(Chronic fatigue can be linked to elevated blood sugar levels.)",
        "4. Do you often feel hungry, even after eating?(Persistent hunger, especially right after a meal, could be a sign of diabetes.)",
        "1. Do you often experience headaches, particularly in the morning?",
        "2. Have you felt dizzy or lightheaded recently without any obvious cause?(Dizziness can sometimes be linked to elevated blood pressure levels.)",
        "3. Do you experience chest pain or a sensation of pressure in your chest?(Chest discomfort can be a sign of heart problems associated with high blood pressure.)",
        "4. Is your family history filled with cases of high blood pressure or heart disease?(A family history of hypertension increases your own risk.)",
        "1. Have you recently developed a persistent cough, producing green, yellow, or bloody mucus?(A productive cough may indicate pneumonia or a serious respiratory infection.)",
        "2. Are you experiencing shortness of breath or difficulty breathing, even when resting?(Shortness of breath is a common symptom of pneumonia or severe flu.)",
        "3. Are you experiencing sharp or stabbing chest pain when you cough or take a deep breath?(Chest pain may be a sign of pneumonia or pleurisy (inflammation of the lungs).)",
        "4. Are you experiencing muscle aches, body pain, or headaches?(Flu often presents with body aches, while pneumonia can cause general discomfort.)",
        "1. Do you often experience shortness of breath, especially during physical activity?(This could be a sign of uncontrolled asthma.)",
        "2. Do you frequently have a tight feeling in your chest?(Chest tightness is a common asthma symptom.)",
        "3. Have you had recurring coughing fits, particularly at night or early in the morning?",
        "4. Have you noticed that cold air or changes in weather make your breathing worse?(Asthma can be triggered by weather changes or cold air.)",
        "1. Do you often experience persistent headaches or migraines that disrupt your daily activities?(Chronic headaches can be a sign of neurological conditions, including migraines or brain disorders.)",
        "2. Have you recently noticed muscle weakness, numbness, or tingling in your hands, legs, or feet?(These sensations may indicate nerve damage or disorders like multiple sclerosis (MS).)",
        "3. Do you have difficulty maintaining balance or experience frequent dizziness?(Balance issues can be related to problems with the brain or nervous system.)",
        "4. Do you ever have episodes of confusion, disorientation, or changes in awareness?(These symptoms could point to seizures, epilepsy, or other neurological conditions.)"
    ],
    "Rating": [None] * 20  # Placeholder for Rating column, which you can fill later
}

# Create DataFrame
df = pd.DataFrame(data)

# Show the DataFrame
st.write(df)




