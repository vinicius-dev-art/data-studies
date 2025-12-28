from pathlib import Path
import pandas as pd
import io


def load_dataset(file_path: Path) -> pd.DataFrame:
    """
    Loads the Titanic dataset from a non-standard CSV file.

    The original dataset is stored in a malformed CSV format where each row
    is enclosed in double quotes and internal quotes are escaped.
    This function normalizes the file content before loading it into pandas.

    Parameters
    ----------
    file_path : Path
        Path to the CSV dataset file.

    Returns
    -------
    pd.DataFrame
        Properly parsed Titanic dataset.
    """
    with open(file_path, "r", encoding="utf-8", errors="replace") as file:
        lines = file.read().splitlines()

    cleaned_lines = []
    for line in lines:
        # Remove enclosing quotes from each row
        if line.startswith('"') and line.endswith('"'):
            line = line[1:-1]

        # Fix escaped double quotes inside fields
        line = line.replace('""', '"')
        cleaned_lines.append(line)

    normalized_csv = "\n".join(cleaned_lines)

    return pd.read_csv(io.StringIO(normalized_csv), sep=",")


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the Titanic dataset by handling missing values.

    - Fills missing values in categorical columns with 'Not known'
    - Removes rows with remaining missing values

    Parameters
    ----------
    df : pd.DataFrame
        Raw Titanic dataset.

    Returns
    -------
    pd.DataFrame
        Cleaned dataset ready for analysis.
    """
    df_clean = df.copy()

    df_clean["Embarked"] = df_clean["Embarked"].fillna("Not known")
    df_clean["Cabin"] = df_clean["Cabin"].fillna("Not known")

    df_clean = df_clean.dropna()

    return df_clean


def save_dataset(df: pd.DataFrame, output_path: Path) -> None:
    """
    Saves the cleaned dataset to a CSV file.

    Parameters
    ----------
    df : pd.DataFrame
        Cleaned dataset.
    output_path : Path
        Destination path for the output file.
    """
    df.to_csv(output_path, index=False)


def main() -> None:
    """
    Executes the full data cleaning pipeline:
    - Loads the raw dataset
    - Cleans missing values
    - Saves the cleaned dataset
    """
    data_dir = Path("data")

    input_file = data_dir / "Titanic-Dataset.csv"
    output_file = data_dir / "Titanic-Dataset-cleaned.csv"

    df_raw = load_dataset(input_file)
    df_clean = clean_dataset(df_raw)

    save_dataset(df_clean, output_file)


if __name__ == "__main__":
    main()
