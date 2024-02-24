# Chapter1. Introduction

### Statistical Learning

Statistical Learning : a vast set of tools for understanding data

- Supervised ⇒ predicting output based on one or more inputs
- Unsupervised ⇒ inputs O supervising ouput X

EX

1. Wage data: regression problem
    1. predicting continuous or quantitative ouput value
    2. linear / non-linear relationship
2. Stock market data: classification problem
    1. predicting a non-numerical value (categorical or qualitative)
3. Gene expression data: unsupervised clustering problem
    1. only observe input variables, with no corresponding output
    2. not predicting an output variable
    3. ex. for each of 64 cancer cell lines, the data set is consist of 6,830 gene expression
        1. we are determining whether there are **groups or clusters** among the cell lines based on the gene expression measurement
            
            ![2 dimensions / principal components : Z1, Z2](https://prod-files-secure.s3.us-west-2.amazonaws.com/7891be5e-1f45-42d0-9a0a-5df6f433bf7d/5db6bd38-5476-4834-ba46-63c7ae603712/0B28D354-D673-4359-BF24-D9E7810509FF.jpeg)
            
            2 dimensions / principal components : Z1, Z2
            
        2. dimension reduction ⇒ resulted in some loss of information
        3. cell lines with the same cancer type tend to be located near each other in this 2-dimensional representation.
        

### Notation and Simple Matrix Algebra

n ⇒ number of distinct data observations (3,000 people)

p ⇒ number of variables that are available for use in making predictions (age, year, educational level,..)