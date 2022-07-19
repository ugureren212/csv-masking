import re

"""
 splits csv file into line and stores "columns" into an array
 csv data is stored in format of dict of arrays to allow for masking of data and stat calc
"""


def import_CSV(filename: str = "") -> dict:
    csv_file = open(filename)
    dict = {}
    headers = csv_file.readline().replace("\n", "").split(",")

    for line in csv_file:
        line_data = line.replace("\n", "").split(",")
        row = {}
        # stores first line as header/columns
        for header in range(len(headers)):
            if header in range(len(headers)):
                # [header: line_data[index(header)]
                row[headers[header]] = line_data[header]
            # catch values without header/column
            else:
                row[headers[header]] = "null"
        # primary key (line_data[0]):
        dict[line_data[0]] = [row]
    csv_file.close()
    return dict


# masks all numeric values in CSV_file with average "Billing" value
def mask_numeric(data: dict) -> dict:
    total_billing = 0
    i = 1

    # calculate average billing
    for line in data:
        for column in data[line]:
            i += 1
            if len(column["Billing"]) == 0 or " " in column["Billing"]:
                continue

            total_billing = total_billing + float(column["Billing"])

    for line in data:
        for column in data[line]:
            data[line][0]["Billing"] = total_billing // i

    return data


# masks emails and names with "X"
def mask_email_and_name(data: dict) -> dict:
    # change/mask existing numeric values
    for line in data:
        for column in data[line]:
            # masks all char's exepect "@.,"
            result_email = re.sub("[^@.,]", "X", column["Email"])
            result_name = re.sub("[^@.,]", "X", column["Name"])

            data[line][0]["Email"] = result_email
            data[line][0]["Name"] = result_name

    return data


def write_to_file(masked_CSV_file: dict, headers: list):
    f = open("masked_clients.csv", "w")

    header = ", ".join([str(x) for x in headers])
    header = header + "\n"
    f.write(header)

    last_line = list(masked_CSV_file)[-1]

    for line in masked_CSV_file:
        text_array = [
            masked_CSV_file[line][0]["ID"],
            masked_CSV_file[line][0]["Name"],
            masked_CSV_file[line][0]["Email"],
            masked_CSV_file[line][0]["Billing"],
            masked_CSV_file[line][0]["Location"],
            "\n",
        ]

        # check for last line in masked_CSV_file. Last line will not append \n new line
        if masked_CSV_file[line][0]["ID"] == last_line:
            text_array = [
                masked_CSV_file[line][0]["ID"],
                masked_CSV_file[line][0]["Name"],
                masked_CSV_file[line][0]["Email"],
                masked_CSV_file[line][0]["Billing"],
                masked_CSV_file[line][0]["Location"],
            ]

        text_string = ", ".join([str(x) for x in text_array])

        # Slice string to remove "," from last column
        index = len(text_string) - 3
        if len(text_string) > index:
            text_string = text_string[0:index:] + text_string[index + 1 : :]

        f.write(text_string)
    f.close()


def calc_name_stats(CSV_file: dict) -> list:
    name_length = []

    for line in CSV_file:
        # check for empty values
        if len(CSV_file[line][0]["Name"]) <= 1:
            continue
        name_length.append(len(CSV_file[line][0]["Name"]))

    min_char = min(name_length)
    max_char = max(name_length)

    sum_char = sum(name_length)
    length_char = len(name_length)

    average_char = sum_char // length_char

    return [max_char, min_char, average_char]


def calc_billing_stat(CSV_file: dict) -> list:
    billing_value = []

    for line in CSV_file:
        # check for empty values
        if len(CSV_file[line][0]["Billing"]) <= 1:
            billing_value.append(float(0))
        else:
            billing_value.append(float(CSV_file[line][0]["Billing"]))

    min_val = min(billing_value)
    max_val = max(billing_value)

    sum_val = sum(billing_value)
    length_val = len(billing_value)

    average_char = sum_val / length_val

    return [max_val, min_val, average_char]


def report_stat(CSV_file: dict) -> list:
    name_stat = calc_name_stats(CSV_file)
    billing_stat = calc_billing_stat(CSV_file)

    name_report = "Name: Max. %d, Min. %d, Avg. %d" % (
        name_stat[0],
        name_stat[1],
        name_stat[2],
    )
    billing_report = "Billing: Max. %d, Min. %d, Avg. %d" % (
        billing_stat[0],
        billing_stat[1],
        billing_stat[2],
    )

    return [name_report, billing_report]


def import_CSVHeaders(filename: str) -> list:
    csv_file = open(filename)
    headers = csv_file.readline().replace("\n", "").split(",")
    return headers


# """
# # reads csv file and stores data in a dict.
# # dict is used to mask values and calculate stats
# """

CSV_file = import_CSV("customers.csv")

CSVHeaders = import_CSVHeaders("customers.csv")

name_report, billing_report = report_stat(CSV_file)

print(name_report)
print(billing_report)

numericmasked_CSV_file = mask_numeric(CSV_file)

masked_CSV_file = mask_email_and_name(numericmasked_CSV_file)

write_to_file(masked_CSV_file, CSVHeaders)
