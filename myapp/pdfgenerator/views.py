from django.http import HttpResponse
from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from django.http import JsonResponse
from io import BytesIO

from weasyprint import HTML, CSS

import pygal
from pygal.style import Style

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


def index(request):
    html_string = loader.render_to_string("index.html")

    return HttpResponse(html_string)


def generate_bar_chart():
    custom_style = Style(
        background="transparent",
        plot_background="transparent",
        font_family="Arial, Helvetica, sans-serif",
        value_label_font_size=24,
        label_font_size=24,
        major_label_font_size=24,
        colors=(
            "#00c4a7",
            "#00c4a7",
            "#00c4a7",
            "#00c4a7",
            "#00c4a7",
            "#00c4a7",
            "#00c4a7",
        ),
    )

    bar_chart = pygal.Bar(
        show_legend=False,
        style=custom_style,
        width=1400,
        range=(0, 40),
    )

    bar_chart.x_labels = (
        "13 - 17",
        "18 - 24",
        "25 - 34",
        "35 - 44",
        "45 - 54",
        "55 - 64",
        "65+",
    )

    bar_chart.add(
        "line",
        [
            input_data_1["audience_age"]["group_1"] * 100,
            input_data_1["audience_age"]["group_2"] * 100,
            input_data_1["audience_age"]["group_3"] * 100,
            input_data_1["audience_age"]["group_4"] * 100,
            input_data_1["audience_age"]["group_5"] * 100,
            input_data_1["audience_age"]["group_6"] * 100,
            input_data_1["audience_age"]["group_7"] * 100,
        ],
    )

    bar_chart.render_to_png("pdfgenerator/static/pdfgenerator/charts/bar_chart.png")


def generate_pie_chart():
    custom_style = Style(
        background="transparent",
        plot_background="transparent",
        colors=("#021c52", "#00c4a7"),
        font_family="Arial, Helvetica, sans-serif",
        legend_font_size=24,
        value_label_font_size=24,
        label_font_size=24,
        major_label_font_size=24,
    )

    pie_chart = pygal.Pie(
        legend_at_bottom=True,
        legend_box_size=16,
        legend_at_bottom_columns=1,
        style=custom_style,
    )

    men = input_data_1["audience_gender"][0]["number"]
    women = input_data_1["audience_gender"][1]["number"]

    pie_chart.add("Men", men)
    pie_chart.add("Women", women)

    pie_chart.render_to_png("pdfgenerator/static/pdfgenerator/charts/pie_chart.png")


def generate_horizontal_bar_chart():
    custom_style = Style(
        background="transparent",
        plot_background="transparent",
        colors=(
            "#00c4a7",
            "#00c4a7",
            "#00c4a7",
            "#00c4a7",
            "#00c4a7",
            "#00c4a7",
            "#00c4a7",
            "#00c4a7",
            "#00c4a7",
            "#00c4a7",
            "#00c4a7",
            "#00c4a7",
            "#00c4a7",
            "#00c4a7",
            "#00c4a7",
        ),
        font_family="Arial, Helvetica, sans-serif",
        value_label_font_size=24,
        label_font_size=24,
        major_label_font_size=24,
    )

    horizontal_bar_chart = pygal.HorizontalBar(
        show_legend=False,
        range=(0, 100),
        style=custom_style,
    )

    horizontal_bar_chart.x_labels = (
        "Finland",
        "US",
        "Brazil",
        "UK",
        "India",
        "Germany",
        "Russia",
        "Australia",
        "Sweden",
        "Canada",
        "Mexico",
        "Italy",
        "Indonesia",
        "Turkey",
        "Morocco",
    )

    horizontal_bar_chart.add(
        "line",
        [
            input_data_1["countries"]["Finland"],
            input_data_1["countries"]["US"],
            input_data_1["countries"]["Brazil"],
            input_data_1["countries"]["UK"],
            input_data_1["countries"]["India"],
            input_data_1["countries"]["Germany"],
            input_data_1["countries"]["Russia"],
            input_data_1["countries"]["Australia"],
            input_data_1["countries"]["Sweden"],
            input_data_1["countries"]["Canada"],
            input_data_1["countries"]["Mexico"],
            input_data_1["countries"]["Italy"],
            input_data_1["countries"]["Indonesia"],
            input_data_1["countries"]["Turkey"],
            input_data_1["countries"]["Morocco"],
        ],
    )

    horizontal_bar_chart.render_to_png(
        "pdfgenerator/static/pdfgenerator/charts/horizontal_bar_chart.png"
    )


def generate_pdf(request):
    """Generate PDF 1."""

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
        {"input_data": input_data_1},
    )
    html_string4 = loader.render_to_string(
        "pdfgenerator/template_1.4.html",
        {"input_data": input_data_1},
    )

    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    html2 = HTML(string=html_string2, base_url=request.build_absolute_uri())
    html3 = HTML(string=html_string3, base_url=request.build_absolute_uri())
    html4 = HTML(string=html_string4, base_url=request.build_absolute_uri())

    pdf1 = html.render()
    pdf2 = html2.render()
    pdf3 = html3.render()
    pdf4 = html4.render()

    generate_bar_chart()
    generate_pie_chart()
    generate_horizontal_bar_chart()

    # combines 4 pages into 1 PDF document
    val = []

    for doc in pdf1, pdf2, pdf3, pdf4:
        for p in doc.pages:
            val.append(p)

    pdf1.copy(val).write_pdf("./pdfs/template_1.pdf")

    return HttpResponse("pdf has been saved inside /pdfs folder")


def generate_pdf2(request):
    """Generate PDF 2."""

    html_string = loader.render_to_string(
        "pdfgenerator/template_2.html",
        {"input_data": input_data_2},
    )

    html = HTML(string=html_string, base_url=request.build_absolute_uri())

    html.write_pdf("./pdfs/template_2.pdf")

    return HttpResponse("pdf2 has been saved inside /pdfs folder")
