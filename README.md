
# Watchful Eye LA

A web-based crime data visualization and reporting tool for Los Angeles. Users can explore past crimes filtered by type, location, and weapon—plus visualize results on a real-time Leaflet.js map.

---

## Project Overview

**Watchful Eye LA** is an interactive web application built with Flask and SQLAlchemy that connects to a normalized MySQL database hosted on Google Cloud Platform (GCP). It enables users to:

- Search crime records using multiple filters (crime type, LAPD division, weapon)
- Submit mock crime reports via web forms
- Display filtered results dynamically in an HTML table
- Plot relevant results as markers on an interactive map

---

## Technologies Used

- **Backend:** Python, Flask, SQLAlchemy
- **Frontend:** HTML, CSS, Jinja2 Templates, Leaflet.js
- **Database:** MySQL (normalized and hosted on GCP)
- **Cloud:** Google Cloud Platform (Cloud SQL)

---

## My Role

This was a collaborative effort, but I took the lead on full-stack development and database interaction:

- Designed and implemented the **entire querying backend**, including complex SQLAlchemy queries for all filter combinations
- Handled all **frontend/backend integration** using Jinja2 templates and Flask routes
- Contributed significantly to **schema normalization decisions**, ensuring efficient joins and scalable queries
- Developed the **homepage filtering logic**, map plotting system, and coordinated integration with our GCP-hosted database
- in /doc I wrote two of the advanced queries and had input in the proposal 

My teammates contributed meaningfully by:

- **Setting up and managing our GCP database**
- **Helping clean and upload real LAPD crime data**
- Assisting with schema design and troubleshooting

---


- All data is public LAPD crime data, used for academic purposes.
- Mapping uses **Leaflet.js** and OpenStreetMap tiles.
- You can modify the query logic inside `__init__.py` for more advanced filtering.
