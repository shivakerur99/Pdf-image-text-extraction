import csv

def txt_to_csv(txt_file, csv_file):
    with open(txt_file, 'r') as infile, open(csv_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        for line in infile:
            writer.writerow([line.strip()])

# Example usage:
txt_file = 'sample4.txt'  # Path to your input text file
csv_file = 'output4.csv'  # Path to save the output CSV file
txt_to_csv(txt_file, csv_file)