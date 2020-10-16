#def to_rna(dna):
#    rna_dict = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
#    rna = ''
#  for elem in dna:
#        rna += rna_dict.get(elem, '')
#    return rna

# Альтернативный вариант с использованием map
# def to_rna(nucleotide):
#     return ''.join(map(MAPPING.get, nucleotide))

MAPPING = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U",
}

def to_rna(nucleotide):
    rna = []
    for item in nucleotide:
        rna.append(MAPPING[item])

    return ''.join(rna)

#def to_rna(dna):
#    rna = list(dna)
#    result = ''
#    for _ in rna:
#        if _ == 'G':
#            result = result + 'C'
#        if _ == 'C':
#            result = result + 'G'
#        if _ == 'T':
#            result = result + 'A'
#        if _ == 'A':
#            result = result + 'U'
#    return result