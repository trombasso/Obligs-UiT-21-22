# Iterating through input, if string countains valid gene-strings it outputs result.
def check_if_gene(genome):
    genome_start = 0
    genome_end = len(genome)
    genome_length = len(genome)
    sequenze = []
    start_point = []
    end_point = []
    positive_pos = 100000

    # Checkloop, continues as long as ATG is found in string.
    while "ATG" in genome[genome_start:genome_length]:
        genome_start += genome[genome_start:genome_length].find("ATG") + 3
        x = genome[genome_start:genome_length]
        if x.find("ATG") != -1:
            ATG_pos = x.find("ATG") + genome_start + 1
        else:
            ATG_pos = positive_pos

        if x.find("TAG") != -1:
            TAG_pos = x.find("TAG") + genome_start + 1
        else:
            TAG_pos = positive_pos

        if x.find("TAA") != -1:
            TAA_pos = x.find("TAA") + genome_start + 1
        else:
            TAA_pos = positive_pos

        if x.find("TGA") != -1:
            TGA_pos = x.find("TGA") + genome_start + 1
        else:
            TGA_pos = positive_pos

        if ATG_pos == positive_pos and TAA_pos == positive_pos and TGA_pos == positive_pos and TAG_pos == positive_pos:
            break

        if ATG_pos < TAA_pos and ATG_pos < TGA_pos and ATG_pos < TAG_pos:
            genome_start = ATG_pos + 3
            continue
        elif TAG_pos < ATG_pos and TAG_pos < TAA_pos and TAG_pos < TGA_pos:
            genome_end = TAG_pos - 1
        elif TAA_pos < ATG_pos and TAA_pos < TAG_pos and TAA_pos < TGA_pos:
            genome_end = TAA_pos - 1
        elif TGA_pos < ATG_pos and TGA_pos < TAA_pos and TGA_pos < TAG_pos:
            genome_end = TGA_pos - 1

        if len((genome[genome_start:genome_end])) % 3 == 0:
            sequenze.append(genome[genome_start:genome_end])
            start_point.append(genome_start)
            end_point.append(genome_end)
        genome_start = genome_end

    if sequenze:
        print(f"\nGen strings found in {len(genome)} chars provided:")
        print("---------------------------------------------------")
        for x in range(0, len(sequenze)):
            print(start_point[x], sequenze[x], end_point[x])
        print(f"\n\nTotal number of strings found: {len(sequenze)}.")
        print("---------------------------------------------------")
    else:
        print("\nNo gene found.\n")


def main():
    # genome = input("Enter a genome string: ").upper()

    # genome = (
    #     "atggctcttcttaaggccaataaggatctcatttccgcaggattgaaggagttcagcgttctgctgaatcagcaggtcttcaatgatcctctcgtctctgaagaagacatggtgactgtggtggaggactggatgaacttctacatcaactattacaggcagcaggtgacaggggagccccaagagcgagacaaggctctgcaggagcttcggcaagagctgaacactctggccaaccctttcctggccaagtacagggacttcctgaagtctcatgagctcccgagtcacccaccgccctcctcctag"
    # ).upper()

    # genome = "TTATGTTTTAAGGATGGGGCGTTAGTT"

    genome = (
        "atgaaaaaagcaaaattattcggttttagtttgattgcattaggtttatcagtttcacttgcagcatgtggtggtggcaaaggcaaaaccgctgaaagcggcggtggcaaaggggatgcagcgcatagtgctgtaatcattacagatacaggcggcgtggatgacaagtcgttcaaccaatcttcttgggaaggattgcaagcttggggtaaagaacatgatttaccagaaggttcaaaagggtatgcatatattcaatcgaatgatgcagctgactatacaaccaatattgaccaagcggtatcaagtaaattcaacacaatctttggtattggctacttgctaaaagatgcaatttcttctgcagcagatgccaaccctgatacaaactttgttttaatcgatgatcaaatcgatggcaaaaagaatgtcgtttctgcaacatttagagataatgaagcagcttacttagccggtgttgctgctgcaaatgaaacaaaaacgaacaaagtcggttttgttggtggtgaagaaggggtcgtaattgaccgtttccaagctggttttgaaaaaggtgtggctgatgctgcgaaagaattaggtaaagaaattactgttgatacgaaatatgcggcttcatttgctgatcctgccaaagggaaagctttagctgctgcaatgtaccaaaacggcgttgatatcatcttccatgcttctggtgcgactggacaaggggtcttccaagaagcaaaagacttgaatgaatcaggttctggcgacaaagtttgggtaatcggcgttgaccgcgatcaagatgctgatggcaagtacaaaacaaaagacggcaaagaagacaacttcacgttaacttcaacgcttaaaggtgtcggcacagcggttcaagatattgccaaccgtgcgttagaagacaaattccctggtggcgaacatttagtttatggattaaaagatggtggcgttgacttaacagacggctatttaaacgacaaaacaaaagaagctgttaaaacagcaaaagataaagtaatctcaggtgacgtaaaagtcccagaaaaaccagaataa"
    ).upper()

    check_if_gene(genome)


if __name__ == "__main__":
    main()
