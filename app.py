import streamlit as st
from sqlalchemy.orm import Session
from models import SessionLocal, Literature, init_db
from utils.ai_functions import generate_summary, generate_outline
from utils.extraction import extract_metadata
import os
import uuid
from PyPDF2 import PdfReader
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the database
init_db()

# Create a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Set Streamlit page configuration
st.set_page_config(page_title="AI Assistant for Scientific Literature", layout="wide")

# Sidebar navigation
st.sidebar.title("Menu")
options = ["Upload Literature", "View Literature", "Edit Literature"]
choice = st.sidebar.radio("Navigate", options)

# Helper function to save uploaded PDF
def save_pdf(uploaded_file):
    unique_filename = str(uuid.uuid4()) + "_" + uploaded_file.name
    save_path = os.path.join("data", unique_filename)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return save_path

# Upload Literature
if choice == "Upload Literature":
    st.header("Upload Scientific Literature")

    with st.form("upload_form"):
        uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
        submit = st.form_submit_button("Upload")

    if submit:
        if uploaded_file is not None:
            # Ensure data directory exists
            if not os.path.exists("data"):
                os.makedirs("data")

            # Save the file
            file_path = save_pdf(uploaded_file)

            # Extract text from PDF
            reader = PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text()

            # Extract metadata
            metadata = extract_metadata(text)
            title = metadata.get("title", "Unknown Title")
            authors = metadata.get("authors", "Unknown Authors")
            publication_date = metadata.get("publication_date", "Unknown Date")
            location = metadata.get("location", "Unknown Location")
            abstract = metadata.get("abstract", "")

            # Generate summary and outline using AI
            with st.spinner("Generating summary and outline..."):
                summary = generate_summary(text)
                outline = generate_outline(text)

            # Save to database
            db = next(get_db())
            literature = Literature(
                title=title,
                authors=authors,
                publication_date=publication_date,
                location=location,
                abstract=abstract,
                summary=summary,
                outline=outline,
                file_path=file_path
            )
            db.add(literature)
            db.commit()
            db.refresh(literature)

            st.success(f"Uploaded and processed: {title}")

# View Literature
elif choice == "View Literature":
    st.header("View Uploaded Literature")
    db = next(get_db())
    literatures = db.query(Literature).all()

    if not literatures:
        st.info("No literature uploaded yet.")
    else:
        for lit in literatures:
            with st.expander(f"{lit.title} by {lit.authors}"):
                cols = st.columns(2)
                cols[0].markdown(f"**Publication Date:** {lit.publication_date}")
                cols[1].markdown(f"**Location:** {lit.location}")
                st.markdown(f"**Abstract:** {lit.abstract}")
                st.markdown(f"**Summary:** {lit.summary}")
                st.markdown(f"**Outline:** {lit.outline}")
                st.download_button(
                    label="Download PDF",
                    data=open(lit.file_path, "rb").read(),
                    file_name=os.path.basename(lit.file_path),
                    mime="application/pdf"
                )

                # Option to delete
                delete = cols[0].button("Delete", key=f"delete_{lit.id}")
                if delete:
                    confirm = st.warning("Are you sure you want to delete this entry?")
                    if st.button("Confirm Delete", key=f"confirm_delete_{lit.id}"):
                        db.delete(lit)
                        db.commit()
                        st.success("Deleted successfully.")
                        st.experimental_rerun()

# Edit Literature
elif choice == "Edit Literature":
    st.header("Edit Literature Entries")
    db = next(get_db())
    literatures = db.query(Literature).all()

    if not literatures:
        st.info("No literature to edit.")
    else:
        literature_titles = [f"{lit.title} by {lit.authors}" for lit in literatures]
        selected = st.selectbox("Select Literature to Edit", literature_titles)

        if selected:
            selected_lit = next((lit for lit in literatures if f"{lit.title} by {lit.authors}" == selected), None)
            if selected_lit:
                with st.form("edit_form"):
                    title = st.text_input("Title", value=selected_lit.title)
                    authors = st.text_input("Authors", value=selected_lit.authors)
                    publication_date = st.text_input("Publication Date", value=selected_lit.publication_date)
                    location = st.text_input("Location", value=selected_lit.location)
                    abstract = st.text_area("Abstract", value=selected_lit.abstract)
                    summary = st.text_area("Summary", value=selected_lit.summary)
                    outline = st.text_area("Outline", value=selected_lit.outline)

                    save_changes = st.form_submit_button("Save Changes")

                if save_changes:
                    selected_lit.title = title
                    selected_lit.authors = authors
                    selected_lit.publication_date = publication_date
                    selected_lit.location = location
                    selected_lit.abstract = abstract
                    selected_lit.summary = summary
                    selected_lit.outline = outline

                    db.commit()
                    st.success("Literature entry updated successfully.")