FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    texlive-latex-base \
    texlive-latex-extra \
    texlive-lang-cyrillic \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY demo demo
RUN pip install dmitritsiu-latex-lib pdflatex

CMD python -m demo /artifacts/input.tex /artifacts/output.pdf