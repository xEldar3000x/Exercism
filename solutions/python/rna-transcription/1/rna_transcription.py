dictionary  = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U"
}

def to_rna(dna_strand):
    
    if dna_strand.isalpha():

        t = str.maketrans(dictionary)
        
        res = dna_strand.translate(t)

        return res
        
    return dna_strand
