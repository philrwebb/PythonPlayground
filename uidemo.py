import streamlit as st
import pandas as pd

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Header
st.title("CSV File Plotter")

# Sidebar
with st.sidebar:
    st.header("Upload and Plot")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Main
if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    # Show the DataFrame (optional)
    if st.checkbox("Show raw data"):
        st.write(df)

    # Select columns to plot
    columns = df.columns.tolist()
    selected_columns = st.multiselect("Select columns to plot", columns)

    if selected_columns:
        # Plotting
        st.subheader("Plotting Data")
        plt.figure(figsize=(10, 6))
        for col in selected_columns:
            plt.plot(df[col], label=col)
        plt.title("Plot")
        plt.xlabel("Index")
        plt.ylabel("Value")
        plt.legend()
        st.pyplot(plt)


# # Title for the app
# st.title("Streamlit Button Click Example")

# # Button
# if st.button("Click Me"):
#     # Text Area to display 'Hello, World!'
#     st.text_area("Output", "Hello, World!")
# else:
#     st.text_area("Output", "")

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.button("Button 1")

# with col2:
#     st.button("Button 2")

# with col3:
#     st.button("Button 3")

# container = st.container()
# container.write("This is inside the container")

# with container:
#     st.button("Inside Container")

# import streamlit as st

# # Header
# st.title("My Complex Layout")

# # Sidebar (Collapsible)
# with st.sidebar:
#     st.header("Sidebar")
#     st.write("This is a collapsible sidebar")

# # Main Content
# # Use st.columns to divide the space
# col1, col2 = st.columns([1, 4])

# # Left sidebar within main for more details (Collapsible)
# with col1:
#     with st.expander("More Details"):
#         st.write("You can put more details here")

# # Main content
# with col2:
#     st.header("Main Content")
#     st.write("This is where you'd put the main content")

# # Footer
# st.write("---")  # Visual separator
# st.write("Footer: More information and links can go here")

