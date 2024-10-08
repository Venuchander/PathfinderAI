# PathfinderAI

PathfinderAI is a web application that generates a comprehensive learning roadmap for any topic from beginner to advanced levels. The roadmap includes suggested blog articles and YouTube videos, structured in clear stages (Beginner, Intermediate, Advanced). The application is built using Streamlit, and it leverages Google's generative AI to create the roadmap. Additionally, users can download the roadmap as a PDF.

## Features

- **Interactive Web Interface**: Enter a topic and get a detailed learning roadmap instantly.
- **AI-Powered Content Generation**: Utilizes Google's generative AI to create custom roadmaps.
- **PDF Download**: Allows users to download the generated roadmap as a PDF for offline use.

## Installation

### Prerequisites

- Python 3.8 or higher
- Streamlit
- FPDF
- Python-dotenv

### Steps

1. Clone this repository:
    ```bash
    git clone https://github.com/Venuchander/PathfinderAI.git
    cd PathfinderAI
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your environment variables:
    - Rename the `.env.example` file to `.env`.
    - Open the `.env` file and replace `YOUR_API_KEY` with your actual Google Generative AI API key:
      ```bash
      api_key=your_actual_api_key_here
      ```

4. Run the application:
    ```bash
    streamlit run main.py
    ```

## Usage

1. Open the application in your browser (it will usually run at `http://localhost:8501`).
2. Enter the topic you want to learn about in the input field.
3. The app will generate a learning roadmap with resources organized by level.
4. You can download the roadmap as a PDF by clicking the "Download Roadmap as PDF" button.

## Dependencies

- [Streamlit](https://streamlit.io/)
- [FPDF](http://www.fpdf.org/)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)
- [Google Gemini AI](https://ai.google.dev/gemini-api)

## Contributors

<div style="display: flex; align-items: center;">
    <a href="https://github.com/imsuryya" style="display: inline-block; margin-right: 40px;">
        <img src="https://github.com/imsuryya.png" alt="Suryya" style="width: 50px; height: 50px; border-radius: 50%;">
    </a>
    <a href="https://github.com/Venuchander" style="display: inline-block;">
        <img src="https://github.com/Venuchander.png" alt="Venuchander" style="width: 50px; height: 50px; border-radius: 50%;">
    </a>
</div>

## License

This project is licensed under the MIT License.
