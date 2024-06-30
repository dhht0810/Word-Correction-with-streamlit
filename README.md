## Word Correction App with Levenshtein Distance and Streamlit

This app provides real-time word correction suggestions based on Levenshtein distance, a popular metric for measuring the similarity between strings. It's built using Streamlit, a Python library for creating interactive web apps.

**Features:**

-   **Real-time correction suggestions:** As you type, the app suggests potential corrections for misspelled words.
-   **Levenshtein distance:** The app calculates the Levenshtein distance between the user's input and dictionary words to determine the most likely corrections.
-   **Streamlit interface:** The app presents a user-friendly interface for text input and correction suggestions.

**Requirements:**

-   Python 3.x ([https://www.python.org/downloads/](https://www.python.org/downloads/))
-   Streamlit ([https://docs.streamlit.io/](https://docs.streamlit.io/))
-   A dictionary file (you can use the existing vocab.txt)

**Installation:**

1.  Clone this repository or download the files.
    
2.  Install required libraries:
    
    Bash
    
    ```
    pip install streamlit
    
    ```
    
    
    
3.  Place your dictionary file in the same directory as the app script (`main.py`).
    

**Usage:**

1.  Run the app:
    
    Bash
    
    ```
    streamlit run app.py
    
    ```

  2.  Type in the text box. The app will display suggestions for misspelled words below the input field.
    

**Explanation:**

1.  **main.py:** This script contains the core logic of the app.
    -   Imports necessary libraries (`streamlit`).
    -   Loads the dictionary file.
    -   Defines a function to calculate Levenshtein distance between strings.
    -   Creates a Streamlit app layout with a text input field and a section to display correction suggestions.
    -   When the user types, the app calls the Levenshtein distance function to find the closest matches in the dictionary and displays them as suggestions.

**Customization:**

-   You can modify the dictionary file to include domain-specific terms or filter out unwanted words.
-   You can adjust the Levenshtein distance threshold to control the sensitivity of suggestions.
-   You can extend the app to provide additional features like context-aware suggestions or part-of-speech tagging for improved accuracy.
