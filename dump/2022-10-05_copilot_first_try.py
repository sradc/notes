"""Playing around with copilot for the first time...
Very impressed.
Had a few holy shit moments tbh.

## Library versions used in this script:
python 3.9.2
pandas 1.2.3
plotly 5.10.0

## Suggestion from copilot:
Use a library like scikit-learn to do this more easily
https://scikit-learn.org/stable/modules/grid_search.html
https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html
https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html
https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ParameterGrid.html
"""
import random
from itertools import product

import pandas as pd
import plotly.express as px


def train_model_with_params(width, depth):
    "Simulate training a model and getting a score"
    return random.random() * 1000


def iter_param_combos(hyperparams: dict):
    "Iterate over all permutations of hyperparams"
    keys = hyperparams.keys()
    for values in product(*hyperparams.values()):
        yield dict(zip(keys, values))


if __name__ == "__main__":
    hyperparams = {
        "width": [10, 33, 100],
        "depth": [1, 2, 3],
    }
    # pre fill a dataframe with the hyperparams
    # so we can add the scores later
    df = pd.DataFrame(iter_param_combos(hyperparams))
    # train the model for each hyperparam permutation
    # and add the score to the dataframe
    for i, hyperparam in df.iterrows():
        df.loc[i, "score"] = train_model_with_params(**hyperparam)
    # plot the results
    fig = px.scatter_3d(df, x="width", y="depth", z="score")
    fig.show()
    fig = px.parallel_coordinates(df, color="score")
    fig.show()
    fig = px.parallel_categories(df, color="score")
    fig.show()
    # print the best score
    best_hyperparams = df.loc[df["score"].idxmax()]
    print("Best hyperparams:")
    print(best_hyperparams.to_string())
    # print the worst score
    worst_hyperparams = df.loc[df["score"].idxmin()]
    print("Worst hyperparams:")
    print(worst_hyperparams.to_string())
