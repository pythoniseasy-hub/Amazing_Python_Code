from fpdf import FPDF
pdf = FPDF()
pdf = FPDF(orientation = 'L', format='A5')
pdf.add_page()
#===================Adding Page Border Through Line===================
pdf.line(5, 5, 205, 5)  # Top Line
pdf.line(5, 5, 5, 143)  # Left Line
pdf.line(5, 143,205,143)    # Bottom Line
pdf.line(205, 5,205,143)    # Right Line
#====================Adding Some Candidate Details====================
pdf.set_font("Arial", style = 'UBI',size=18)
pdf.cell(200, 10, txt="Identity Card",align="C")
pdf.set_font("Arial", style = 'B',size=12)
pdf.text(x=15,y=50, txt="Name")
pdf.set_font("Arial",size=11)
pdf.text(x=50,y=50,txt=":Gagan Aggarwal")
pdf.set_font("Arial", style = 'B',size=12)
pdf.text(x=15,y=60, txt="Course")
pdf.set_font("Arial",size=11)
pdf.text(x=50,y=60,txt=":MCA (Master of Computer Application)")
pdf.set_font("Arial", style = 'B',size=15)
pdf.text(x=150,y=40, txt="Candidate Pic")
pdf.image(name="Gagan.jpg",x = 140, y = 45, w = 50, h = 50, type ='jpg')
pdf.set_font("Arial", style = 'B',size=12)
pdf.text(x=15,y=70, txt="College")
pdf.set_font("Arial",size=11)
pdf.text(x=50,y=70,txt=":RBMI Greater Noida")
pdf.set_font("Arial", style = 'B',size=12)
pdf.text(x=15,y=80, txt="Address")
pdf.set_font("Arial",size=11)
pdf.text(x=50,y=80,txt=":Gamma 2, Greater Noida")
pdf.set_font("Arial", style = 'B',size=12)
pdf.text(x=15,y=90, txt="Profile")
pdf.set_font("Arial",size=11)
pdf.text(x=50,y=90,txt=":Python Developer")
pdf.set_font("Arial", style = 'B',size=12)
pdf.text(x=15,y=100, txt="Email")
pdf.set_font("Arial",size=11)
pdf.text(x=50,y=100,txt=":gaggarwal124@gmail.com")
pdf.set_font("Arial", style = 'B',size=12)
pdf.text(x=15,y=110, txt="Blog")
pdf.set_font("Arial",size=11)
pdf.text(x=50,y=110,txt=":https://mystudy247.blogspot.com/")

pdf.output("Identity Card.pdf")