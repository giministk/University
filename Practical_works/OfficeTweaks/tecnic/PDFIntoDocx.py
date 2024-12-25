from docx2pdf import convert
from pdf2docx import Converter


def pdf_to_docx(choice, docs):
        if int(choice) == 0:
            for i in list(docs.values()):
                docx_file = i[:-3] + 'docx'
                pdf_conv = Converter(i)
                pdf_conv.convert(docx_file)
                pdf_conv.close()
                print(f'Файл {i} успешно конвертирован')
        else:
            if type(docs) is dict:
                pdf_file = docs.get(int(choice))
                docx_file = pdf_file[:-3] + 'docx'
                pdf_conv = Converter(pdf_file)
                pdf_conv.convert(docx_file)
                pdf_conv.close()
                print(f'Файл {pdf_file} успешно конвертирован')
            else:
                for i in docs:
                    docx_file = i[:-3] + 'docx'
                    pdf_conv = Converter(i)
                    pdf_conv.convert(docx_file)
                    pdf_conv.close()
                    print(f'Файл {i} успешно конвертирован')


def docx_to_pdf(choice, docs):
        if int(choice) == 0:
            for i in list(docs.values()):
                pdf_file = i[:-4] + 'pdf'
                convert(i, pdf_file)
                print(f'Файл {i} успешно конвертирован')
        else:
            if type(docs) is dict:
                docx_file = docs.get(int(choice))
                pdf_file = docx_file[:-4] + 'pdf'
                convert(docx_file, pdf_file)
                print(f'Файл {docx_file} успешно конвертирован')
            else:
                for i in docs:
                    pdf_file = i[:-4] + 'pdf'
                    convert(i, pdf_file)
                    print(f'Файл {i} успешно конвертирован')