<h1 align="center"> imodels🔍 data</h1>
<p align="center"> Tabular data for various problems, especially for high-stakes rule-based modeling with the <a href="https://github.com/csinva/imodels">imodels package.</a>
</p>



Includes the following datasets and more (see notebooks for more details on the datasets). To download, use the "Name" field as the key: e.g. `imodels.get_clean_dataset('compas_two_year_clean', data_souce='imodels')`.


| Name                  |   Samples |   Features |   Class 0 |   Class 1 |   Majority class % |
|:----------------------|----------:|-----------:|----------:|----------:|-------------------:|
| heart                 |       270 |         15 |       150 |       120 |               55.6 |
| breast_cancer         |       277 |         17 |       196 |        81 |               70.8 |
| haberman              |       306 |          3 |        81 |       225 |               73.5 |
| credit_g              |      1000 |         60 |       300 |       700 |               70   |
| csi_prop              |      3313 |         70 |      2773 |       540 |               83.7 |
| csi_pred              |      3313 |         40 |      2773 |       540 |               83.7 |
| juvenile_clean        |      3640 |        286 |      3153 |       487 |               86.6 |
| compas_two_year_clean |      6172 |         20 |      3182 |      2990 |               51.6 |
| enhancer              |      7809 |         80 |      7115 |       694 |               91.1 |
| iai_pecarn            |     12044 |         58 |     11841 |       203 |               98.3 |
| credit_card_clean     |     30000 |         33 |     23364 |      6636 |               77.9 |
| tbi_prop              |     42428 |        223 |     42052 |       376 |               99.1 |
| tbi_pred              |     42428 |        121 |     42052 |       376 |               99.1 |
| readmission_clean     |    101763 |        150 |     54861 |     46902 |               53.9 |

# Data usage

First, install the `imodels` package: `pip install imodels`. Then, use the `imodels.get_clean_dataset` function.

```python
imodels.get_clean_dataset(dataset_name: str, data_source: str = 'imodels', data_path='data') ‑> Tuple[numpy.ndarray, numpy.ndarray, list]
"""
Fetch clean data (as numpy arrays) from various sources including imodels, pmlb, openml, and sklearn. If data is not downloaded, will download and cache. Otherwise will load locally
"""

```

## Parameters

- **`dataset_name`** : `str`

  dataset_name - unique dataset identifier

- **`data_source`** : `str`

  options: 'imodels', 'pmlb', 'sklearn', 'openml', 'synthetic'

- **`data_path`** : `str`

  path to load/save data (default: 'data')

## Returns

- **`X`** : `np.ndarray`

  features

- **`y`** : `np.ndarray`

  outcome

- **`feature_names`** : `list`

   

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

There are two versions of each PECARN (TBI and CSI) dataset. In the "prop" version missing
values have not been imputed, while in the "pred" version they have. Note that unlike the rest of the
datasets in this repo, which are fully cleaned, csi_pred.csv contains a variable ("SITE") 
that should be removed before fitting models.