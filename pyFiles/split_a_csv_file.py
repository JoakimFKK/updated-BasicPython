import sys
import os
import csv
import argparse

### Accepting arguments from console terminal
def get_arguments():
    parser = argparse.ArgumentParser()
    ### oprettelse af argument
    parser.add_argument(
        "-i",
        "--input_file",
        required=True,
        help="csv input file (with extension)",
        type=str,
    )
    parser.add_argument(
        "-o",
        "--output_file",
        required=True,
        help="csv output file (without extention)",
        type=str,
    )
    parser.add_argument(
        "-r",
        "--row_limit",
        required=True,
        help="row limit to split csv at",
        type=int,
    )
    ### Argumenterne bliver sat til ny variable
    args = parser.parse_args()

    # check if the input_file exists
    is_valid_file(parser, args.input_file)
    # check if the input_file is valid
    is_valid_csv(parser, args.input_file, args.row_limit)

    return args.input_file, args.output_file, args.row_limit

def is_valid_file(parser, file_name):
    # ensures input_file exists
    if not os.path.exists(file_name):
        parser.error(f"The file '{file_name}' does not exist.")
        sys.exit(1)

def is_valid_csv(parser, file_name, row_limit):
    # Ensure that the # of rows in the input_file is greater than the row_limit
    row_count = 0
    for row in csv.reader(open(file_name)):
        row_count += 1
    if not row_count > row_limit:
        parser.error(f"the 'row_count' of '{row_limit}' is less than the number of rows in '{file_name}'")
        sys.exit(1)

def parse_file(arguments):
    # Splits the csv into multiple files or chunks based on the row_limit
    input_file = arguments[0]
    output_file = arguments[1]
    row_limit = arguments[2]
    output_path = "." # current directory/os.cwd()

    with open(input_file, "r") as input_csv:
        reader = csv.reader(input_csv)
        all_rows = []
        for row in reader:
            all_rows.append(row)
        # remove header
        header = all_rows.pop(0)
        # split list of list into chunks
        current_chunk = 1
        # loop through the list
        for i in range(0, len(all_rows), row_limit):
            # create single chunk
            chunk = all_rows[i : i + row_limit]
            # create a new output file
            current_output = os.path.join(output_path, f"{output_file}--{current_chunk}.csv"
            )
            chunk.insert(0, header)
            print()
            print(f"Chunk # {current_chunk}")
            print(f"Filepath: {current_output}")
            print(f"# of rows: {len(chunk)}")

arguments = get_arguments()
parse_file(arguments)