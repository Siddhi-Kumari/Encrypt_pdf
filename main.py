
from PyPDF2 import PdfFileWriter, PdfFileReader

out = PdfFileWriter()

file = PdfFileReader("Siddhi Kumari Resume (6).pdf")


num = file.numPages


for idx in range(num):

    page = file.getPage(idx)
    out.addPage(page)

password = "pass"

out.encrypt(password)
with open("Siddhi_encrypted.pdf", "wb") as f:

    out.write(f)