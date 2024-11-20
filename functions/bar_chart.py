import pandas as pd
import streamlit as st
import plotly.express as px

def bar_chart(dataset, x_axis, y_axis, title, x_axis_title, y_axis_title):
    # Create the bar chart
    fig = px.bar(
        dataset,
        x=x_axis,
        y=y_axis,
        title=title,
    )
    # Customize the layout
    fig.update_layout(
        xaxis_title=x_axis_title,
        yaxis_title=y_axis_title,
        template='plotly_white',  # Optional: clean white theme
    )
    # Display the chart in Streamlit
    return st.plotly_chart(fig, use_container_width=True)
