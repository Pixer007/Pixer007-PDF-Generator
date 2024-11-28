import streamlit as st
from fpdf import FPDF
from datetime import datetime

class StyledPDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "AppSynergies Pvt Ltd", ln=True, align="L")
        self.set_font("Arial", size=10)
        self.cell(0, 10, "186 Malvern Avenue, Harrow, HA2 9HD, UK", ln=True, align="L")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", size=10)
        self.cell(0, 10, "Contact: info@appsynergies.com | +91-9967067419", align="C")

def generate_nda_pdf(name, address, nda_type):
    pdf = StyledPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    today_date = datetime.now().strftime("%B %d, %Y")

    # Title
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Non-Disclosure Agreement", ln=True, align="C")
    pdf.ln(10)

    # Date
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Date: {today_date}", ln=True)
    pdf.ln(5)

    # Parties
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Parties:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=f"""
This Agreement is entered into between:
1. {name}, residing at {address} ("Receiving Party").
2. AppSynergies Pvt Ltd, 186 Malvern Avenue, Harrow, HA2 9HD, UK ("Disclosing Party").
    """)
    pdf.ln(5)

    # Purpose
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Purpose:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=f"""
This NDA applies to the confidentiality obligations related to the {nda_type.upper()} category.
    """)
    pdf.ln(5)

    # Confidentiality Obligations
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Confidentiality Obligations:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt="""
1. The Receiving Party shall not disclose any confidential information.
2. Confidential information must be used solely for the purpose specified.
3. The Agreement shall remain in effect for 3 years unless terminated earlier.
    """)
    pdf.ln(5)

    # Signatures
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Signatures:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Receiving Party: {name}", ln=True)
    pdf.cell(0, 10, "Disclosing Party: AppSynergies Pvt Ltd", ln=True)

    # Save PDF
    file_name = f"NDA_{name.replace(' ', '_')}.pdf"
    pdf.output(file_name)
    return file_name

# Streamlit App
st.title("NDA Generator")
nda_type = st.selectbox("Select NDA Type", ["India", "ROW"])
name = st.text_input("Enter Your Name")
address = st.text_area("Enter Your Address")

if st.button("Generate NDA"):
    if not name or not address:
        st.error("Please fill in all fields.")
    else:
        pdf_file = generate_nda_pdf(name, address, nda_type)
        with open(pdf_file, "rb") as file:
            st.download_button("Download NDA PDF", file, file_name=pdf_file, mime="application/pdf")
