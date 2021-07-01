# PDF generator

This project was built to enable PDF generation from a Python dictionary.
Currently, there are 2 different templates that can be generated from 2 hardcoded dictionaries.

### Tech stack

- Python 3.9.4
- Django 3.2.4
- WeasyPrint 52.5
- Chart.js 3.4.0

### Quick start

- run `pip3 install -r requirements.txt` to install necessary packages
- `brew install python3 cairo pango gdk-pixbuf libffi` - needed to enable WeasyPrint (https://weasyprint.readthedocs.io/en/stable/install.html#macos)
- go to `/myapp` directory and run `python manage.py runserver 8080` to start the app on port 8080
- go to `http://localhost:8080/` where you will see the `index.html` page
- click on the appropriate button to generate a chosen PDF template
- functions `generate_pdf` and `generate_pdf2` currently return JSON response but can return the binary representation of PDF (just change this line: `JsonResponse({"encoded": encoded})` into `return binary_representation`)

Templates were based on examples mentioned in the spec below, however, there might be slight changes due the lack of some data in the dictionaries or charts library limitations.
https://docs.google.com/document/d/1TvC4tBhagMxqcWELHwKiSPQznG2fdhSYwchce0pwXRQ/edit#
