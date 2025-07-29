# Chapter 4: Trimming and Filtering Raw Data

### Objective
In Chapter 3, our Quality Control (QC) analysis revealed common issues in raw sequencing data: the presence of **adapter sequences** and a drop in **base quality**. This chapter details the crucial "cleaning" step of trimming and filtering our reads to prepare them for accurate downstream analysis.

A good trimming strategy aims to keep reads with a **Phred quality score > 20** and a **read length > 36 bp** (a common minimum for reliable alignment).

---

### Table of Contents
*   [4.1 The "Why": Rationale for Trimming](#41-the-why-rationale-for-trimming)
*   [4.2 Anatomy of an Adapter and How Contamination Occurs](#42-anatomy-of-an-adapter-and-how-contamination-occurs)
*   [4.3 Choosing Your Trimming Tool: fastp vs. Trimmomatic vs. Trim Galore!](#43-choosing-your-trimming-tool-fastp-vs-trimmomatic-vs-trim-galore)
*   [4.4 The Recommended Workflow: Using `fastp`](#44-the-recommended-workflow-using-fastp)
*   [4.5 Alternative Workflows: Trimmomatic and Trim Galore!](#45-alternative-workflows-trimmomatic-and-trim-galore)
*   [4.6 The Final, Crucial Step: Post-Trimming QC](#46-the-final-crucial-step-post-trimming-qc)
*   [4.7 Summary and Next Steps](#47-summary-and-next-steps)

---

### 4.1 The "Why": Rationale for Trimming
We trim our data to address issues that arise from technical limitations of the sequencing process.
*   **Causes of Poor Quality:** Low-quality bases can result from sequencing errors, PCR amplification bias during library prep, or poor initial sample quality.
*   **Impact of Contamination:** If not removed, adapter sequences can prevent reads from aligning to the genome or cause them to align to the wrong location, leading to inaccurate results.

### 4.2 Anatomy of an Adapter and How Contamination Occurs
An **adapter** is a synthetic DNA sequence ligated to our RNA/cDNA fragments during library preparation. It's a multi-purpose tool containing:
*   Sequences for binding the fragment to the sequencer's flow cell.
*   Primer binding sites for initiating the sequencing reaction.
*   Index/barcode sequences for multiplexing (pooling multiple samples in one run).

**Adapter contamination** happens when the DNA insert is shorter than the number of bases being sequenced. The sequencer reads through the entire DNA fragment and continues into the adapter sequence on the other side.


Long Insert:
<--Read 1--> [ DNA FRAGMENT ] <--Read 2--> (No contamination)

Short Insert ("Read-Through"):
<--Read 1--> [ DNA ]-->ADAPTER-->... (Contamination in Read 1)

Generated code
### 4.3 Choosing Your Trimming Tool: fastp vs. Trimmomatic vs. Trim Galore!

| Feature                      | fastp (Modern All-in-One)                               | Trimmomatic (Classic Workhorse)                        | Trim Galore! (Wrapper)                                  |
| ---------------------------- | ------------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------- |
| **Main Function**            | QC, adapter trimming, quality filtering in one command. | Adapter trimming and quality filtering.                | A wrapper for `Cutadapt` and `FastQC`.                  |
| **Adapter Detection**        | **Automatic** for standard Illumina kits.               | Requires user to provide an adapter FASTA file.        | Automatic for standard Illumina kits.                   |
| **Trimming Modes**           | Quality-based, length, complexity filtering.            | "Simple" and "Palindrome" modes for adapter finding.   | Uses `Cutadapt` for error-tolerant adapter finding.     |
| **Quality Trimming**         | Sliding window, quality filtering, N-base filtering.    | Sliding window, leading/trailing base quality.         | Base quality filtering.                                 |
| **Speed**                    | **Very fast**, fully multithreaded.                     | Multithreaded.                                         | Slower, as `Cutadapt` is single-threaded.               |
| **Output**                   | Trimmed FASTQ, detailed HTML & JSON reports.            | Trimmed FASTQ files only.                              | Trimmed FASTQ and optional `FastQC` reports.            |
| **Best For**                 | **The recommended starting point for most users.**      | Fine-grained control, established pipelines.           | Simplicity and integrating `Cutadapt` with `FastQC`.    |

### 4.4 The Recommended Workflow: Using `fastp`
`fastp` is the preferred tool for this tutorial because it's fast, efficient, and combines trimming and QC into a single step.

#### Step 1: Install `fastp`
```bash
conda activate qc-tools
conda install -c bioconda fastp -y
```
Step 2: Run fastp with a Loop

This script will iterate through all our paired-end samples and process them.
```bash
Generated bash
# Navigate to your main project directory
cd rna-seq-project

# Create output directories
mkdir -p analysis/trimmed_fastq analysis/fastp_reports

# Loop through each sample pair
for read1 in $(ls -1 data/raw_fastq/*_1.fastq.gz); do
    read2=$(echo ${read1} | sed 's/_1.fastq.gz/_2.fastq.gz/')
    samplename=$(basename ${read1} _1.fastq.gz)

    echo "--- Processing sample: ${samplename} ---"

    fastp \
        -i ${read1} \
        -I ${read2} \
        -o analysis/trimmed_fastq/${samplename}_1.trimmed.fastq.gz \
        -O analysis/trimmed_fastq/${samplename}_2.trimmed.fastq.gz \
        --html analysis/fastp_reports/${samplename}.html \
        --json analysis/fastp_reports/${samplename}.json \
        --thread 12 \
        --length_required 36
done
```
### 4.5 Alternative Workflows: Trimmomatic and Trim Galore!

Understanding how to use other popular tools is a valuable skill. Below are example commands for Trimmomatic and Trim Galore!.

<details>
<summary><strong>Click here for the Trimmomatic Workflow</strong></summary>


Trimmomatic offers fine-grained control with its two main adapter trimming modes:

Simple Mode: Detects adapters by finding an approximate match between the read and a user-provided adapter sequence. It works on a "seed and extend" approach.

Palindrome Mode: Specifically for paired-end data to detect "adapter read-through." It aligns the read pairs to each other to find overlapping regions, which provides higher sensitivity and specificity for this type of contamination.

Example Loop for Paired-End Reads:

⚠️ Important Note: The HEADCROP and CROP parameters used below are very aggressive and generally not recommended for standard analysis, as they unconditionally remove data. It is better to rely on adaptive quality trimming (SLIDINGWINDOW, LEADING, TRAILING). This example is provided for educational purposes.
```bash
Generated bash
# Create an output directory
mkdir -p analysis/trimmomatic_output

# Loop through paired-end files
ls data/raw_fastq/*_1.fastq.gz | cut -d'_' -f1 | sort -u | while read i; do
  java -jar /path/to/trimmomatic.jar PE \
    -threads 12 -phred33 \
    ${i}_1.fastq.gz ${i}_2.fastq.gz \
    analysis/trimmomatic_output/${i}_1_paired.fastq.gz analysis/trimmomatic_output/${i}_1_unpaired.fastq.gz \
    analysis/trimmomatic_output/${i}_2_paired.fastq.gz analysis/trimmomatic_output/${i}_2_unpaired.fastq.gz \
    ILLUMINACLIP:/path/to/adapters/NexteraPE-PE.fa:2:30:10 \
    LEADING:20 TRAILING:20 SLIDINGWINDOW:4:20 MINLEN:36
done
```
</details>

<details>
<summary><strong>Click here for the Trim Galore! Workflow</strong></summary>


Trim Galore! is a convenient wrapper around Cutadapt (for trimming) and FastQC (for QC).

Example Loop for Paired-End Reads:

⚠️ Important Note: The --clip_R1 and --three_prime_clip_R1 parameters are forms of hard-clipping and should be used with caution. It's often better to let quality-based trimming handle this dynamically.
```bash
Generated bash
# Create an output directory
mkdir -p analysis/trim_galore_output

# Loop through paired-end files
ls data/raw_fastq/*_1.fastq.gz | cut -d'_' -f1 | sort -u | while read i; do
  trim_galore --quality 20 --paired ${i}_1.fastq.gz ${i}_2.fastq.gz \
    --fastqc --cores 8 -o analysis/trim_galore_output/
done
```
</details>

### 4.6 The Final, Crucial Step: Post-Trimming QC

How do we know if our trimming worked? We run FastQC and MultiQC again on the clean data. This is a non-negotiable step to verify your work and generate the "after" plots for your report.
```bash
Generated bash
# Create a new QC directory for the trimmed data
mkdir -p analysis/qc_trimmed

# Run FastQC on the trimmed files (produced by fastp)
fastqc analysis/trimmed_fastq/*.trimmed.fastq.gz -t 12 -o analysis/qc_trimmed/

# Run MultiQC on the new reports to get a final summary
multiqc analysis/qc_trimmed/ -o analysis/qc_trimmed/
```
### 4.7 Summary and Next Steps

By using fastp, we have efficiently removed adapter sequences and low-quality bases from our raw data. Our post-trimming QC report confirms that the data is now of high quality, with technical artifacts removed.

**Next Step:** In Chapter 5, we are finally ready for the main event: aligning our clean reads to the human reference genome using a splice-aware aligner like STAR.
