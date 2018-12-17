
getwd()
library(Seurat)
library(dplyr)
print('loaded')
pbmc.data <- Read10X(data.dir = "filtered_gene_bc_matrices/hg19/")
dense.size <- object.size(x = as.matrix(x = pbmc.data))
dense.size
pbmc <- CreateSeuratObject(raw.data = pbmc.data, min.cells = 3, min.genes = 200, project = "10X_PBMC")
save(pbmc, file = "seurat_object.rda")
