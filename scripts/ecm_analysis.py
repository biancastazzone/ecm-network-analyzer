library(DESeq2)

# ejemplo simple
counts <- matrix(sample(1:1000, 100, replace=TRUE), ncol=10)
coldata <- data.frame(condition=rep(c("control","treated"), each=5))

dds <- DESeqDataSetFromMatrix(countData = counts,
                              colData = coldata,
                              design = ~ condition)

dds <- DESeq(dds)
res <- results(dds)

print(head(res))
