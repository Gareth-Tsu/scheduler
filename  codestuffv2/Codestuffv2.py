import os
import re
import shutil
import pypdf

cwd = os.getcwd()
imgdir = 'C:/Users/Garet/PycharmProjects/WorkingDir/ codestuffv2'

for file in os.listdir(imgdir):
    if file.endswith('.pdf'):
        shutil.copy2(os.path.join(imgdir, file), cwd)

f = open('Find_the_Phone_Number.pdf', 'rb')
pdf_read = pypdf.PdfReader(f)
all_text = []
for page in pdf_read.pages:
    all_text.append(page.extract_text())

pattern = r'\d{3}\W\d{3}\W\d{4}'

for text in all_text:
    result = re.search(pattern, text)
    if result:
        print(result.group())



