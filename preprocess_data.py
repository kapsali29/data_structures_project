def file_preprocessing(file, new_file):
    """
    Using that function the initial dataset is modified for better processing.

    :param file: dataset
    :param new_file: file where the processed data will be stored
    :return:
    Example
        >>>file_preprocessing("cleared_dataset.csv", "final_dataset.csv")
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


def create_test_dataset(file, new_file, data_size):
    """
    Using that function you are able to create a test dataset in order for better testing and debugging

    :param file: initial dataset
    :param new_file: test dataset filename
    :param data_size: size of data
    :return:
    Example:
        >>>create_test_dataset("final_dataset.csv", "test_dataset.csv", data_size=100)
    """
    with open(file, encoding="utf-8", errors='ignore') as file:
        lines = file.readlines()
        with open(new_file, "w") as f:
            counter = 1
            headers = [substring for substring in lines[0].split("\"") if substring != ',' and substring != '']
            headers = ["id"] + headers
            f.write(",".join(headers))
            lines = lines[1:]
            for line in lines:
                if counter == data_size:
                    break
                else:
                    cleaned_data = [substring for substring in line.split("\"") if substring != ',' and substring != '']
                    cleaned_data = [str(counter)] + cleaned_data
                    counter += 1
                    if cleaned_data:
                        new_line = ",".join(cleaned_data)
                        f.write(new_line)
                    else:
                        continue


chunk_size = int(input("Please enter the size for the test dataset: "))
file_preprocessing("cleared_dataset.csv", "final_dataset.csv")
create_test_dataset("final_dataset.csv", "test_dataset.csv", data_size=chunk_size)
