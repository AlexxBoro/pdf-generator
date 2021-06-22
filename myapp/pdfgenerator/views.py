from django.http import HttpResponse
from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from weasyprint import HTML, CSS
from django.http import JsonResponse


def index(request):
    html_string = loader.render_to_string("index.html")

    return HttpResponse(html_string)


def generate_pdf(request):
    """Generate pdf."""

    input_data = {
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
                "image": "https://cdn.boksi.com/.../thumbnail.jpg",
                "creator": {
                    "name": "Jutta Häkämies",
                    "username": "juttaemmii",
                    "image": "https://cdn.boksi.com/.../thumbnail.jpg",
                },
            },
            {
                "awareness": 77.8,
                "compatibility": 60.96,
                "virality": 100.0,
                "engagement": 56.87,
                "image": "https://cdn.boksi.com/.../thumbnail.jpg",
                "creator": {
                    "name": "Rita Piironen",
                    "username": "ritapiiii",
                    "image": "https://cdn.boksi.com/.../thumbnail.jpg",
                },
            },
            {
                "awareness": 93.31,
                "compatibility": 65.84,
                "virality": 72.8,
                "engagement": 52.19,
                "image": "https://cdn.boksi.com/.../thumbnail.jpg",
                "creator": {
                    "name": "Janita Iivanainen",
                    "username": "janitamariaw",
                    "image": "https://cdn.boksi.com/.../thumbnail.jpg",
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
        "countries": {"FI": 0.889, "US": 0.039},
    }

    # Write odd and even pages separately:
    #   Lists count from 0 but page numbers usually from 1
    #   [::2] is a slice of even list indexes but odd-numbered pages.
    # document.copy(document.pages[::2]).write_pdf('odd_pages.pdf')
    # document.copy(document.pages[1::2]).write_pdf('even_pages.pdf')

    # Rendered
    html_string = loader.render_to_string(
        # pass chart as image
        "pdfgenerator/template_1.1.html",
        {"input_data": input_data},
    )
    html_string2 = loader.render_to_string(
        "pdfgenerator/template_1.2.html",
        {"input_data": input_data},
    )

    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    html2 = HTML(string=html_string2, base_url=request.build_absolute_uri())

    html.write_pdf("./pdfs/template_1.1.pdf")
    html2.write_pdf("./pdfs/template_1.2.pdf")

    # return HttpResponse(html_string2)
    # return HttpResponse(pdf, content_type="application/pdf")
    return HttpResponse("pdf has been saved inside /pdfs folder")


def generate_pdf2(request):
    """Generate pdf."""

    input_data = {
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

    # Rendered
    html_string = loader.render_to_string(
        # pass chart as image
        "pdfgenerator/template_2.html",
        {"input_data": input_data},
    )
    html = HTML(string=html_string, base_url=request.build_absolute_uri())

    html.write_pdf("./pdfs/template_2.pdf")

    return HttpResponse("pdf2 has been saved inside /pdfs folder")
