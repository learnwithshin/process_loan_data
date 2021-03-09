import os
import re

import pandas as pd


resource_dir = "resources/"


def get_target_files(prefix):
    """Get the target files."""
    target_files = [
        file for file in os.listdir(resource_dir) if file.startswith(prefix)
    ]
    return target_files


def concat_df(file_names):
    """Read in each csv file and concatenate into one dataframe."""
    all_dfs = [pd.read_csv(resource_dir + f) for f in file_names]
    return pd.concat(all_dfs)


def extract_payment(string):
    payment_reg = r"monthly payment:\s*\${0,1}(\d*)"
    match = re.search(payment_reg, string, re.I)
    try:
        payment = match.group(1)
        return payment
    except AttributeError:
        print(f"Failed to edtract payment. No match for string: {string}")
        return None
