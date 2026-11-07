
# This creates the page for displaying data visualizations.

import streamlit as st
import json
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import os

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visuals",
    page_icon="📈",
)

st.image("images/music_banner.jpg", use_container_width=True)

# PAGE TITLE
st.title("Data Visualizations 📈")


# ==========================================
# PART 1: GRAPHS FROM data.json
# ==========================================

with open("data.json", "r") as file:
    data = json.load(file)

songs = data["data_points"]
genre_counts = {}

for song in songs:
    genre = song["genre"]

    if genre in genre_counts:
        genre_counts[genre] += 1
    else:
        genre_counts[genre] = 1

genre_table = pd.DataFrame({
    "Genre": list(genre_counts.keys()),
    "Count": list(genre_counts.values())
})

st.write(genre_table)

st.bar_chart(genre_table, x="Genre", y="Count")

regions = ["Northeast", "South", "Midwest", "West"]

selected_region = st.selectbox(
    "Choose a region",
    regions,
    key="selected_region"
)

region_counts = {}

for song in songs:
    if song["region"] == selected_region:
        genre = song["genre"]

        if genre in region_counts:
            region_counts[genre] += 1
        else:
            region_counts[genre] = 1

region_table = pd.DataFrame({
    "Genre": list(region_counts.keys()),
    "Count": list(region_counts.values())
})

st.write(region_table)

fig = px.pie(
    region_table,
    names="Genre",
    values="Count",
    title="Genre Breakdown: " + selected_region
)

st.plotly_chart(fig)


# ==========================================
# PART 2: GRAPHS FROM data.csv
# ==========================================

st.divider()
st.header("Survey Results 🎵")

# Check whether the CSV file exists.
if os.path.exists("data.csv") and os.path.getsize("data.csv") > 0:

    survey_data = pd.read_csv("data.csv")

    # Check that the required columns exist.
    if "Category" in survey_data.columns and "Value" in survey_data.columns:

        # Convert Value into numbers.
        survey_data["Value"] = pd.to_numeric(
            survey_data["Value"],
            errors="coerce"
        )

        # Remove rows with missing information.
        survey_data = survey_data.dropna(
            subset=["Category", "Value"]
        )

        if not survey_data.empty:

            # ==================================
            # VISUALIZATION 1: STATIC BAR CHART
            # ==================================

            st.subheader("Average Listening Hours by Genre")

            # Calculate average listening hours for each genre.
            average_hours = survey_data.groupby(
                "Category"
            )["Value"].mean().reset_index()

            # Create the Matplotlib chart.
            fig, ax = plt.subplots()

            ax.bar(
                average_hours["Category"],
                average_hours["Value"]
            )

            ax.set_title("Average Daily Music Listening by Genre")
            ax.set_xlabel("Music Genre")
            ax.set_ylabel("Average Hours Per Day")

            plt.xticks(rotation=45)
            plt.tight_layout()

            st.pyplot(fig)

            plt.close(fig)


            # ==================================
            # VISUALIZATION 2: DYNAMIC PIE CHART
            # ==================================

            st.subheader("Explore Music Genre Popularity")

            # Count responses for each genre.
            genre_counts = survey_data["Category"].value_counts()

            # Initialize session state.
            if "top_genres" not in st.session_state:
                st.session_state.top_genres = min(
                    3, len(genre_counts)
                )

            # Let users select how many genres to display.
            selected_number = st.slider(
                "How many top genres would you like to display?",
                min_value=1,
                max_value=len(genre_counts),
                key="top_genres"
            )

            # Select the most popular genres.
            selected_genres = genre_counts.head(
                selected_number
            ).copy()

            # Combine remaining genres into Other.
            if len(genre_counts) > selected_number:

                other_count = genre_counts.iloc[
                    selected_number:
                ].sum()

                selected_genres.loc["Other"] = other_count

            # Create the Plotly pie chart.
            fig2 = px.pie(
                names=selected_genres.index,
                values=selected_genres.values,
                title="Survey Responses by Music Genre"
            )

            st.plotly_chart(fig2)


            # ==================================
            # EXTRA CREDIT: SUMMARY STATISTICS
            # ==================================

            st.subheader("Listening Statistics")

            # Get the selected genres.
            chosen_categories = genre_counts.head(
                selected_number
            ).index

            selected_data = survey_data[
                survey_data["Category"].isin(chosen_categories)
            ]["Value"]

            # Calculate mean and median.
            mean_hours = selected_data.mean()
            median_hours = selected_data.median()

            col1, col2 = st.columns(2)

            col1.metric(
                "Mean Listening Hours",
                f"{mean_hours:.2f}"
            )

            col2.metric(
                "Median Listening Hours",
                f"{median_hours:.2f}"
            )

        else:
            st.warning("There is no valid survey data to display.")

    else:
        st.error("Your data.csv file needs Category and Value columns.")

else:
    st.warning(
        "No survey responses yet! Visit the Survey page to add data."
    )

st.image("images/music_banner2.jpg", use_container_width=True)
