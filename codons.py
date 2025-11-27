def create_codon_dict(file_path):
    file = open(file_path)
    rows = file.readlines()
    file.close()
    codon_dict = {}
    for row in rows:
     cells = row.strip().split('\t')
     codon = cells [0]
     abbreviation = cells[2]
     codon_dict[codon] = abbreviation
    return codon_dict 
