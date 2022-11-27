import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename: str, delimeter: str = ",", end_row: str = "\n") -> list[dict]:
    with open(filename) as in_file:
        data = in_file.read()
        data = data.split(end_row)
        columns = data[0].split(delimeter)

        return [dict(zip(columns, rows.split(delimeter))) for rows in data[1:-1]]


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
