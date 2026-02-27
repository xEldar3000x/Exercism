dictionary  = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U"
}

def to_rna(dna_strand):
    
    if dna_strand.isalpha():

        rules_table = str.maketrans(dictionary)
        
        result = dna_strand.translate(rules_table)

        return result
        
    return dna_strand
