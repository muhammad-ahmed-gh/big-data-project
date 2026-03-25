import os
import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

df = pd.read_csv("data_preprocessed.csv")
print(df.head())

all_words = ' '.join(df['Description']).split()
stop_words = set(stopwords.words('english'))
filtered = [word for word in all_words if word not in stop_words]

# most common words
common_words = pd.Series(filtered).value_counts(ascending=False).index.to_list()
print(common_words[:50])

# sizes
sizes = ["small", "big", "medium", "large", "tiny", "huge", "jumbo"]
sizes_occurrences = [word for word in filtered if word in sizes]
common_sizes = pd.Series(sizes_occurrences).value_counts(ascending=False)
print(common_sizes)

#################################################################################
# after analyzing the description column content, we've reached 2 main insights #
#################################################################################

insight1 = f'''\
-- Insight 1 --
Most common words: {common_words[:50]}

It's is noticed that the most purchased products are
related to love, Christmas, and decoration (red, heart,
christmas, decoration, etc.)

Other common words were for house stuff and food (set,
cake, lunch, home, doormat, cream, etc.)
'''

insight2 = f'''\
-- Insight 2 --
Most common sizes:
{common_sizes}

It's is noticed that the most the vast majority of the
consumers tend to buy products of either jumbo or small
sizes

Other less common keywords: medium, tiny, big
'''

with open("insight1.txt", "w") as f:
    f.write(insight1)

with open("insight2.txt", "w") as f:
    f.write(insight2)

os.system("python visualize.py")