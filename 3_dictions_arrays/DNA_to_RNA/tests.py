import dna 

def test_to_rna():
    assert dna.to_rna("C") == "G"
    assert dna.to_rna("G") == "C"
    assert dna.to_rna("T") == "A"
    assert dna.to_rna("A") == "U"
    assert dna.to_rna("ACGTGGTCTTAA") == "UGCACCAGAAUU"
    print('test_to_rna is Ok!')

test_to_rna()