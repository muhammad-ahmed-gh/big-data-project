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

```
Insights:
-- Insight 1 --
Most common words: ['set', 'bag', 'red', 'heart', 'retrospot', 'vintage', 'design', 'pink', 'christmas', 'box', 'cake', 'white', 'metal', 'jumbo', 'lunch', '3', 'blue', 'hanging', 'holder', 'sign', 'pack', 'tlight', 'paper', 'small', 'card', 'wooden', '6', 'cases', 'glass', 'tea', 'polkadot', '12', 'decoration', 'spaceboy', 'bottle', 'home', 'hot', 'pantry', 'large', 'tin', 'water', 'regency', 'ceramic', 'doormat', '4', 'paisley', 'dolly', 'ivory', 'cream', 'bunting']

It's is noticed that the most purchased products are
related to love, Christmas, and decoration (red, heart,
christmas, decoration, etc.)

Other common words were for house stuff and food (set,
cake, lunch, home, doormat, cream, etc.)
```