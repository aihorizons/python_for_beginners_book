# Project: Data Aggregator (Combining Data from CSV Files)

import csv
 
def csv_reader_generator(filenames):
    for filename in filenames:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                yield row

def aggregate_data(filenames):
    aggregated_data = []
    for row in csv_reader_generator(filenames):
        aggregated_data.append(row)
    return aggregated_data

def write_csv(data, output_filename):
    with open(output_filename, "w", newline="") as file:
        writer = csv.writer(file)
        # Write a header row
        writer.writerow(["Name", "Age", "City"])
        # Write the data rows
        writer.writerows(data)
 
# Example usage
files = ["data1.csv", "data2.csv", "data3.csv"]
combined_data = aggregate_data(files)
write_csv(combined_data, "aggregated_data.csv")
