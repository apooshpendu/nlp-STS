import csv

sentence_pair={}
sentence_pair_list=[]
sentence1 = set()
sentence2 = set()
data_count = 0
all_count=0


filenames = ["Academia.csv", "Astronomy.csv", "Biology.csv", "Chemistry.csv", "Cooking.csv",
             "HomeImprovement.csv", "Interpersonal.csv", "MoviesTV.csv", "Physics.csv",
             "Puzzling.csv", "ScienceFiction.csv", "Statistics.csv", "Travel.csv", "Writing.csv"
             ]
for file in filenames:
    file = "Data\\" + file
    with open(file, mode="r", errors = "ignore") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                sentence_pair["Sentence1"] = row["Title1"]
                sentence_pair["Sentence2"] = row["Title2"]
                sentence_pair_list.append(sentence_pair.copy())
                sentence_pair.clear()
            line_count = line_count + 1
            all_count = all_count + 1
print("Raw data size: ",all_count)

with open('dataset.csv', mode='w', newline='') as csv_file:
    fieldnames = ['Sentence1', 'Sentence2', 'Gold Label', 'is_sts']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for pair in sentence_pair_list:
        sentence1 = set(pair["Sentence1"].split())
        sentence2 = set(pair["Sentence2"].split())
        if len(sentence1)>6 and len(sentence2)>6 and abs(len(sentence1)-len(sentence2))<5:
            if len(sentence1.intersection(sentence2))>=2:
                label = 1
            else:
                label = 0
            pair["Gold Label"] = label
            pair["is_sts"] = 0
            writer.writerow(pair)
            data_count = data_count+1

print("Final dataset size: ",data_count)
