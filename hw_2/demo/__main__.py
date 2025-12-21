# Во вложенном пакете, чтоб не было подозрения что локально импортнул библиотеку
import sys
from typing import TextIO

from dmitri_latex.latex_lib import create_document, generate_image, generate_table
from pdflatex import PDFLaTeX


def generate_doc_and_write(io: TextIO):
    my_table = [
        ["№", "Language", "Description"],
        [1, "Scala", "Sigma based language"],
        [2, "Java", "Coffee language CRUD CRUD"],
        [3, "Python", "no comment"],
    ]

    my_image = "/artifacts/image.jpg"  # Path in docker

    doc = create_document(
        "\\section{Моя картинка}",
        generate_image(my_image, caption="This is a random image stolen from the 5th hw!"),
        "\\section{Моя таблица}",
        generate_table(my_table),
    )

    io.write(doc)


def render_pdf(in_file: str, out_file: str):
    pdfl = PDFLaTeX.from_texfile(in_file)
    pdf, _, _ = pdfl.create_pdf()

    with open(out_file, "wb") as out:
        out.write(pdf)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        generate_doc_and_write(sys.stdout)
    else:
        render_pdf(sys.argv[1], sys.argv[2])
