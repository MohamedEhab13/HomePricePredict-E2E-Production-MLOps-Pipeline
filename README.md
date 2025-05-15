# End-to-End HomePricePredict: Production MLOps Pipeline

![MLOps Pipeline Architecture](Figures/diagram.png) <!-- Placeholder for ZenML/MLflow pipeline diagram -->

## Project Overview
An MLOps-powered solution for residential property price prediction, featuring:
- **Automated ML Pipeline** with ZenML
- **Experiment Tracking** with MLflow
- **Production-grade workflows** from raw data to model deployment

## Repository Structure
```plaintext
house-price-prediction/
├── data/
│   ├── raw/                   # Original Ames Housing Dataset
│   └── processed/            # Cleaned/transformed data
├── notebooks/                # EDA and prototyping notebooks
├── pipelines/                # ZenML pipeline configurations
├── src/
│   ├── preprocessing/        # Custom transformers/scalers
│   ├── models/               # Model architectures
│   └── utils/                # Helper functions
├── mlruns/                   # MLflow experiment tracking
├── artifacts/                # Serialized models/metrics
└── README.md

#### Missing Values Analysis
[![Missing Values Heatmap](placeholder.jpg)](link)  
*Heatmap showing null values distribution in raw dataset*

#### Target Distribution
[![SalePrice Distribution](placeholder.jpg)](link)  
```python
# Skewness reduction implementation
df['SalePrice'] = np.log1p(df['SalePrice'])
