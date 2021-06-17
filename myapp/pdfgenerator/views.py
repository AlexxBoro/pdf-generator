from django.http import HttpResponse
from django.http import HttpResponse
from django.template import loader
from weasyprint import HTML, CSS
import tempfile


def index(request):
    return HttpResponse("PDF generator app!")


def generate_pdf(request):
    """Generate pdf."""
    # Model data
    # people = [
    #     {"name": "Ola", "surname": "B", "age": "29"},
    #     {"name": "Basia", "surname": "K", "age": "25"},
    # ]

    # Rendered
    html_string = loader.render_to_string("pdfgenerator/pdf.html")

    html = HTML(string=html_string)
    # result = html.write_pdf()

    html.write_pdf(
        "./pdfs/test.pdf", stylesheets=[CSS(string="body { font-size: 16px }")]
    )

    # Creating http response
    response = HttpResponse(content_type="application/pdf;")
    response["Content-Disposition"] = "inline; filename=list_people.pdf"
    response["Content-Transfer-Encoding"] = "binary"

    # with tempfile.NamedTemporaryFile(delete=True) as output:
    #     output.write(result)
    #     output.flush()
    #     output = open(output.name, "r")
    #     response.write(output.read())

    return HttpResponse(html_string)
    # return response
