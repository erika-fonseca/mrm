# Databricks notebook source
pip install requests==2.31.0 PyYAML==6.0 graphviz==0.20.1 pdfkit==1.0.0 nbconvert==5.6.1 jinja2==3.0.3 bs4

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

import os
from os import listdir
from os.path import isfile, join
import logging
import requests
import base64

from bs4 import BeautifulSoup
from nbconvert import HTMLExporter
import nbformat

import pdfkit

logger = logging.getLogger('databricks')

# COMMAND ----------

dst_header = os.path.join(os.getcwd(), "templates/header.html")
dst_footer = os.path.join(os.getcwd(), "templates/footer.html")
dst_cover = os.path.join(os.getcwd(), "templates/cover.html")

# Get the API endpoint and token for the current notebook context
API_ROOT = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiUrl().get() 
API_TOKEN = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()

api_endpoint = f"{API_ROOT}/api/2.0/workspace/export"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

# COMMAND ----------

# MAGIC %md
# MAGIC # Generate ipynb

# COMMAND ----------

path = "/Workspace/Users/erika.fonseca@databricks.com/mrm/MRM/dlt-cdc"

separator = " "  # Define a separator, e.g., space

files = sorted([f for f in listdir(path) if isfile(join(path, f))])

content = []
for file_name in files:
    data = {"path": f"{path}/{file_name}", "format": "JUPYTER", "direct_download": True}
    # Make the request to export the notebook
    logger.info(f"Retrieving notebook {path}/{file_name} associated to model")
    response = requests.get(api_endpoint, headers=headers, params=data)

    if "error_code" in response:
        logger.error(f"Error in notebook response, {response['message']}")

    else:
        decoded_content = base64.b64decode(response.json()["content"]).decode("utf-8")
        notebook_content = nbformat.reads(decoded_content, as_version=4)

        # Initialize the HTMLExporter (or any other exporter)
        html_exporter = HTMLExporter(template="classic")
        # Export the notebook to HTML
        (body, resources) = html_exporter.from_notebook_node(notebook_content)

        # Save the css
        with open(f"exports/{file_name}.css", "w", encoding="utf-8") as f:
            f.write(separator.join(resources["inlining"]["css"]))

        # Save the output to a file
        with open(f"exports/{file_name}.html", "w", encoding="utf-8") as f:
            """By default the library adds the custom.css to all files, but this behaviour is problematic,
            so we need to replace the css reference with the one we just created.
            """
            body = body.replace("custom.css", f"{file_name}.css")
            f.write(body)

# COMMAND ----------

# MAGIC %md
# MAGIC # Generate pdf

# COMMAND ----------

html_files = [f"exports/{f}.html" for f in files]
data_files = sorted(
    [
        f
        for f in listdir(join(os.getcwd(), "exports/data"))
        if isfile(join(join(os.getcwd(), "exports/data"), f))
    ]
)
data_files = [f"exports/data/{f}" for f in data_files]
html_files.extend(data_files)

options = {
    "page-size": "Letter",
    "enable-local-file-access": None,
    "--header-html": "file://{}".format(dst_header),
    "--footer-font-size": "8",
    "--footer-left": "Copyright © 2024 by Raiffeisen Bank International AG",
    "--footer-right": "[page]/[toPage]",
    "margin-top": "1in",
    "margin-bottom": "1in",
    "margin-right": "1in",
    "margin-left": "1in",
    "no-outline": None,
    "--header-spacing": 3,
    "--footer-spacing": 3,
    "--no-stop-slow-scripts": True,
    "--javascript-delay":  5000
}

toc = {"toc-header-text": "Table of Contents", "toc-text-size-shrink": 1}

cover = f"file://{dst_cover}"

pdfkit.from_file(
    html_files,
    "mrm.pdf",
    options=options,
    toc=toc,
    cover=cover,
    cover_first=True,
    verbose=True,
)
