def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    if not strand_a or not strand_b:
        return 0

    combined_strand = strand_a + strand_b

    hamming_distance = 0
    for index in range(0, len(strand_a)):
        if combined_strand[index] != combined_strand[len(strand_a) + index]:
            hamming_distance += 1
    return hamming_distance

    
