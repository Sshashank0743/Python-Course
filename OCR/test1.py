import pypdfium2 as pdfium
import os
pdf = pdfium.PdfDocument("Balidaanam_.pdf")
version = pdf.get_version()  # get the PDF standard version
n_pages = len(pdf)  # get the number of pages in the document
savedDirectory = "one"
print("Total Pages :"+str(n_pages))
page_indices = [i for i in range(n_pages)]  # all pages
renderer = pdf.render(
    pdfium.PdfBitmap.to_pil,
    page_indices = page_indices,
    scale = 300/72,  # 300dpi resolution
)
for i, image in zip(page_indices, renderer):
#print(savedDirectory+str(i)+".jpg")
    image.save(savedDirectory+str(i)+".jpg")
    os.rename(savedDirectory+str(i)+".jpg",savedDirectory+str(i)+".png")