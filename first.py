import os
import argparse

def main(database:str, url_list_files:str):
    print("database file " + database)
    print("list file     " + url_list_files)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="Sqlite filename")
    parser.add_argument("-i", "--input", help="File containing urls to read")

    args = parser.parse_args()
    database_file = args.database
    input_file = args.input

    main(database=database_file, url_list_files=input_file)


