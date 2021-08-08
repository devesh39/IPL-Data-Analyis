import plotly.express as px
import plotly.graph_objects as go

def plotbar(df,x,y):
    return px.bar(data_frame=df,x=x,y=y)