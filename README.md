# Hackathon PSU: Group Movie Recommender

## Project Overview

This project is a web-based movie recommender system designed for groups, built for the Hackathon PSU competition. It allows users to create accounts, input their movie preferences, and receive personalized movie recommendations based on group consensus. The system utilizes KMeans clustering to generate a group preference vector and the TMDB API to fetch movie data. User accounts and preferences are stored in a SQLite database.

## Features

* **User Account Management:**
    * Account creation and login.
    * Storage of user preferences.
* **Group Preference Aggregation:**
    * Uses KMeans clustering to generate a group preference vector from individual user preferences.
    * Handles diverse group preferences effectively.
* **Movie Recommendations:**
    * Fetches movie data from the TMDB API.
    * Provides recommendations based on the group preference vector.
    * Displays movie titles, genre information, and ratings.
* **Data Storage:**
    * SQLite database for storing user accounts and preferences.
* **Web Interface:**
    * Front-end website built with Flask for user interaction.

## Technologies Used

* **Python:** Main programming language.
* **Flask:** Web framework for the front-end.
* **Scikit-learn (sklearn):** KMeans clustering for preference vector generation.
* **TMDB API:** For retrieving movie data.
* **SQLite:** Database for data storage.
* **NumPy:** For numerical computations.
* **Pandas:** For data manipulation.
* **Pathlib:** For path manipulation.

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone [repository_url]
    cd [project_directory]
    ```

2.  **Install dependencies:**

    ```bash
    pip install Flask scikit-learn numpy pandas requests
    ```

3.  **Set up TMDB API Key:**

    * Obtain an API key from TMDB ([https://www.themoviedb.org/documentation/api](https://www.themoviedb.org/documentation/api)).
    * Store the API key in a secure location and update the code accordingly.

4.  **Database setup:**
    * The sqlite database will be created upon first run of the flask application.

5.  **Run the Flask application:**

    ```bash
    python app.py
    ```

    * Replace `app.py` with the name of your Flask application file.

6.  **Access the website:**

    * Open your web browser and navigate to `http://127.0.0.1:5000/` (or the address displayed in the terminal).

## Collaborators

* Franklin Collazo
* Roberto Ramirez Galan
* Andrew Sutton
* Bruno Rodriguez
* Adam Manowski

## Hackathon PSU

This project was developed for the Hackathon PSU competition.

## Future Improvements

* Implement user review and rating systems.
* Add more advanced recommendation algorithms.
* Improve the user interface and experience.
* Add more robust error handling.
* Implement user search functionality.
* Implement movie sorting functionality.
* Implement genre filtering.
* Implement user friend system, and group creation.
