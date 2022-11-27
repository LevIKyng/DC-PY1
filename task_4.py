import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(input_file, delimiter=",", new_line="\n") -> list[dict]:
    with open(input_file) as file:
        header = file.readline().replace(new_line, "").split(delimiter)
        data = []
        for line in file:
            data.append(line.replace(new_line, "").split(delimiter))
        last_data = []
        for i in range(len(data)):
            new_dict = {}
            for j in range(len(header)):
                new_dict[header[j]] = data[i][j]
            last_data.append(new_dict)
        return last_data

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))