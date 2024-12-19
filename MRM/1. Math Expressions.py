# Databricks notebook source
# MAGIC %md
# MAGIC # Display mathematical equations
# MAGIC Notebooks support [KaTeX](https://github.com/KaTeX/KaTeX/wiki) for displaying mathematical formulas and equations. For example,
# MAGIC
# MAGIC \\( f(\beta)= -Y_t^T X_t \beta + \sum log( 1+{e}^{X_t\bullet\beta}) + \frac{1}{2}\delta^t S_t^{-1}\delta\\)
# MAGIC
# MAGIC where \\(\delta=(\beta - \mu_{t-1})\\)
# MAGIC
# MAGIC Documentation:
# MAGIC https://docs.databricks.com/en/notebooks/notebooks-code.html#display-mathematical-equations

# COMMAND ----------

# MAGIC %md
# MAGIC # LaTex
# MAGIC ## 7.3 Calculation of long-run average LGD
# MAGIC  
# MAGIC - probability of cure (*Probability of Cure* 𝑝 ) is being calculated as (including open defaults based on classification described above):
# MAGIC  
# MAGIC *Probability of Cure* 𝑝 = $$
# MAGIC \frac{\sum_{k \in p} \left( \text{weight}_k \times \mathbf{1}_{\{k \text{ is closed as cured}\}} + \text{weight}_k \times \mathbf{1}_{\{k \text{ is open but classified as cured}\}} \right)}{\sum_{k \in p} \left( \text{weight}_k \times \mathbf{1}_{\{k \text{ is closed}\}} + \text{weight}_k \times \mathbf{1}_{\{k \text{ is open}\}} \right)}
# MAGIC $$
# MAGIC  
# MAGIC where $$\mathbf{1}$$ denotes indicator (characteristic) function and $$\text{weight}_k \mathbf{1}$$ for ∀ k ∈ _calib. sample_ (open and closed).

# COMMAND ----------

# MAGIC %md
# MAGIC # KaTeX
# MAGIC ## 7.3 Calculation of long-run average LGD
# MAGIC  
# MAGIC - probability of cure \\(\{(Probability \thinspace of \thinspace Cure}_{p}) \\) is being calculated as (including open defaults based on classification described above):
# MAGIC
# MAGIC $${Probability \thinspace of \thinspace Cure}_{p} =
# MAGIC \frac{\sum_{k \in p} \left( \text{weight}_k \times \mathbf{1}_{\{k \text{ is closed as cured}\}} + \text{weight}_k \times \mathbf{1}_{\{k \text{ is open but classified as cured}\}} \right)}{\sum_{k \in p} \left( \text{weight}_k \times \mathbf{1}_{\{k \text{ is closed}\}} + \text{weight}_k \times \mathbf{1}_{\{k \text{ is open}\}} \right)}
# MAGIC $$
# MAGIC  
# MAGIC where \\(\mathbf{1}\\) denotes indicator (characteristic) function and \\(weight_{k} =\mathbf{1}\\) for  \\(\forall{k} \in{calib.sample}\\) (open and closed).

# COMMAND ----------

# MAGIC %md
# MAGIC # KaTeX
# MAGIC ## 7.3 Calculation of long-run average LGD
# MAGIC  
# MAGIC - probability of cure \\(\{(Probability \thinspace of \thinspace Cure}_{p}) \\) is being calculated as (including open defaults based on classification described above):
# MAGIC
# MAGIC $${Probability \thinspace of \thinspace Cure}_{p} =
# MAGIC \frac{\sum_{k \in p} \left( \text{weight}_k \times \mathbf{1}_{\{k \text{ is closed as cured}\}} + \text{weight}_k \times \mathbf{1}_{\{k \text{ is open but classified as cured}\}} \right)}{\sum_{k \in p} \left( \text{weight}_k \times \mathbf{1}_{\{k \text{ is closed}\}} + \text{weight}_k \times \mathbf{1}_{\{k \text{ is open}\}} \right)}
# MAGIC $$
# MAGIC  
# MAGIC where \\(\mathbf{1}\\) denotes indicator (characteristic) function and \\(weight_{k} =\mathbf{1}\\) for  \\(\forall{k} \in{calib.sample}\\) (open and closed).
