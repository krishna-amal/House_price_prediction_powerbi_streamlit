import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="HOUSE PRICE DASHBOARD",page_icon=":house:",layout="wide")

df = pd.read_csv("_All_Cities_Cleaned.csv")
df["bedroom"].astype("int")
df1=df.fillna(0)


#st.dataframe(df)

st.sidebar.header("Please choose your preferences here!")
CITY=st.sidebar.selectbox("select your city: ",options=df1["city"].unique())

BEDROOMS=st.sidebar.selectbox("Select number of bedroms: ",options=df1["bedroom"].unique())

BATHROOMS=st.sidebar.selectbox("Select number of bathroms ",options=df1["bathroom"].unique())

SELLER_TYPE=st.sidebar.selectbox("Select seller_type",options=df1["seller_type"].unique())

PROPERTY_TYPE=st.sidebar.selectbox("select property_type",options=df1["property_type"].unique())

FURNITURE_TYPE=st.sidebar.selectbox("select furnish_type",options=df1["furnish_type"].unique())

df_selection=df1.query("city == @CITY & bedroom == @BEDROOMS & bathroom == @BATHROOMS  & seller_type == @SELLER_TYPE & property_type == @PROPERTY_TYPE & furnish_type == @FURNITURE_TYPE")

#st.dataframe(df_selection)

st.title(":house:house sales dashboard")
st.markdown("######")

Avg_price=df_selection["price"].mean()

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("AVERAGE PRICE OF HOUSE!")
    st.subheader(f"{Avg_price:,}")


graph_price=(df1.groupby(by=["city"]).mean()[["price"]].sort_values(by="price"))
fig=px.bar(graph_price,x="price",y=graph_price.index,orientation="h",
    title="<b>Average house price per city</b>",
    color_discrete_sequence=["#0083B8"] * len(df1),
    template="plotly_white",
)

fig.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

#st.plotly_chart(fig)

fig_df=(df.groupby(by=["city"]).mean()[["price"]].sort_values(by="price"))
fig_2=px.bar(fig_df,x="price",y=fig_df.index,orientation="h",
    title="<b>Average house price per proprty type</b>",
    color_discrete_sequence=["#0083B8"] * len(fig_df),
    template="plotly_white",
)

#st.plotly_chart(fig_2)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig, use_container_width=True)
right_column.plotly_chart(fig_2, use_container_width=True)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)