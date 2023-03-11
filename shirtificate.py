#import fpdf2
from fpdf import FPDF


#Get the name of the student
name = input("Type in your name: ")


pdf = FPDF(orientation="p", unit="mm", format="A4")
pdf.add_page()
pdf.set_font('helvetica', 'B', size=45)

pdf.cell(h=45, align='C', w= 0, new_x='LEFT', new_y= 'NEXT', txt = "CS50 Shirtificate")

pdf.image("shirt.png", x= 'C', w=170)

pdf.set_font('helvetica', "B", size=23)

pdf.set_text_color(255,255,255)

pdf.text(x= 55, y= 115, txt = f"{name.title()} took CS50")




pdf.output("shirtificate.pdf")


