import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Set up data
data = {
    "Year": ["2021", "2017", "2013", "2010", "2007"],
    "Winner": ["Amarjeet Sohi", "Don Iveson", "Don Iveson", "Stephen Mandel", "Stephen Mandel"],
    "Percentage": [45.05, 73.6, 62.2, 55.23, 65.8]
}

df = pd.DataFrame(data)

# Streamlit app
st.title("Edmonton Mayoral Election Results (2007–2021)")
st.markdown("This chart shows the vote percentage of the winning mayoral candidate in Edmonton over the last five elections.")

# Create bar chart
fig = go.Figure(data=[
    go.Bar(
        x=df["Year"],
        y=df["Percentage"],
        text=df["Winner"],
        textposition='outside',
        marker_color='steelblue'
    )
])

# Update layout
fig.update_layout(
    yaxis=dict(title="Winning Vote Percentage", range=[0, 100]),
    xaxis=dict(title="Election Year"),
    title="Winning Mayoral Candidates in Edmonton (2007–2021)",
    template="plotly_white"
)

# Display chart
st.plotly_chart(fig, use_container_width=True)
