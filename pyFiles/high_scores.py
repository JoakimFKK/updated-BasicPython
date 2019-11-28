import csv

scores_path = r"doesntExist.csv"
hs_dict = {}

with open(scores_path, "r") as read_file:
    reader = csv.reader(read_file)
    for name, score in reader:
        score = int(score)
        if name in hs_dict:
            if hs_dict[name] < score:
                hs_dict[name] = score
        else:
            hs_dict[name] = score



for key, value in sorted(hs_dict.items()):
    print(f"{key} - {value}")