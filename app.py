import streamlit as st
from fpdf import FPDF
from datetime import datetime

def generate_nda_pdf(type_of_nda, name, address):
    # Create PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_font("Arial", "B", size=14)
    pdf.cell(200, 10, txt="Non-Disclosure Agreement", ln=True, align="C")

    # Line Break
    pdf.ln(10)

    # Body
    pdf.set_font("Arial", size=12)
    today_date = datetime.now().strftime("%B %d, %Y")
    content = f"""
This Non-Disclosure Agreement (the "Agreement") is entered into on {today_date}.

BETWEEN:
{name}
Address: {address}

AND:
App Synergies of 186 Malvern Avenue, Harrow, HA2 9HD, UK, hereinafter referred to as the "Disclosing Party".

Purpose:
The NDA is applicable to the {type_of_nda.upper()} category of disclosure.

The parties agree as follows:
1. Confidential Information...
2. Obligation of Confidentiality...
3. Terms of Agreement...

Signed by:
[Signature Line]
"""
    pdf.multi_cell(0, 10, txt=content)

    # Save PDF
    pdf_file = f"NDA_{type_of_nda}_{name.replace(' ', '_')}.pdf"
    pdf.output(pdf_file)
    return pdf_file

# Streamlit App
st.title("NDA PDF Generator")

# Type of NDA Selection
type_of_nda = st.selectbox("Select NDA Type", ["India", "ROW"])

# Input Fields
name = st.text_input("Enter Your Name")
address = st.text_area("Enter Your Address")

if st.button("Generate PDF"):
    if not name or not address:
        st.error("Please fill in all fields.")
    else:
        pdf_file = generate_nda_pdf(type_of_nda, name, address)
        with open(pdf_file, "rb") as file:
            st.download_button(
                label="Download NDA PDF",
                data=file,
                file_name=pdf_file,
                mime="application/pdf"
            )
