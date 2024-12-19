# Generating documentation for Model Risk Management

## Set up

Create a Databricks cluster with wkhtmltopdf and graphviz binary installed, use `init.sh` file for the installation.

## Usage

1. [Math Expressions]($./MRM/1. Math Expressions) - lverage KaTex for better formatting 
2. [Format static tables with HTML]($./MRM/2. Format static tables with HTML) - solution to add special effects, like changing the background of table cells
3. [Format datasets with HTML]($./MRM/3. Format datasets with HTML) - extract the entire content make it printable and readable in the final pdf
4. [Generate MRM in PDF]($./MRM/4. Generate MRM in PDF) - export the notebooks to html and uses `pdfkit` to generate the final pdf.
