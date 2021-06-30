from django.http import HttpResponse
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import base64
from weasyprint import HTML

input_data_1 = {
    "name": "Wolt: Tue paikallisia ravintoloita",
    "used_budget": 6562,
    "budget": 3000,
    "creators": 24,
    "submissions": 48,
    "applications": 242,
    "reach": 232874,
    "engagement": 17786,
    "impressions": 252791,
    "cpm": 25.96,
    "cpe": 0.37,
    "engagement_percentage": 10.28,
    "followers": 271389,
    "audience_female_share": 0.65,
    "top_posts": [
        {
            "awareness": 100.0,
            "compatibility": 100.0,
            "virality": 51.6,
            "engagement": 50.0,
            "image": "pdfgenerator/images/woman_1.jpeg",
            "creator": {
                "name": "Jutta Häkämies",
                "username": "juttaemmii",
                "image": "pdfgenerator/images/avatar_1.jpeg",
            },
        },
        {
            "awareness": 77.8,
            "compatibility": 60.96,
            "virality": 100.0,
            "engagement": 56.87,
            "image": "pdfgenerator/images/woman_2.jpeg",
            "creator": {
                "name": "Rita Piironen",
                "username": "ritapiiii",
                "image": "pdfgenerator/images/avatar_2.jpeg",
            },
        },
        {
            "awareness": 93.31,
            "compatibility": 65.84,
            "virality": 72.8,
            "engagement": 52.19,
            "image": "pdfgenerator/images/woman_3.jpeg",
            "creator": {
                "name": "Janita Iivanainen",
                "username": "janitamariaw",
                "image": "pdfgenerator/images/avatar_3.jpeg",
            },
        },
    ],
    "audience_age": {
        "group_1": 0.084,
        "group_2": 0.35,
        "group_3": 0.327,
        "group_4": 0.159,
        "group_5": 0.061,
        "group_6": 0.014,
        "group_7": 0.003,
    },
    "audience_gender": [
        {"gender": "men", "number": 35},
        {"gender": "women", "number": 65},
    ],
    "countries": {
        "Morocco": 2,
        "Turkey": 2,
        "Indonesia": 2,
        "Italy": 2,
        "Mexico": 2,
        "Canada": 2,
        "Sweden": 2,
        "Australia": 2,
        "Russia": 2,
        "Germany": 3,
        "India": 3,
        "UK": 3,
        "Brazil": 4,
        "US": 5,
        "Finland": 90,
    },
}

input_data_2 = {
    "items": [
        {
            "name": "item A",
            "description": "item description",
            "quantity": 2,
            "unit_price": "$100",
            "total_price": "$200",
        },
        {
            "name": "item B",
            "description": "item description item description longer description",
            "quantity": 1,
            "unit_price": "$100",
            "total_price": "$100",
        },
        {
            "name": "item C",
            "description": "item description decs",
            "quantity": 1,
            "unit_price": "$100",
            "total_price": "$100",
        },
        {
            "name": "item D",
            "description": "item description item description longer",
            "quantity": 1,
            "unit_price": "$100",
            "total_price": "$100",
        },
    ],
    "subtotal": "$500",
    "tax_rate": "20%",
    "total_tax": "$100",
    "total": "$600",
}


def get_data(request):
    return JsonResponse({"input_data": input_data_1})


def index(request):
    html_string = loader.render_to_string("index.html", {"input_data": input_data_1})

    return HttpResponse(html_string)


@csrf_exempt
def generate_pdf(request):
    """Generate PDF 1."""

    # parsing 'request.body' from POST into JSON
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    content = body

    chart_1 = content["chart_1"]
    chart_2 = content["chart_2"]
    chart_3 = content["chart_3"]

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
        {"input_data": input_data_1, "chart_1": chart_1},
    )
    html_string4 = loader.render_to_string(
        "pdfgenerator/template_1.4.html",
        {"input_data": input_data_1, "chart_2": chart_2, "chart_3": chart_3},
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

    pdf1.copy(val).write_pdf("./pdfs/template_1.pdf")

    # byte = pdf1.copy(val).write_pdf("./pdfs/template_1.pdf")
    # encoded = base64.b64encode(byte)
    # encoded = encoded.decode("utf-8")
    # return JsonResponse(encoded)

    # return HttpResponse("pdf has been saved inside /pdfs folder")
    return HttpResponse(html_string3)


def generate_pdf2(request):
    """Generate PDF 2."""

    html_string = loader.render_to_string(
        "pdfgenerator/template_2.html",
        {"input_data": input_data_2},
    )

    html = HTML(string=html_string, base_url=request.build_absolute_uri())

    html.write_pdf("./pdfs/template_2.pdf")

    return HttpResponse("pdf2 has been saved inside /pdfs folder")
