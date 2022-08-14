<h1 align="center"> imodels🔍 data</h1>
<p align="center"> Tabular data for various problems, especially for high-stakes rule-based modeling with the <a href="https://github.com/csinva/imodels">imodels package.</a>
<p align="center"> See also https://huggingface.co/imodels </p>
</p>


Includes the following datasets and more (see notebooks for more details on the datasets).

To download, use the "Name" field as the key: e.g. `imodels.get_clean_dataset('compas_two_year_clean', data_source='imodels')`.


| Name                  |   Samples |   Features |   Class 0 |   Class 1 |   Majority class % |
|:----------------------|----------:|-----------:|----------:|----------:|-------------------:|
| heart                 |       270 |         15 |       150 |       120 |               55.6 |
| breast_cancer         |       277 |         17 |       196 |        81 |               70.8 |
| haberman              |       306 |          3 |        81 |       225 |               73.5 |
| credit_g              |      1000 |         60 |       300 |       700 |               70   |
| csi_pecarn_prop       |      3313 |         97 |      2773 |       540 |               83.7 |
| csi_pecarn_pred       |      3313 |         39 |      2773 |       540 |               83.7 |
| juvenile_clean        |      3640 |        286 |      3153 |       487 |               86.6 |
| compas_two_year_clean |      6172 |         20 |      3182 |      2990 |               51.6 |
| enhancer              |      7809 |         80 |      7115 |       694 |               91.1 |
| fico                  |     10459 |         23 |      5000 |      5459 |               52.2 |
| iai_pecarn_prop       |     12044 |         73 |     11841 |       203 |               98.3 |
| iai_pecarn_pred       |     12044 |         58 |     11841 |       203 |               98.3 |
| credit_card_clean     |     30000 |         33 |     23364 |      6636 |               77.9 |
| tbi_pecarn_prop       |     42428 |        223 |     42052 |       376 |               99.1 |
| tbi_pecarn_pred       |     42428 |        121 |     42052 |       376 |               99.1 |
| readmission_clean     |    101763 |        150 |     54861 |     46902 |               53.9 |
# Data usage

First, install the `imodels` package: `pip install imodels`. Then, use the `imodels.get_clean_dataset` function.

```python
imodels.get_clean_dataset(dataset_name: str, data_source: str = 'imodels', data_path='data') ‑> Tuple[numpy.ndarray, numpy.ndarray, list]
"""
Fetch clean data (as numpy arrays) from various sources including imodels, pmlb, openml, and sklearn. If data is not downloaded, will download and cache. Otherwise will load locally

Parameters
----------
dataset_name: str
    dataset_name - unique dataset identifier
data_source: str
    options: 'imodels', 'pmlb', 'sklearn', 'openml', 'synthetic'
data_path: str
    path to load/save data (default: 'data')

Returns
-------
X: np.ndarray
    features
y: np.ndarray
    outcome
feature_names: list
"""

```
   

## Example

```python
# download compas dataset from imodels
X, y, feature_names = imodels.get_clean_dataset('compas_two_year_clean', data_source='imodels')
# download ionosphere dataset from pmlb
X, y, feature_names = imodels.get_clean_dataset('ionosphere', data_source='pmlb')
# download liver dataset from openml
X, y, feature_names = imodels.get_clean_dataset('8', data_source='openml')
# download ca housing from sklearn
X, y, feature_names = imodels.get_clean_dataset('california_housing', data_source='sklearn')
```

# Data info

Data comes from various sources - please cite those sources appropriately.

> [notebooks_fetch_data](notebooks_fetch_data) contains notebooks which download and preprocess the data
> 
> [data_cleaned](data_cleaned) contains the cleaned csv file for each dataset


## Clinical decision-rule (PECARN) datasets
There are two versions of each PECARN (TBI, IAI, and CSI) dataset.
- `prop`: missing values have not been imputed
- `pred`: missing values have been imputed

`csi_pecarn_pred.csv` note: unlike the rest of the datasets in this repo, which are fully cleaned, `csi_pecarn_pred.csv` contains a variable ("SITE") 
that should be removed before fitting models.


| Dataset |  Task                                                        | Size                            | References |
| ---------- | ----- | ----------------------------------------------------------- | :-------------------------------: |
|iai_pecarn| Predict intra-abdominal injury requiring acute intervention before CT | 12,044 patients, 203 with IAI-I | [📄](https://pubmed.ncbi.nlm.nih.gov/23375510/), [🔗](https://pecarn.org/datasets/) |
|tbi_pecarn| Predict traumatic brain injuries before CT | 42,412 patients, 376 with ciTBI | [📄](https://pecarn.org/studyDatasets/documents/Kuppermann_2009_The-Lancet_000.pdf), [🔗](https://pecarn.org/datasets/) |
|csi_pecarn | Predict cervical spine injury in children | 3,314 patients, 540 with CSI | [📄](https://pecarn.org/studyDatasets/documents/Kuppermann_2009_The-Lancet_000.pdf), [🔗](https://pecarn.org/datasets/)

## Miscellaneous notes
The `breast_cancer` dataset here is not the extremely common Wisconsin breast-cancer dataset but rather [this dataset](https://www.openml.org/search?type=data&sort=runs&id=13&status=active) from OpenML. Preprocessing (e.g. dropping missing values) results in the cleaned data having n=277, p=17, rather than the original n=286, p=9.

Some other cool datasets:

- [moleculenet](https://moleculenet.org/datasets-1) - benchmarks for molecular datasets
- [srbench](https://github.com/cavalab/srbench) - benchmarking for symbolic regression
- [big-bench](https://github.com/google/BIG-bench) - language modeling benchmarks
