# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
    Algorithim: Random Forest Classifier
    Data Source: Census Bureau Datasets

## Intended Use
    This ML Model predicts whether income exceeds $50K/yr based on 1994 census data.

## Training Data
    1994 Census Data collected from UC Irvine Machine Learning Repository

## Evaluation Data
    20% of the data is used for testing the ML Model.

## Metrics
    The model was trained on Precision, Recall, and F1.
    Model Preformance:
    Precision: 0.7744 | Recall: 0.6359 | F1: 0.6984  

## Ethical Considerations
    This data was extracted from the 1994 Census database using the following conditions: ((AAGE>16) && (AGI>100) && (AFNLWGT>1)&& (HRSWK>0)) to determine whether the individual makes over $50k a year. To the extent of my knowledge, all data used in this model is free of bias at the time of collection and processing.

## Caveats and Recommendations
    The included ML data, model, and workflow is designed for training purposes only.