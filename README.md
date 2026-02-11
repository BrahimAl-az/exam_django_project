# Django Exam Project

## Project Overview
This project is a Django-based web application containing two applications:
1.  **`user_data`**: Handles user input, storage, and retrieval.
2.  **`api_data`**: Fetches and displays data from an external API.

## What will the User Expect?

From this project, the user can expect:

### 1. Interactive Data Entry (User App)
-   **Functionality**: A clean form to submit feedback or user details (Name, Email, Message).
-   **Persistence**: Data submitted is saved to a local SQLite database and persists across page reloads.
-   **Feedback Loop**: Submitted data is immediately listed below the form, confirming successful storage.

### 2. External Data Integration (API App)
-   **Real-time Fetching**: Navigate to the "External Data" tab to see live data fetched from `jsonplaceholder.typicode.com`.
-   **Error Handling**: If the API is down, the user sees a graceful error message instead of a crash.

### 3. Modern Aesthetic
-   **Visuals**: A "Dark Mode" inspired interface with gradients, glass-morphism effects (blur), and the modern "Outfit" typeface.
-   **Responsiveness**: The layout adapts to different screen sizes.

### 4. Deployment Check
-   **Current Status**: Running locally.
-   **URL**: `http://127.0.0.1:8000/`

## How to Run
1.  Ensure you have Python installed.
2.  Install dependencies:
    ```bash
    pip install django requests
    ```
3.  Run the server:
    ```bash
    python manage.py runserver
    ```
4.  Open `http://127.0.0.1:8000/` in your browser.
