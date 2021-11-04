'''A collection of Data Science Helper functions'''

import pandas as pd
from sklearn.utils import shuffle

def null_count(df): 
    """
    Check a dataframe for nulls and return the number of missing values
    """

    # Example Input (df = pd.DataFrame):
    # > | column 0    | column 1    | column 2    |
    # > | ----------- | ----------- | ----------- |
    # > | NaN         | 9           | 10          |
    # > | 4           | NaN         | 2           |
    # > | 3           | NaN         | 2           |

    # Function:
    # > `null_count(df)`

    # Expected Output (int):
    # > `3`

    # x = [df[col].isna().sum() for col in df.columns]
    # y = 0
    # for num in x:
    #   y += num
    #   return y

    return df.isna().sum().sum()


def train_test_split(df, frac):
    """Create a train/test split function for a data frame that returns both the
    training and test sets.  'frac' refers to the percent of data you would
    like to set aside for training"""

    cutoff = df.index < int(df.shape[0] * frac)
    df_train = df.loc[cutoff]
    df_test = df.loc[~cutoff]
    print(df_train)
    print(df_test)
    return df_train, df_test


def randomize(df, seed):
    """Develop a randomization function that randomizes all of a 
    dataframe's cells then returns that randomized dataframe. This
    function also accepts a random seed for reproducible randomization"""

    df = df.copy()
    columns = df.columns
    # df = shuffle(df, random_state=seed) # also works
    df = shuffle(df[columns], random_state=seed)
    return df


def addy_split(addy_series):
    """Split addresses into three columns (df['city'],
    df['state'], df['zip']"""

    # Example Input (addy_series = pd.Series):
    #        > | address                                    |
    #        > | ------------------------------------------ |
    #        > | 890 Jennifer Brooks\nNorth Janet, WY 24785 |
    #        > | 8394 Kim Meadow\nDarrenville, AK 27389     |
    #        > | 379 Cain Plaza\nJosephburgh, WY 06332      |
    #        > | 5303 Tina Hill\nAudreychester, VA 97036    |

    #        Function:
    #        > `addy_split(addy_series)`

    #        Expected Output (pd.Dataframe): 
    #        > | city          | state       | zip         |
    #        > | ------------- | ----------- | ----------- |
    #        > | North Janet   | WY          | 24785       |
    #        > | Darrenville   | AK          | 27389       |
    #        > | Josephburgh   | WY          | 06332       |
    #        > | Audreychester | VA          | 97036       |

    cities = []
    states = []
    zips = []

    for entry in addy_series:
        split_addy = entry.split(",")
        cities.append(split_addy[0].split('\n')[1])
        states.append(split_addy[1].split(" ")[1])
        zips.append(split_addy[1].split(" ")[2])

    df = pd.DataFrame({'city': cities, 'state': states, 'zip': zips})
    return df