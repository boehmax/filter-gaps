from Bio import AlignIO
from Bio.Align import MultipleSeqAlignment
import sys

# Check for input arguments
if len(sys.argv) < 4:
    print("Usage: python filter_gaps.py <input_alignment> <output_alignment> <positions>")
    print("Positions: Comma-separated 1-based indices, e.g., 10,20,30")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]
positions = list(map(int, sys.argv[3].split(',')))

# Read the alignment
alignment = AlignIO.read(input_file, "fasta")

# Filter sequences
filtered_sequences = []
for record in alignment:
    # Check for gaps at important positions (convert to 0-based indices)
    if all(record.seq[pos - 1] != '-' for pos in positions):
        filtered_sequences.append(record)

# Create a MultipleSeqAlignment object from the filtered sequences
filtered_alignment = MultipleSeqAlignment(filtered_sequences)

# Write the filtered alignment
with open(output_file, "w") as out_f:
    AlignIO.write(filtered_alignment, out_f, "fasta")

print(f"Filtered alignment saved to {output_file}")
