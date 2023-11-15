These csvs contain the prompt features from the [Tree-Prompting paper](https://arxiv.org/abs/2310.14034). Specifically, each dataset runs many prompts through the LLaMA-2 (7B) model, resulting in a table of features. These features can be used the same as any tabular dataset. Outcome is stored in the last column (`label`). The remaining column names give the prompt used to extract the feature.


```python
from sklearn.tree import DecisionTreeClassifier

df_train = pd.read_csv('knnp__dbpedia_train.csv')
df_test = pd.read_csv('knnp__dbpedia_test.csv')
X_train, y_train = df_train.iloc[:, :-1], df_train.iloc[:, -1]
X_test, y_test = df_test.iloc[:, :-1], df_test.iloc[:, -1]

# Column names give the prompt used to generate each feature (with LLaMA-2)
for depth in [1, 2, 3, 4, 5]:
    clf = DecisionTreeClassifier(max_depth=depth)
    clf.fit(X_train, y_train)
    print(f'Accuracy with Tree(depth={depth}) {clf.score(X_test, y_test):3f}')
```

-----Outputs--------
> Accuracy with Tree(depth=1) 0.148438
> Accuracy with Tree(depth=2) 0.191406
> Accuracy with Tree(depth=3) 0.246094
> Accuracy with Tree(depth=4) 0.320312
> Accuracy with Tree(depth=5) 0.398438