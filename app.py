import streamlit as st
from docx import Document
from io import BytesIO
from datetime import datetime

# Function to load the Word template
def load_template(file_path):
    return Document(file_path)

# Function to replace placeholders in the template
def replace_placeholders(doc, replacements):
    # Replace text in paragraphs
    for paragraph in doc.paragraphs:
        for key, value in replacements.items():
            if key in paragraph.text:
                for run in paragraph.runs:
                    if key in run.text:
                        run.text = run.text.replace(key, value)

    # Replace text in tables
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    for key, value in replacements.items():
                        if key in paragraph.text:
                            for run in paragraph.runs:
                                if key in run.text:
                                    run.text = run.text.replace(key, value)

# Streamlit app
def main():
    st.title("NDA Generator with Company Branding")
    st.markdown("Easily generate an NDA document with your company's branding and background.")

    # Sidebar input fields
    st.sidebar.header("Input Details")
    client_company_name = st.sidebar.text_input("Client Company Name", placeholder="Enter the company name")
    client_name_surname = st.sidebar.text_input("Client Full Name", placeholder="Enter the full name of the client")
    client_address = st.sidebar.text_area("Client Address", placeholder="Enter the client address")
    
    # Automatically fetch today's date
    today_date = datetime.now().strftime("%d-%m-%Y")
    agreement_date = st.sidebar.text_input("Agreement Date", value=today_date, placeholder="Enter the agreement date")

    agreement_type = st.sidebar.selectbox(
        "Type of Agreement",
        options=["Unilateral", "Mutual"]
    )

    if st.sidebar.button("Generate NDA"):
        # Load the Word template
        template_path = "NDA Template - INDIA 3.docx"  # Ensure this file is pre-designed with your background
        doc = load_template(template_path)

        # Define replacements
        replacements = {
            "__Client Company Name (Client Name) __": client_company_name,
            "________" : client_company_name,
            "__Client Address__": client_address,
            "10th September, 2023": agreement_date,
            "10-09-2023" : agreement_date,
            "Name Surname": client_name_surname,  # Fixes alignment by targeting runs
            "- Unilateral –": f"- {agreement_type} –",
        }

        # Replace placeholders
        replace_placeholders(doc, replacements)

        # Save the updated document to a BytesIO object
        output = BytesIO()
        doc.save(output)
        output.seek(0)

        # Allow the user to download the file
        st.success("NDA document generated successfully!")
        st.download_button(
            label="Download NDA",
            data=output,
            file_name=f"NDA_{client_company_name.replace(' ', '_')}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )

if __name__ == "__main__":
    main()
