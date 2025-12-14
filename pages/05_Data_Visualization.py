import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Visualization",
    layout="wide",
    initial_sidebar_state="expanded"
)


#Read the csv
PATH = "data/african_classified_dpdp.csv"
df = pd.read_csv(PATH)


st.title("Data Vizualization")


st.subheader("Map of Pageviews Per Capita")
st.write("The following visualization shows the number of pageviews per capita (per 1000000)\
         for each year (2023-2024)")

#adding the per capita column to the dataframe

# make year
df["year"] = pd.to_datetime(df["date"]).dt.year

# views per country-year
views_cty_yr = (
    df.groupby(["country", "year"], as_index=False)["views"]
      .sum()
)

# population per country-year 
pop_cty_yr = (
    df.groupby(["country", "year"], as_index=False)["population"]
      .first()
)

# region per country-year 
region_cty_yr = (
    df.groupby(["country", "year"], as_index=False)["region"]
      .first()
)

# mergind df
merged_df = (views_cty_yr
             .merge(pop_cty_yr, on=["country", "year"], how="left")
             .merge(region_cty_yr, on=["country", "year"], how="left")
)

# per-capita (per 1,000,000 people)
merged_df["views_per_capita"] = (merged_df["views"] / merged_df["population"]) * 1_000_000

merged_df = merged_df[["country", "year", "region", "population", "views", "views_per_capita"]]

merged_df = merged_df.dropna(subset=["region"])


#User controls
regions = st.multiselect("Filter by region", df["region"].unique(), default=df["region"].unique())

filtered_df = merged_df[merged_df["region"].isin(regions)]


#Plotly Chloropleth

global_max = filtered_df["views_per_capita"].max()
global_max = (int(global_max / 100) + 1) * 100



fig = px.choropleth(
    filtered_df,
    locations="country",
    locationmode="country names",
    color="views_per_capita",
    range_color=[0, global_max],
    animation_frame="year",
    hover_name="country",
    color_continuous_scale="Viridis",
    title=f"Choropleth Map of {"views_per_capita (1M)".replace('_', ' ').title()}",
    height=700, width=1000
)

# Show borders
fig.update_geos(
    showcountries=True, countrycolor="black",
    showcoastlines=True, coastlinecolor="gray",
    showland=True, landcolor="lightgray"
)

st.plotly_chart(fig, use_container_width=True)


st.divider()
st.header("Most Viewed Articles Per Country")

year_select = st.selectbox(
    "Choose a year:",
    sorted(df["year"].dropna().unique())
)

df_year = df[df["year"] == year_select].copy()

if df_year.empty:
    st.warning("No rows available for that year.")
else:
    country = st.selectbox(
        "Choose a country:",
        sorted(df_year["country"].dropna().unique())
    )

    country_df = df_year[df_year["country"] == country].copy()

    top25 = (
        country_df.groupby("article", as_index=False)["views"]
        .sum()
        .sort_values("views", ascending=False)
        .head(25)
    )

    st.write(f"Most Viewed Articles in **{country}** for **{year_select}**")
    st.dataframe(top25[["article", "views"]])