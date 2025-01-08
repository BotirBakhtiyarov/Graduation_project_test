import re

def extract_metadata(text: str) -> dict:
    metadata = {}

    # Example patterns (these may need to be adjusted based on the literature format)
    title_pattern = r"Title:\s*(.*)"
    authors_pattern = r"Authors?:\s*(.*)"
    date_pattern = r"Publication Date:\s*(.*)"
    location_pattern = r"Location:\s*(.*)"
    abstract_pattern = r"Abstract:\s*(.*?)\n\n"

    title = re.search(title_pattern, text, re.IGNORECASE | re.DOTALL)
    authors = re.search(authors_pattern, text, re.IGNORECASE | re.DOTALL)
    publication_date = re.search(date_pattern, text, re.IGNORECASE | re.DOTALL)
    location = re.search(location_pattern, text, re.IGNORECASE | re.DOTALL)
    abstract = re.search(abstract_pattern, text, re.IGNORECASE | re.DOTALL)

    metadata['title'] = title.group(1).strip() if title else "Unknown Title"
    metadata['authors'] = authors.group(1).strip() if authors else "Unknown Authors"
    metadata['publication_date'] = publication_date.group(1).strip() if publication_date else "Unknown Date"
    metadata['location'] = location.group(1).strip() if location else "Unknown Location"
    metadata['abstract'] = abstract.group(1).strip() if abstract else ""

    return metadata