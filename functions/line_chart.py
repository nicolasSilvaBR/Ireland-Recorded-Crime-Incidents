import pandas as pd
import streamlit as st
import plotly.express as px

def line_chart(dataset, x_axis, y_axis, title, x_axis_title, y_axis_title):
    """
    Creates and displays a line chart in Streamlit.

    Parameters:
    - dataset: pd.DataFrame -> The data source for the chart.
    - x_axis: str -> The column to use for the x-axis.
    - y_axis: str -> The column to use for the y-axis.
    - title: str -> Title of the chart.
    - x_axis_title: str -> Title of the x-axis.
    - y_axis_title: str -> Title of the y-axis.
    """
    # Create a line chart using Plotly Express
    fig = px.line(
        dataset,
        x=x_axis,
        y=y_axis,
        markers=True,  # Add markers at data points
        title=title
    )
    # Customize the layout
    fig.update_layout(
        xaxis_title=x_axis_title,
        yaxis_title=y_axis_title,
        template='plotly_white'  # Set a clean theme
    )
    # Display the chart in Streamlit
    return st.plotly_chart(fig, use_container_width=True)
