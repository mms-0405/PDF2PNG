from pdf2image import convert_from_path
pdf = "C:/Users/12705/Desktop/Visa/boarding-pass.pdf"
img = convert_from_path(pdf)
for i in range(len(img)):
    img[i].save('page'+str(i)+'.png')