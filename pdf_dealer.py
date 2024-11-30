import os
from pypdf import PdfReader, PdfWriter

pdf_folder = "pdf_files/"
path = os.path.join(os.getcwd(),pdf_folder)
file_format = '.pdf'

class Reader:
    def __init__(self,path,folder,format):
        self.path = path
        self.folder = folder
        self.format = format

    def read_pdf(self):
        user_choice = input('input name of file: ')
        if not user_choice.endswith(self.format):
            user_choice = user_choice + self.format
        if os.path.exists(os.path.join(self.path,user_choice)):
            reader = PdfReader(f"{self.folder}{user_choice}")
            for i in range(len(reader.pages)):
                page = reader.pages[i]
                text = page.extract_text()
                print(text)
        else:
            print("couldn't read file")

    def merge_pdf(self):
        merger = PdfWriter()
        while True:
            user = input('input file you want to merge and q to exit merging : ')
            if user == 'q':
                break
            user = user + self.format
            if not os.path.exists(os.path.join(self.path,user)):
                print('no such file')
                continue
            merger.append(os.path.join(self.path,user))
        merged_file_name = input('input the name of merged file: ')
        merger.write(os.path.join(self.path,merged_file_name+self.format))
        merger.close()
        print('done')

    def split_pdf(self):
        user = input('input the pdf you want to split: ')
        if not user.endswith(self.format):
            user = user + self.format
        if not os.path.exists(os.path.join(path,user)):
            print('no such file')
        reader = PdfReader(os.path.join(path,user))
        for i in range(len(reader.pages)):
            writer = PdfWriter()
            writer.add_page(reader.pages[i])
            with open(f"{self.path}page_{i + 1}.pdf", "wb") as output_pdf:
                writer.write(output_pdf)
        print('done')

    @staticmethod
    def user_choice():
        while True:
            print("1) to read pdf")
            print("2) to merge pdf")
            print("3) to split pdf")
            choice = input('input choice : ')
            if "1"<=choice<="3":
                return choice

p_obj = Reader(path, pdf_folder, file_format)
print('pdf handler')
user = p_obj.user_choice()
if user == "1":
    p_obj.read_pdf()
elif user == "2":
    p_obj.merge_pdf()
elif user == "3":
    p_obj.split_pdf()