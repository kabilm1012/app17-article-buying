from fpdf import FPDF


def create_pdf(name, price):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt="Receipt nr.1", ln=1)
    pdf.cell(w=50, h=8, txt=f"Article: {name}", ln=1)
    pdf.cell(w=50, h=8, txt=f"Price: {price}", ln=1)

    pdf.output("receipt.pdf")
    print("PDF receipt generated successfully!")