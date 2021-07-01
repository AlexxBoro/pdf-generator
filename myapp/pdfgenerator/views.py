from django.http import HttpResponse
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import base64
from weasyprint import HTML
from .dictionaries import input_data_1, input_data_2


def get_data(request):
    return JsonResponse({"input_data": input_data_1})


def index(request):
    html_string = loader.render_to_string("index.html", {"input_data": input_data_1})

    return HttpResponse(html_string)


@csrf_exempt
def generate_pdf(request):
    """Generate PDF 1."""

    # parsing 'request.body' from POST into JSON
    body = json.loads(request.body.decode("utf-8"))
    content = body

    bar_chart = content["bar_chart"]
    horizontal_bar_chart = content["horizontal_bar_chart"]
    pie_chart = content["pie_chart"]

    html_string = loader.render_to_string(
        "pdfgenerator/template_1.1.html",
        {"input_data": input_data_1},
    )
    html_string2 = loader.render_to_string(
        "pdfgenerator/template_1.2.html",
        {"input_data": input_data_1},
    )
    html_string3 = loader.render_to_string(
        "pdfgenerator/template_1.3.html",
        {"input_data": input_data_1, "bar_chart": bar_chart},
    )
    html_string4 = loader.render_to_string(
        "pdfgenerator/template_1.4.html",
        {
            "input_data": input_data_1,
            "horizontal_bar_chart": horizontal_bar_chart,
            "pie_chart": pie_chart,
        },
    )

    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    html2 = HTML(string=html_string2, base_url=request.build_absolute_uri())
    html3 = HTML(string=html_string3, base_url=request.build_absolute_uri())
    html4 = HTML(string=html_string4, base_url=request.build_absolute_uri())

    pdf1 = html.render()
    pdf2 = html2.render()
    pdf3 = html3.render()
    pdf4 = html4.render()

    # combining 4 pages into 1 PDF document
    val = []

    for doc in pdf1, pdf2, pdf3, pdf4:
        for p in doc.pages:
            val.append(p)

    binary_representation = pdf1.copy(val).write_pdf()
    encoded = base64.b64encode(binary_representation)
    encoded = encoded.decode("utf-8")

    return JsonResponse({"encoded": encoded})


def generate_pdf2(request):
    """Generate PDF 2."""

    html_string = loader.render_to_string(
        "pdfgenerator/template_2.html",
        {"input_data": input_data_2},
    )

    html = HTML(string=html_string, base_url=request.build_absolute_uri())

    binary_representation = html.write_pdf()
    encoded = base64.b64encode(binary_representation)
    encoded = encoded.decode("utf-8")

    return JsonResponse({"encoded": encoded})
