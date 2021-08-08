from ipywidgets.widgets import widget
import streamlit as st
import pandas as pd
from streamlit.proto.Image_pb2 import Image
from visualize import * 
st.title("IPL DATA ANALYSIS 2008-2020")
st.video("146.mp4")

sidebar=st.sidebar
sidebar.title("Devesh singh")
st.image("145.jpg")



df=pd.read_csv('ipl.csv')

st.header('Most wins in IPL')

st.plotly_chart(plotbar(df.groupby("winner").count().reset_index(),x="winner",y="id"))

st.subheader("## Mumbai Indians won most number of matches followed by Chennai Super Kings ##")

st.header('Most wins in Eleminator')

st.plotly_chart(plotbar(df.groupby("winner").count().reset_index(),x="winner",y="eliminator"))

st.header('Number of Matches played in each Stadium')

st.plotly_chart(plotbar(df.groupby("venue").count().reset_index(),x="id",y="venue"))

st.subheader("## Most number of IPL matches were played in Eden Gardens Stadium, Kolkata")

st.header('Top 5 Umpire')

st.plotly_chart(plotbar(df.groupby("umpire1").count().reset_index(),x="umpire1",y="id"))

st.header('Toss Decision of Team')

st.plotly_chart(plotbar(df.groupby("toss_winner").count().reset_index(),x="toss_winner",y="id"))

st.header('Top 5 Umpire_2')

st.plotly_chart(plotbar(df.groupby("umpire2").count().reset_index(),x="umpire2",y="id"))

st.header('Player of the Match')

st.plotly_chart(plotbar(df.groupby("player_of_match").count().reset_index(),x="player_of_match",y="id"))

st.subheader("## Chris Gayle won most Man of the Match Awards")

st.header("Number of matches played in each City")

st.plotly_chart(plotbar(df.groupby("city").count().reset_index(),x="city",y="id"))

st.subheader("## Most matches played in Mumbai")