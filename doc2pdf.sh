#!/bin/sh
export HOME=/tmp/&&\
cd /tmp/doc2pdf/&&\
soffice --headless --convert-to pdf --outdir /tmp/doc2pdf/ file.doc&&\
pdftk file.pdf background /var/www/web_doc2pdf/header.pdf output file_bg.pdf&&\
pdftk /var/www/web_doc2pdf/cover.pdf file_bg.pdf output final.pdf

