# Click With Caution - Scam Analysis Tool

This Streamlit application analyzes text, PDF documents, and images for potential scam indicators using Google's Gemini 1.5 Pro model.

## Features

-   **Text Analysis:** Enter text directly into the application for analysis.
-   **File Uploads:** Upload text (.txt), PDF (.pdf), or image (PNG, JPG, JPEG) files for analysis.
-   **Scam Detection:** Utilizes Gemini 1.5 Pro to identify potential scam indicators.
-   **JSON Output:** Provides analysis results in a structured JSON format, including:
    -   `is_scam`: "Yes, it is likely a scam" or "No, not likely to be a scam".
    -   `confidence`: A numerical confidence level (0 to 1).
    -   `explanation`: A brief explanation of the analysis.
-   **User-Friendly Interface:** Clean and intuitive Streamlit interface.
-   **Custom Styling:** Custom CSS for improved visual presentation.

## Prerequisites

-   Python 3.6+
-   Streamlit
-   Google Generative AI (genai)
-   python-dotenv
-   pypdf (for PDF support)
-   Pillow (PIL) (for image support)

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install streamlit google-generativeai python-dotenv pypdf pillow
    ```

4.  **Set up environment variables:**

    -   Create a `.env` file in the project directory.
    -   Add your Google API key to the `.env` file:

        ```
        GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
        ```

    -   Replace `YOUR_GOOGLE_API_KEY` with your actual API key.

## Usage

1.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

    (Replace `app.py` with the name of your python file)

2.  **Interact with the application:**

    -   Enter text into the text area.
    -   Upload a text, PDF, or image file.
    -   Click the "Analyze" button.
    -   View the analysis results in the output container.

## Dependencies

-   `streamlit`: For creating the web application.
-   `google-generativeai`: For interacting with the Gemini API.
-   `python-dotenv`: For loading environment variables.
-   `pypdf`: For reading and extracting text from PDF files.
-   `pillow`: For image file handling.
-   `re`: For regular expression matching.
-   `json`: For JSON parsing.
-   `io`: For handling file input/output.

## Notes

-   Ensure you have a valid Google API key and that it is correctly configured in your `.env` file.
-   The accuracy of the scam detection depends on the Gemini 1.5 Pro model's capabilities.
-   Large files may take longer to process.
-   Install the required dependencies before running the application.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bug fixes, feature requests, or improvements.
