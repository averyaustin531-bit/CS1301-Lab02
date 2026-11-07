# This creates the main landing page for the Streamlit application.
# Contains an introduction to the project and guide users to other pages.

# Import Streamlit
import streamlit as st

# st.set_page_config() is used to configure the page's appearance in the browser tab.
# It's good practice to set this as the first Streamlit command in your script.
st.set_page_config(
    page_title="Homepage",  # The title that appears in the browser tab
    page_icon="🏡",         # An emoji that appears as the icon in the browser tab
)

st.image("images/music_banner.jpg", use_container_width=True)

# WELCOME PAGE TITLE
st.title("Your ZIP Code Has a Playlist! 🎶")

# INTRODUCTORY TEXT
st.write("""

This website is designed to collect and visualize data about music across different U.S. regions.

I collected 80 Apple Music chart entries from eight U.S. cities, organized into four regions: Northeast, South, Midwest, West. The bar chart shows genre counts across all eight cities: New York City, Philadelphia, Atlanta, Nashville, Chicago, Detroit, Los Angeles, and Seattle. The pie chart lets visitors choose a region and compare its genre breakdown. The data comes from Apple Music's Top 25 City Playlists, using the first 10 entries from each on Friday October 23, 2026.

As a few last disclaimers:
* The "Latin" music genre combines several musical styles for this comparison.
* Despite the title, my data compares selected cities, rather than individual Zip Codes.
You can navigate to the different pages using the sidebar on the left.

How to use this website:
- *Survey Page*: Submit your music preferences and listening habits.
- *Visuals Page*: Go here to see the data visualized in different graphs.

This project is part of CS 1301's Lab 2.
""")

# OPTIONAL: ADD AN IMAGE
# 1. Navigate to the 'images' folder in your Lab02 directory.
# 2. Place your image file (e.g., 'welcome_image.png') inside that folder.
# 3. Uncomment the line below and change the filename to match yours.
#
st.image("images/music_banner2.jpg", use_container_width=True)

