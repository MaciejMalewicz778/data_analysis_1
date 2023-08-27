import pandas as pd


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    copy = data.copy(deep=True)
    copy['Pressure (millibars)'].replace(to_replace=0, method='ffill', inplace=True)
    copy['Precip Type'].fillna('no_fall', inplace=True)
    return copy


def transform_variables(data: pd.DataFrame) -> pd.DataFrame:
    copy = data.copy(deep=True)

    copy['is_partly_cloudy'] = copy['Summary'].apply(lambda x: 1 if 'Partly Cloudy' in x else 0)
    copy['is_mostly_cloudy'] = copy['Summary'].apply(lambda x: 1 if 'Mostly Cloudy' in x else 0)
    copy['is_overcast'] = copy['Summary'].apply(lambda x: 1 if 'Overcast' in x else 0)
    copy['is_humid'] = copy['Summary'].apply(lambda x: 1 if 'Humid' in x else 0)
    copy['is_windy'] = copy['Summary'].apply(lambda x: 1 if 'Windy' in x else 0)
    copy['is_foggy'] = copy['Summary'].apply(lambda x: 1 if 'Foggy' in x else 0)
    copy['is_rain'] = copy['Summary'].apply(lambda x: 1 if 'Rain' in x else 0)
    copy['is_breezy'] = copy['Summary'].apply(lambda x: 1 if 'Breezy' in x else 0)
    copy['is_dry'] = copy['Summary'].apply(lambda x: 1 if 'Dry' in x else 0)
    copy['is_clear'] = copy['Summary'].apply(lambda x: 1 if 'Clear' in x else 0)
    copy['is_drizzle'] = copy['Summary'].apply(lambda x: 1 if 'Drizzle' in x else 0)

    copy['month'] = copy['Formatted Date'].str.slice(5, 7)

    copy.drop('Formatted Date', axis=1, inplace=True)
    copy.drop('Summary', axis=1, inplace=True)
    copy.drop('Daily Summary', axis=1, inplace=True)

    return copy


def fix_data(data: pd.DataFrame) -> pd.DataFrame:
    cleaned_data = clean_data(data)
    fixed_data = transform_variables(cleaned_data)
    return fixed_data


def main():
    data_imported = pd.read_csv("weatherHistory.csv", delimiter=",")
    data = fix_data(data_imported)

    print(data.head)

if __name__ == "__main__":
    main()