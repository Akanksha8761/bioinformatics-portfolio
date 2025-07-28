# Chapter 3: Quality Control of Raw Sequencing Data

### Objective
Raw sequencing data is never perfect. It contains technical artifacts, low-quality bases, and adapter sequences from the library preparation process. Before we can trust our analysis, we must first assess the quality of our raw data. This process is known as **Quality Control (QC)**.

In this chapter, we will use **FastQC** to inspect individual FASTQ files and the indispensable **MultiQC** to aggregate these results into a single, comprehensive report for easy comparison.

---

### Table of Contents
*   [3.1 What is FastQC?](#31-what-is-fastqc)
*   [3.2 Running the QC Workflow](#32-running-the-qc-workflow)
*   [3.3 A Deep Dive into the MultiQC Report](#33-a-deep-dive-into-the-multiqc-report)
    *   [3.3.1 Per Base Sequence Quality](#331-per-base-sequence-quality)
    *   [3.3.2 Per Tile Sequence Quality](#332-per-tile-sequence-quality)
    *   [3.3.3 Per Sequence Quality Scores](#333-per-sequence-quality-scores)
    *   [3.3.4 Per Base Sequence Content](#334-per-base-sequence-content)
    *   [3.3.5 Per Sequence GC Content](#335-per-sequence-gc-content)
    *   [3.3.6 Per Base N Content](#336-per-base-n-content)
    *   [3.3.7 Sequence Length Distribution](#337-sequence-length-distribution)
    *   [3.3.8 Sequence Duplication Levels](#338-sequence-duplication-levels)
    *   [3.3.9 Overrepresented Sequences](#339-overrepresented-sequences)
    *   [3.3.10 Adapter Content](#3310-adapter-content)
*   [3.4 Summary and Next Steps](#34-summary-and-next-steps)

---

### 3.1 What is FastQC?
**FastQC** is a cornerstone tool in bioinformatics. It reads raw FASTQ files and generates a detailed report on a wide range of quality metrics. It gives you a quick and thorough impression of whether your data has any problems before you proceed with analysis.

### 3.2 Running the QC Workflow

While you can run FastQC on each file individually, the professional standard is to use **MultiQC** to aggregate the results. This allows you to spot outliers and batch effects easily.

#### Step 1: Install Tools
If you haven't already, install FastQC and MultiQC into a dedicated conda environment.

```bash
conda create -n qc-tools fastqc multiqc -y
conda activate qc-tools
```
Step 2: Run FastQC and MultiQC

We will run FastQC on all our raw files and immediately pipe the results into MultiQC.

```bash
# Navigate to your main project directory
cd rna-seq-project

# Create an output directory for our QC results
mkdir -p analysis/qc_raw

# Run FastQC on all raw FASTQ files
# Note: Adjust the -t flag based on your system's CPU cores. 6-12 is a safe bet.
fastqc data/raw_fastq/*.fastq.gz -t 12 -o analysis/qc_raw/

# Run MultiQC on the directory containing the FastQC output
multiqc analysis/qc_raw/ -o analysis/qc_raw/
```

This will create a multiqc_report.html file inside analysis/qc_raw/. Open this file in your web browser. This single report is what we will now interpret.

### 3.3 A Deep Dive into the MultiQC Report

Below are the key plots from the MultiQC report and how to interpret them.
(Note: These are example images. You would replace these with screenshots from your own MultiQC report to make this a part of your portfolio.)

## 3.3.1 Per Base Sequence Quality

What it Shows: The distribution of quality scores at each position across the length of the reads. The Y-axis is the Phred Quality Score (higher is better).

How to Interpret It:

Green Zone (Good Quality, Q > 28): You want the median (central red line) and the interquartile range (yellow box) to remain high in this zone for most of the read.

Orange Zone (Reasonable Quality, Q > 20): Acceptable, but indicates lower confidence.

Red Zone (Poor Quality, Q < 20): These bases are unreliable and should be trimmed.

A dip in quality towards the 3' end of reads is normal and expected due to sequencing chemistry.

The thin blue line represents the mean quality. If it's very stable and high, it indicates excellent, consistent data.

Good Quality	Poor Quality (Needs Trimming)
	
## 3.3.2 Per Tile Sequence Quality

What it Shows: A heatmap of quality deviations across the sequencer's flow cell for each base position. This is for diagnosing technical issues with the sequencing run itself.

How to Interpret It:

Blue (Good): The plot should be predominantly blue, indicating no systematic quality issues tied to a specific physical location on the flow cell.

Warm Colors (Red/Orange): These indicate that certain tiles (physical areas) on the flow cell consistently produced lower-quality reads at specific cycles. This could be due to a bubble, a smudge, or other hardware issues. Usually, there's nothing you can do about this, but it's good to be aware of.

Good (All Blue)	Potential Issue
	
## 3.3.3 Per Sequence Quality Scores

What it Shows: The distribution of average quality scores per read. It answers the question: "How many reads have a high average quality?"

How to Interpret It: You want a single, sharp peak shifted far to the right, indicating that the vast majority of reads have a high average quality score (e.g., > 30). A peak shifted to the left or a broad peak indicates overall poor sequence quality.

## 3.3.4 Per Base Sequence Content

What it Shows: The percentage of each of the four bases (A, T, C, G) at each position across all reads.

How to Interpret It:

In a perfectly random library, the lines for A/T and G/C should be parallel and consistent throughout.

A common wobble at the start (first ~10-15 bp) is normal for RNA-Seq! This is a known bias caused by the random hexamer primers used during library preparation to initiate cDNA synthesis. It does not indicate a problem.

Significant divergence in the middle or end of the reads could suggest an overrepresented sequence (like an adapter).

Normal for RNA-Seq (Wobble at start)	Potential Issue (Bias later in reads)
	
## 3.3.5 Per Sequence GC Content

What it Shows: The distribution of GC content per read, compared to a theoretical normal distribution.

How to Interpret It: You should see a roughly normal, bell-shaped curve centered on the expected GC content for your organism. A sharp, secondary peak is a classic sign of contamination (e.g., an adapter dimer or DNA from another organism).

Normal GC Content	GC Content with Contamination
	
## 3.3.6 Per Base N Content

What it Shows: The percentage of bases that the sequencer could not confidently call, replacing them with an 'N'.

How to Interpret It: This plot should show a flat line at or very near zero. Any significant 'N' content indicates a problem with the sequencing run.

## 3.3.7 Sequence Length Distribution

What it Shows: The distribution of read lengths.

How to Interpret It: For standard Illumina data, you should see a single, sharp peak at the specified read length (e.g., 100 bp, 150 bp). If you see a wide distribution, it may mean you have already performed quality trimming.

## 3.3.8 Sequence Duplication Levels

What it Shows: The percentage of reads that are identical sequences.

How to Interpret It:

Low duplication (desirable): A high level of unique sequences. In RNA-Seq, some duplication is expected for highly expressed genes.

High duplication (potential issue): A high level suggests an "enrichment bias," often from too little starting material or too many PCR cycles during library prep. It can reduce the complexity of your library. This plot often shows a warning in RNA-Seq, and it's important to interpret it in the context of your experiment.

## 3.3.9 Overrepresented Sequences

What it Shows: A list of sequences that appear more than expected (typically >0.1% of the total).

How to Interpret It: The most common source of overrepresented sequences is adapter contamination. FastQC will often identify the sequence and tell you which known adapter it matches. This is a clear signal that adapter trimming is necessary.

## 3.3.10 Adapter Content

What it Shows: A cumulative plot of where known adapter sequences are found in the reads.

How to Interpret It: This plot should be empty. If you see rising percentages toward the 3' end, it confirms the presence of adapter sequences that must be removed before alignment.

### 3.4 Summary and Next Steps

After reviewing the QC report, we have a clear action plan. Our data shows:

A drop in quality at the 3' ends of the reads.

Significant adapter content.

These are typical findings for raw Illumina data and are precisely why we perform QC.

**Next Step:** In Chapter 4, we will use a trimming tool like fastp or Trim Galore! to clean our data by removing low-quality bases and adapter sequences. This will prepare clean, high-quality reads for the alignment step.

