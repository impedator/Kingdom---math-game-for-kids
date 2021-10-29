#! /usr/bin/python3

import datetime
from random import randrange
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors

if __name__ == "__main__":

    x = datetime.datetime.now()
    kingdom_pdf_file_name = (str(x.year)+str(x.month)+str(x.day)
                             + str(x.hour)+str(x.minute)+str(x.second)
                             + "-kingdom.pdf")

    data = []
    collumns = 11
    rows = 15
    element = 0
    # Generowanie listy list 11 kolumn, 14 wierszy z losowymi cyframi
    for iii in range(0, rows):
        temp_list = []
        for jjj in range(0, collumns):
            element_old = element
            element = randrange(1, 9)
            while (element + element_old > 10):
                element = randrange(1, 9)
            temp_list.extend([str(element)])
        data.append(temp_list)
        element = 0
        print(temp_list)

    pdf = SimpleDocTemplate(
        kingdom_pdf_file_name,
        pagesize=A4
    )

    table = Table(data)
    # add style
    style = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Courier-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 30),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 30),
        ('LEFTPADDING', (0, 0), (-1, -1), 15),
        ('RIGHTPADDING', (0, 0), (-1, -1), 15)
    ])
    table.setStyle(style)
    # Add borders
    ts = TableStyle(
        [
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]
    )
    table.setStyle(ts)

    elems = []
    elems.append(table)

    pdf.build(elems)
