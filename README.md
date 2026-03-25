# E-Commerce Data Analysis

## Team Members

1. Mohamed Ibrahim, 231002063
2. Zein Hatem, 231000057
3. Yassin Mashhour, 231000604
4. Youssof Mohie, 231000179

## How to Get Started

```bash
docker build -t big-data-project
docker run --name big-data-project-container -it big-data-project

# then run the python ingest.py file, and everything is automated
python ingest.py data.csv

# to copy results, stop and delete the container, run summary.sh
./summary.sh
```

## Execution Flow

1. When running the `ingest.py` Python file file, it produces the
`data_raw.csv` that's used in preprocessing later

2. Then `preprocess.py` is automatically run by `ingest.py`. It does
the preprocessing and produces `data_preprocessed.csv`. It contains
the final dataset that is ready for analysis

3. `preprocess.py` triggers `analytics.py`, which analyzes the
description column in the dataset (textual analysis)

4. Then `visualize.py` is called which produces the illustrative graphs

5. Then `cluster.py` is called which clusters the data based on ___

## Sample Outputs

___