import pandas as pd

genes = ["COL1A1", "COL3A1", "COL5A1", "FN1", "MMP2"]

df = pd.DataFrame(genes, columns=["ECM_genes"])
print(df)
