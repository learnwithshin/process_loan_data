from utils import get_target_files, concat_df, extract_payment


def main():
    # get all target file names
    file_names = get_target_files(prefix="20")

    # combine all files into one df
    combined_df = concat_df(file_names)

    # assign new column using regex for extraction
    combined_df["payment"] = combined_df["comments"].apply(extract_payment)

    # save to csv
    combined_df.to_csv("result.csv", index=False)
    print("Done")


if __name__ == "__main__":
    main()