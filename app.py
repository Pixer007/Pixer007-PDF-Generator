import streamlit as st
from fpdf import FPDF

# Function to generate PDF
def generate_pdf(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    for key, value in data.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True, align='L')
    
    return pdf

# Streamlit App Layout
st.title("PDF Generator App")
st.write("Fill in the details below to generate a PDF.")

# Create a form for user input
with st.form("input_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Generate PDF")

# Process the form submission
if submitted:
    if name and email and message:
        user_data = {
            "Name": name,
            "Email": email,
            "Message": message,
        }
        
        # Generate PDF
        pdf = generate_pdf(user_data)
        pdf_output = "generated_document.pdf"
        pdf.output(pdf_output)
        
        # Display download link
        with open(pdf_output, "rb") as file:
            st.download_button(
                label="Download PDF",
                data=file,
                file_name="generated_document.pdf",
                mime="application/pdf",
            )
    else:
        st.error("Please fill out all fields.")

