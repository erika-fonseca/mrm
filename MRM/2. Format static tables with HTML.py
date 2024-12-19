# Databricks notebook source
# MAGIC %md
# MAGIC # HTML, Javascript, D3 and SVG
# MAGIC To view HTML code, such as Javascript, D3, and SVG, use the displayHTML method.
# MAGIC
# MAGIC Note:
# MAGIC
# MAGIC The maximum size for a notebook cell, including contents and output, is 16MB. Make sure that the size of the HTML you pass to the displayHTML function does not exceed this value.
# MAGIC
# MAGIC When linking to external resources, use https:// instead of http://. Otherwise, graphics, images, or Javascript might not render correctly due to mixed content errors.
# MAGIC
# MAGIC Documentation: https://docs.databricks.com/en/visualizations/html-d3-and-svg.html

# COMMAND ----------

displayHTML(open('samples/dummy_table.html').read())
