# DSML-Lab

Data Science and Machine Learning Laboratory codes for MCA Semester 3.

## Repository Structure

This repository contains various DSML lab experiments organized by topics:

- `data-preprocessing/` - Data cleaning and preprocessing techniques
- `visualization/` - Data visualization using matplotlib, seaborn
- `statistics/` - Statistical analysis and hypothesis testing
- `regression/` - Linear and polynomial regression models
- `classification/` - Classification algorithms (KNN, SVM, Decision Trees)
- `clustering/` - Unsupervised learning algorithms
- `neural-networks/` - Basic neural network implementations

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/CERO-100/DSML-Lab.git
cd DSML-Lab
```

2. Install required packages:
```bash
pip install numpy pandas matplotlib seaborn scikit-learn jupyter
```

3. Navigate to specific lab folders and run the Python files or Jupyter notebooks.

## Requirements

- Python 3.7+
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook (optional)

Each subfolder contains its own README with specific instructions.

# Data Preprocessing

This folder contains code for data cleaning and preprocessing techniques.

## Files

- `data_cleaning.py` - Data cleaning operations
- `missing_values.py` - Handling missing values
- `outlier_detection.py` - Outlier detection and removal
- `feature_scaling.py` - Feature normalization and standardization

## How to Run

```bash
python data_cleaning.py
```

## Working

1. **Data Cleaning**: Removes duplicates, handles inconsistent data formats
2. **Missing Values**: Implements various imputation techniques (mean, median, mode)
3. **Outlier Detection**: Uses IQR and Z-score methods for outlier identification
4. **Feature Scaling**: Applies Min-Max scaling and Standard scaling

## Input/Output

- Input: Raw CSV datasets
- Output: Cleaned and preprocessed data ready for ML models

# Data Visualization

This folder contains various data visualization techniques using Python libraries.

## Files

- `basic_plots.py` - Line plots, bar charts, histograms
- `advanced_plots.py` - Heatmaps, box plots, scatter plots
- `seaborn_viz.py` - Advanced visualizations using Seaborn

## How to Run

```bash
python basic_plots.py
python advanced_plots.py
python seaborn_viz.py
```

## Working

1. **Basic Plots**: Creates fundamental charts for data exploration
2. **Advanced Plots**: Generates complex visualizations for pattern recognition
3. **Seaborn Visualizations**: Statistical plotting with beautiful aesthetics

## Dependencies

- matplotlib
- seaborn
- pandas
- numpy

## Output

Generated plots are saved as PNG files in the `plots/` directory.

# Regression Analysis

Implementation of various regression algorithms for predictive modeling.

## Files

- `linear_regression.py` - Simple and multiple linear regression
- `polynomial_regression.py` - Polynomial regression implementation
- `regression_metrics.py` - Model evaluation metrics

## How to Run

```bash
python linear_regression.py
python polynomial_regression.py
```

## Working

1. **Linear Regression**: 
   - Fits linear relationship between features and target
   - Uses least squares method
   - Calculates R² score and RMSE

2. **Polynomial Regression**:
   - Fits polynomial curves to data
   - Handles non-linear relationships
   - Includes degree selection techniques

## Input Data

- CSV files with numerical features
- Target variable for supervised learning

## Output

- Trained model coefficients
- Prediction accuracy metrics
- Visualization plots showing fit quality

# Clustering Algorithms

Unsupervised learning algorithms for pattern discovery and data grouping.

## Files

- `kmeans_clustering.py` - K-Means clustering implementation
- `hierarchical_clustering.py` - Agglomerative clustering
- `dbscan_clustering.py` - Density-based clustering

## How to Run

```bash
python kmeans_clustering.py
python hierarchical_clustering.py
python dbscan_clustering.py
```

## Working

1. **K-Means**: Partitions data into k clusters using centroid-based approach
2. **Hierarchical**: Creates tree of clusters using linkage criteria
3. **DBSCAN**: Groups dense regions and identifies outliers

## Evaluation Methods

- Silhouette Score
- Within-cluster Sum of Squares (WCSS)
- Elbow Method for optimal k
- Dendrogram visualization

## Applications

- Customer segmentation
- Image segmentation
- Anomaly detection
- Data compression