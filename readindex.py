## open file and close if finished

with open ("sample.txt", encoding="utf-8") as f:
    for line in f:
        print(line)