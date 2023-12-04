import csv
import random
import os
import shutil


def get_random_number():
    number = random.random()
    if number < 0.7:
        return 1
    elif number < 0.9:
        return 2
    else:
        return 3


def main():
    with open("old_dataset/full_df.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            # print(row)
            filepath = 'old_dataset/ODIR-5K' + row[15][42:]

            label = row[16][2]

            filename = os.path.basename(filepath)
            folder = os.path.dirname(filepath)

            num = get_random_number()
            if num == 1:
                output_path = os.path.join("new_dataset/train/", label)
            elif num == 2:
                output_path = os.path.join("new_dataset/val/", label)
            elif num == 3:
                output_path = os.path.join("new_dataset/test/", label)

            output_filename = filename

            # Create the output directory if it doesn't exist
            if not os.path.exists(output_path):
                os.makedirs(output_path)
            print(os.path.join(output_path, output_filename))

            shutil.copy(filepath, os.path.join(output_path, output_filename))


if __name__ == "__main__":
    main()
