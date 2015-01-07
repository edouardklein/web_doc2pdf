#!env sh
cd /tmp/doc2pdf/&&\
soffice --headless --convert-to pdf file.doc&&\
pdftk file.pdf background /var/www/web_doc2pdf/header.pdf output file_bg.pdf&&\
pdftk /var/www/cover.pdf file_bg.pdf output final.pdf

