def file_preprocessing(file, new_file):
    """
    Using that function the initial dataset is modified for better processing.

    :param file: dataset
    :param new_file: file where the processed data will be stored
    :return:
    """
    with open(file, encoding="utf-8", errors='ignore') as file:
        lines = file.readlines()
        with open(new_file, "w") as f:
            for line in lines:
                cleaned_data = [substring for substring in line.split("\"") if substring != ',' and substring != '']
                if cleaned_data:
                    new_line = ",".join(cleaned_data[0:4])
                    f.write(new_line)
                    f.write('\n')
                else:
                    continue


file_preprocessing("cleared_dataset.csv", "final_dataset.csv")
