l = []
with open('metabolic_process_annotations.txt') as infile:
    for line in infile:
        l.append('4932.'+line.split()[1])
print(l)