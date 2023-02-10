import os
import pandas as pd
from jinja2 import Environment, FileSystemLoader

folder = "path/to/folder"
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("template.html")

for filename in os.listdir(folder):
    if filename.endswith(".xlsx"):
        filepath = os.path.join(folder, filename)
        df1 = pd.read_excel(filepath, sheet_name="Sheet1").fillna('')
        df2 = pd.read_excel(filepath, sheet_name="Sheet2").fillna('')
        df3 = pd.read_excel(filepath, sheet_name="Sheet3").fillna('')

        html = template.render(
            df1=df1.to_html(classes='table table-striped'),
            df2=df2.to_html(classes='table table-striped'),
            df3=df3.to_html(classes='table table-striped')
        )

        with open(f"{os.path.splitext(filename)[0]}_sheet1.html", "w") as f:
            f.write(html)

        html = template.render(
            df1=df2.to_html(classes='table table-striped'),
            df2=None,
            df3=None
        )

        with open(f"{os.path.splitext(filename)[0]}_sheet2.html", "w") as f:
            f.write(html)

        html = template.render(
            df1=df3.to_html(classes='table table-striped'),
            df2=None,
            df3=None
        )

        with open(f"{os.path.splitext(filename)[0]}_sheet3.html", "w") as f:
            f.write(html)
