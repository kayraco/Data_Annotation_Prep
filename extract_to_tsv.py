import pandas as pd
import argparse
import json
import csv
import random


def get_post(json_data, num_posts_to_output, out_file):
    data = []
    if num_posts_to_output is None:

        for posts in json_data:

            row = {}
            row["Name"] = posts["data"]["name"]
            row["title"] = posts["data"]["title"]
            row["coding"] = ""
            data.append(row)


    elif int(num_posts_to_output) < len(json_data):
        data = []
        sample_indexes = random.sample(range(1, len(json_data)), int(num_posts_to_output))
        for index in sample_indexes:
            post = json_data[index]
            row = {}
            row["Name"] = post["data"]["name"]
            row["title"] = post["data"]["title"]
            row["coding"] = ""
            data.append(row)

    csv_columns = ['Name', 'title', 'coding']
    csv_filename = out_file

    with open(csv_filename, 'w') as csvfile:
        dict_writer = csv.DictWriter(csvfile, csv_columns, delimiter='\t')
        dict_writer.writeheader()
        dict_writer.writerows(data)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-o', '--out_file', help='output filepath in a tsv format')
    parser.add_argument('json_file', help='the path to file that contains posts')
    parser.add_argument('num_posts_to_output', nargs='?', help='number of posts to output')
    args = parser.parse_args()
    out_file = args.out_file
    json_file = args.json_file
    num_posts_to_output = args.num_posts_to_output

    with open(args.json_file, 'r') as handle:
        json_data = [json.loads(line) for line in handle]

    get_post(json_data, num_posts_to_output, out_file)


if __name__ == '__main__':
    main()
