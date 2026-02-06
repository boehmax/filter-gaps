# Filter Gaps in Multiple Sequence Alignment

<a href="https://doi.org/10.5281/zenodo.16736722"><img src="https://zenodo.org/badge/759921808.svg" alt="DOI"></a>

This Python script filters out sequences from a multiple sequence alignment (in FASTA format) that contain gaps (-) at specified positions.
## Requirements

- Python 3
- Biopython (pip install biopython)

## Usage

python filter_gaps.py <input_alignment> <output_alignment> <positions>

### Parameters:

- <input_alignment>: Path to the input FASTA alignment file.
- <output_alignment>: Path to the output file where the filtered alignment will be saved.
- <positions>: Comma-separated list of 1-based column positions to check for gaps (e.g., 10,20,30).

### Example:

python filter_gaps.py aligned_sequences.fasta filtered_output.fasta 15,32,88

This will output all sequences that do not have a gap at positions 15, 32, or 88.

## Output

A new FASTA file containing only the sequences without gaps at the specified positions.
## License

This script is provided as-is without any warranty. You are free to use and modify it.
