import os
from google.cloud import documentai_v1 as documentai

# Set up authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\surya\OneDrive\Desktop\xxx\xxx.json'

# Initialize Document AI client
client = documentai.DocumentProcessorServiceClient()

# Your project and processor details
PROJECT_ID = ''
LOCATION = 'us'
PROCESSOR_ID = ''

# Full resource name of the processor
RESOURCE_NAME = f"projects/{PROJECT_ID}/locations/{LOCATION}/processors/{PROCESSOR_ID}"

def process_document(file_path):
    # Read the file into memory
    with open(file_path, "rb") as file:
        file_content = file.read()

    # Create the raw document object
    raw_document = documentai.RawDocument(
        content=file_content,
        mime_type='application/pdf'
    )

    # Configure the process request
    request = documentai.ProcessRequest(
        name=RESOURCE_NAME,
        raw_document=raw_document
    )

    try:
        # Use the Document AI client to process the document
        response = client.process_document(request=request)

        # Print the document text
        print(f"Document text:\n{response.document.text}")

        # Print the summary (if available)
        if response.document.text_styles:
            for style in response.document.text_styles:
                if style.text_anchor.content == "SUMMARY":
                    start = style.text_anchor.text_segments[0].start_index
                    end = style.text_anchor.text_segments[0].end_index
                    print(f"\nSummary:\n{response.document.text[start:end]}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Usage
if __name__ == "__main__":
    
    document_path = r"C:\Users\surya\Downloads\xxx.pdf"
    process_document(document_path)