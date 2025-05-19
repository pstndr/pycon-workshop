import streamlit as st
import pandas as pd
import plotly.express as px

from utils.platform.header import same_old


same_old()

# Titolo della pagina
st.title("📊 Data Visualization Dashboard")
st.write("Upload a CSV file and explore your data with interactive visualizations!")

# Caricamento del file CSV
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    # Caricamento dei dati
    df = pd.read_csv(uploaded_file)
    st.write("### Preview of the Dataset")
    st.dataframe(df)

    # Selezione delle colonne per la visualizzazione
    st.write("### Select Columns for Visualization")
    numeric_columns = df.select_dtypes(include=["float", "int"]).columns
    if len(numeric_columns) < 2:
        st.warning("The dataset must have at least two numeric columns for visualization.")
    else:
        (sx, mid, dx) = st.columns(3)
        x_axis = sx.selectbox("Select X-axis", options=numeric_columns)
        y_axis = mid.selectbox("Select Y-axis", options=numeric_columns)
        chart_type = dx.selectbox("Select Chart Type", ["Scatter Plot", "Line Chart", "Bar Chart"])

        # Generazione del grafico
        st.write("### Visualization")
        if chart_type == "Scatter Plot":
            fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{chart_type} of {x_axis} vs {y_axis}")
        elif chart_type == "Line Chart":
            fig = px.line(df, x=x_axis, y=y_axis, title=f"{chart_type} of {x_axis} vs {y_axis}")
        elif chart_type == "Bar Chart":
            fig = px.bar(df, x=x_axis, y=y_axis, title=f"{chart_type} of {x_axis} vs {y_axis}")

        st.plotly_chart(fig, use_container_width=True)

        # Opzione per scaricare il grafico come immagine
        st.write("### Download Chart")
        st.download_button(
            label="Download Chart as HTML",
            data=fig.to_html(),
            file_name="chart.html",
            mime="text/html",
        )
else:
    st.info("Please upload a CSV file to get started.")
