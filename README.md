# 16S-rRNA-sequence-analysis
Python and BLAST analysis of a Pseudomonas aeruginosa 16S rRNA gene (NR_113599.1): sequence statistics, GC content, reverse complement and BLAST interpretation. Beginner bioinformatics learning project.
# 16S rRNA Sequence Analysis of *Pseudomonas aeruginosa*

A beginner bioinformatics project using Python and NCBI BLAST to analyze a bacterial 16S rRNA gene sequence.

## Question
What are the basic properties of the *P. aeruginosa* 16S rRNA gene (length, base composition, GC content), and which organisms does it match in a BLAST search?

## Background
The 16S rRNA gene is part of the bacterial ribosome. It is highly conserved, so it is widely used to identify bacteria and compare their relationships. This project is a learning exercise to practise the basic steps of a sequence analysis workflow.

## Data
- Source: NCBI Nucleotide (RefSeq)
- Accession: **NR_113599.1**
- Record: *Pseudomonas aeruginosa* strain NBRC 12689, 16S ribosomal RNA, partial sequence
- Format: FASTA (`data/p_aeruginosa_16S.fasta`)

## Methods
1. Downloaded the FASTA record from NCBI.
2. Wrote Python scripts (no external libraries) to:
   - read the FASTA file (`scripts/read_fasta.py`)
   - count nucleotides and calculate GC content (`scripts/analyze_sequence.py`)
   - generate the reverse complement and check it by reversing it again (`scripts/reverse_complement.py`)
3. Ran NCBI BLASTN (web) against the 16S rRNA type strains database.

## Results

### Sequence statistics
| Measure | Value |
|---|---|
| Length | 1,461 bp |
| A | 371 |
| T | 297 |
| G | 463 |
| C | 330 |
| Other letters | 0 |
| GC content | 54.28% |

The counts of A and T (and of G and C) differ because the file holds a single strand. In double-stranded DNA they would match.

### BLAST top hits
| Hit | Accession | Identity | Query cover | E value |
|---|---|---|---|---|
| *P. aeruginosa* DSM 50071 | NR_117678.1 | 100% | 100% | 0.0 |
| *P. aeruginosa* NBRC 12689 (the query itself) | NR_113599.1 | 100% | 100% | 0.0 |
| *P. aeruginosa* ATCC 10145 | NR_114471.1 | 100% | 100% | 0.0 |
| *Metapseudomonas otitidis* | NR_043289.1 | 98.63% | 100% | 0.0 |
| *Metapseudomonas lalkuanensis* | NR_179771.1 | 98.08% | 100% | 0.0 |
| *Pseudomonas tohonis* | NR_179382.1 | 98.02% | 100% | 0.0 |

Full table: see the BLAST hit table CSV and screenshot in `results/`.

## Interpretation
- The sequence matches *P. aeruginosa* references with 100% identity over its whole length.
- E values are all 0.0, so they cannot separate the hits here. Percent identity and query cover are more informative.
- The next-closest hits are 98-98.6% identical but belong to other species. 16S is a strong tool for genus-level identification but has limited power to separate closely related species, and none for strains.
- The GC content (54.28%) is lower than the *P. aeruginosa* whole genome (about 66%). This is consistent with the 16S gene being strongly conserved.

## Limitations
- This was a test of the workflow using a reference sequence. The query is itself in the database, so the result is expected and is not an identification of an unknown isolate.
- The sequence is partial (1,461 bp), not full length.
- 16S cannot distinguish strains and says nothing about virulence or resistance genes.
- BLAST was run once on the web with default settings, and I did not build an alignment or phylogenetic tree.
- Taxonomy is being revised (for example the genera *Metapseudomonas*, *Aquipseudomonas* and *Stutzerimonas*), so names may differ between databases.

## Repository structure
```
├── data/        FASTA file
├── scripts/     Python scripts
├── results/     BLAST hit table, screenshot, summary
└── README.md
```

## How to run
Requires Python 3. From the project folder (Windows):
```
py -3 scripts\read_fasta.py
py -3 scripts\analyze_sequence.py
py -3 scripts\reverse_complement.py
```

## What I learned
Reading FASTA files in Python, calculating GC content, working with dictionaries and loops, running and interpreting BLAST, and documenting a project.
