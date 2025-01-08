# AI Assistant for Scientific Literature

## Overview

The **AI Assistant for Scientific Literature** is a web-based application designed to streamline the management and analysis of scientific papers. Leveraging the power of Artificial Intelligence, this tool assists researchers, students, and academics in organizing their literature, extracting essential metadata, generating summaries, and creating structured outlines of scientific documents.

Built with Python and Streamlit for an intuitive frontend, and powered by OpenAI's GPT models for advanced text processing, this application aims to enhance the efficiency of the literature review process and support academic research endeavors.

## Features

- **Upload PDFs:** Easily upload scientific literature in PDF format.
- **Metadata Extraction:** Automatically extract key details such as title, authors, publication date, location, and abstract.
- **AI-Generated Summaries:** Generate concise summaries of the literature using OpenAI's GPT models.
- **Structured Outlines:** Obtain structured outlines outlining main sections like Introduction, Methods, Results, and Discussion.
- **Manage Literature Entries:** View, edit, and delete uploaded literature entries.
- **Download PDFs:** Download the original uploaded PDFs for offline access.

## Technologies Used

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Backend:** Python, SQLAlchemy
- **Database:** SQLite
- **AI Integration:** OpenAI's GPT (e.g., GPT-3.5-turbo, GPT-4)
- **PDF Processing:** PyPDF2
- **Environment Management:** python-dotenv
- **Others:** UUID, NLTK, pandas

## Project Structure

```
ai_assistant_scientific_literature/
├── app.py
├── models.py
├── database.db
├── requirements.txt
├── .env
├── utils/
│   ├── ai_functions.py
│   ├── extraction.py
│   └── summarization.py
└── data/
    └── (uploaded PDFs are stored here)
```

- **app.py:** Main Streamlit application handling user interactions.
- **models.py:** Database models and configuration using SQLAlchemy.
- **database.db:** SQLite database file.
- **requirements.txt:** Python dependencies.
- **.env:** Environment variables (e.g., OpenAI API key).
- **utils/:** Helper modules for AI functions and metadata extraction.
- **data/:** Directory to store uploaded PDF files.

## Installation

### Prerequisites

- Python 3.7 or higher
- Git

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/ai_assistant_scientific_literature.git
   cd ai_assistant_scientific_literature
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**

   Create a `.env` file in the root directory and add your OpenAI API key:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Initialize the Database:**

   Run the following command to create the SQLite database and required tables:

   ```bash
   python models.py
   ```

6. **Ensure Data Directory Exists:**

   Make sure the `data/` directory exists to store uploaded PDFs. If not, create it:

   ```bash
   mkdir data
   ```

## Usage

Run the Streamlit application using the following command:

```bash
streamlit run app.py
```

This will launch the app in your default web browser. Use the sidebar to navigate between uploading, viewing, and editing literature entries.

### Application Sections

1. **Upload Literature:**
   - Upload PDF files of scientific literature.
   - The app extracts metadata, generates summaries and outlines using AI.

2. **View Literature:**
   - View all uploaded literature entries.
   - Expand each entry to see detailed information and download the PDF.

3. **Edit Literature:**
   - Edit metadata, summaries, and outlines of existing literature entries.
   - Delete entries if necessary.

## Deployment

You can deploy this application using various platforms. Below is an example of deploying with Docker.

### Docker Deployment

1. **Build the Docker Image:**

   ```bash
   docker build -t ai_assistant_literature .
   ```

2. **Run the Docker Container:**

   ```bash
   docker run -d -p 8501:8501 ai_assistant_literature
   ```

3. **Access the App:**

   Open your browser and navigate to `http://localhost:8501`.

### Additional Deployment Options

- **Streamlit Sharing:** Quick and easy deployment for Streamlit apps.
- **Heroku:** Supports Python applications with straightforward deployment steps.
- **AWS/GCP/Azure:** For scalable and robust deployments with cloud infrastructure.
- **Others:** Any platform that supports Docker can be used for deployment.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. **Fork the Repository.**
2. **Create a New Branch:**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes:**

   ```bash
   git commit -m "Add your message here"
   ```

4. **Push to Your Fork:**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request:** Describe your changes and submit for review.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or support, please contact:

- **Email:** [your_email@example.com](mailto:your_email@example.com)
- **GitHub:** [yourusername](https://github.com/yourusername)

## Acknowledgements

- [OpenAI](https://openai.com/) for providing powerful language models.
- [Streamlit](https://streamlit.io/) for enabling easy web app development.
- [SQLAlchemy](https://www.sqlalchemy.org/) for database management.
- [PyPDF2](https://pypi.org/project/PyPDF2/) for PDF processing.

---

*Embark on your research journey with ease using the AI Assistant for Scientific Literature!*
