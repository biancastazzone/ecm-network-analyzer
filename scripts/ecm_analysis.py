import pandas as pd

# Example ECM gene list
ecm_genes = ["COL1A1", "COL3A1", "COL5A1", "FN1", "MMP2", "MMP9", "ELN"]

df = pd.DataFrame(ecm_genes, columns=["ECM_Genes"])

print("Extracellular Matrix Gene List:")
print(df)
