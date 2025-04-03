# MSID Lab Project 1

## Author
**280462 – Bartosz Wacławiak**

## Grade
** Aiming for 5.5**

## Dataset
[Predict Students' Dropout and Academic Success – UCI ML Repo](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)

## Project Scope
Exploratory Data Analysis (EDA) using Python, focusing on both numerical and categorical features. Visualizations include boxplots, violin plots, histograms, error bars, correlation heatmaps, regression analysis, and dimensionality reduction (PCA).

## Catalog structure and files

<pre> project/ 
    ├── data/                           # holds the data set
    │ └── data.csv                      # students data set
    │ ├── scripts/                      # helper functions
    │ ├── consts.py                     # constant values, mainly dictonaries for converting categorical attributes
    │ ├── read_data.py                  # reads data from data/data.csv and converts them to DataFrame
    │ └── errorbar.py                   # for creating errorbars to avoid code duplication and follow custom format
    │ ├── notebook/                     # each notebook corresponds to the plot type from the task
    │ ├── boxplots.ipynb                # Grade 3.5 
    │ ├── violinplots.ipynb             # Grade 3.5 
    │ ├── histograms.ipynb              # Grade 4.0 
    │ ├── error_plots.ipynb             # Grade 4.0 
    │ ├── heatmap.ipynb                 # Grade 4.5 
    │ ├── regression.ipynb              # Grade 5.0 
    │ ├── PCA.ipynb                     # Grade 5.5 
    │ ├── initial_statistics.ipynb      # Grade 3.0 
    │ └── config.py                     # access script/ module
    │ ├── statistics/                   # CSVs with statistics 
    ├── generated_charts/               # Output plots 
    ├── data_analysis_main.py           # Main script to generate all the files 
    ├── RAPORT.md                       # Summary and visual insights 
    ├── README.md                       # Project general info
    └── Task.pdf                        # Task description
</pre>



