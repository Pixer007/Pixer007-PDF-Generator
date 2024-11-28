import streamlit as st
from fpdf import FPDF
from datetime import datetime

class NDA_PDF(FPDF):
    def header(self):
        # Add company header
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "AppSynergies Pvt Ltd", ln=True, align="L")
        self.set_font("Arial", size=10)
        self.multi_cell(0, 5, "D-1602, Orchid Suburbia,\nLink Road, Kandivali West,\nMumbai 400067", align="L")
        self.ln(5)

    def footer(self):
        # Add footer
        self.set_y(-15)
        self.set_font("Arial", size=10)
        self.cell(0, 10, "Contact: info@appsynergies.com | +91-9967067419", align="C")

    def add_section(self, title, content):
        # Add section with title and content
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.set_font("Arial", size=12)
        self.multi_cell(0, 10, content)
        self.ln(5)

def generate_nda_pdf(client_name, client_address, nda_type):
    pdf = NDA_PDF()
    pdf.add_page()

    # Title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "NON-DISCLOSURE AGREEMENT", ln=True, align="C")
    pdf.ln(10)

    # Intro Section
    today_date = datetime.now().strftime("%B %d, %Y")
    intro = f"""
This Non-Disclosure Agreement executed on {today_date}, is entered into by and between:
1. {client_name} with the address of {client_address} ("Party A").
2. AppSynergies Pvt Ltd, D-1602, Orchid Suburbia, Link Road, Kandivali West, Mumbai 400067 ("Party B").

AppSynergies and {client_name} may be referred to collectively as the "Parties".
    """
    pdf.add_section("Introduction:", intro)

    # Type of Agreement
    pdf.add_section("Type of Agreement:", f"The Agreement is {nda_type.upper()}.")

    # Confidentiality Definition
    confidentiality = """
In this Agreement, "Confidential Information" refers to any information with commercial value, including technical and non-technical data, financial details, customer lists, or any proprietary details shared by either party.
    """
    pdf.add_section("Definition of Confidentiality:", confidentiality)

    # Obligations
    obligations = """
The Parties shall maintain strict confidentiality and shall not disclose any information without prior written consent. All shared records must be returned upon request.
    """
    pdf.add_section("Obligations:", obligations)

    # Term
    pdf.add_section("Term:", "The confidentiality obligations shall remain in effect for 3 years or until written release by the disclosing party.")

    # Signatures
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Signatures:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Party A: {client_name}", ln=True)
    pdf.cell(0, 10, "Party B: Sneha Shukla, AppSynergies Pvt Ltd", ln=True)

    # Save PDF
    file_name = f"NDA_{client_name.replace(' ', '_')}.pdf"
    pdf.output(file_name)
    return file_name

# Streamlit App
st.title("NDA Generator")
nda_type = st.selectbox("Select NDA Type", ["India", "ROW"])
client_name = st.text_input("Enter Client Name")
client_address = st.text_area("Enter Client Address")

if st.button("Generate NDA"):
    if not client_name or not client_address:
        st.error("Please fill in all fields.")
    else:
        pdf_file = generate_nda_pdf(client_name, client_address, nda_type)
        with open(pdf_file, "rb") as file:
            st.download_button("Download NDA PDF", file, file_name=pdf_file, mime="application/pdf")
