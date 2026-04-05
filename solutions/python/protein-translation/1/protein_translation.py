def proteins(strand):
    codon_map = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP"
}
    result = []
    for index in range(0, len(strand), 3):
        strand_slice = strand[index: index + 3]
        if codon_map[strand_slice] == "STOP":
            break
        result.append(codon_map[strand_slice])
        
    return result
