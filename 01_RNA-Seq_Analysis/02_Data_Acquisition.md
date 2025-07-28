# Chapter 2: Finding and Acquiring Your Data

In Chapter 1, we covered the biological theory behind RNA-Seq. Now, we move from theory to practice. Most bioinformatics research involves analyzing publicly available data. This chapter will teach you how to find, evaluate, and download a real-world dataset for our tutorial.

### 2.1 A Global Library: Public Sequencing Repositories

When researchers publish a study using sequencing data, they are required to deposit their raw data into a public database. This is a cornerstone of reproducible science. The two most important repositories are:

*   **NCBI Gene Expression Omnibus (GEO):** A database focused on functional genomics data, excellent for browsing experiments by publication or biological context.
*   **European Nucleotide Archive (ENA):** A comprehensive repository for all nucleotide sequence data.

These databases, along with the DNA Data Bank of Japan (DDBJ), synchronize their data. A project submitted to one will be accessible through the others. We will use GEO and its connected **Sequence Read Archive (SRA)** for our example.

### 2.2 The Art of Searching for Data

Finding the right dataset is a critical skill. Your search should always be guided by your biological question.

1.  **Brainstorm Keywords:** Think about the key components of a potential experiment (e.g., organism, disease, technology, cell type).
2.  **Combine Keywords:** Use Boolean operators (`AND`, `OR`) to refine your search on the [NCBI GEO Datasets](https://www.ncbi.nlm.nih.gov/gds) website. For example: `("Homo sapiens"[Organism]) AND ("prostate cancer"[MeSH Terms]) AND ("Expression profiling by high throughput sequencing"[DataSet Type])`

### 2.3 The Quality Checklist: How to Evaluate a Dataset

Before you commit to a dataset, perform a quick quality check:

1.  **✅ Clear Objective:** Is the biological question clearly stated?
2.  **✅ Sound Experimental Design:** Is it a clean comparison (e.g., Treatment vs. Control)?
3.  **✅ Sufficient Replicates:** Are there at least **3 biological replicates** per condition? This is non-negotiable for statistical power.
4.  **✅ Correct Technology:** Is it short-read (Illumina) paired-end data? Paired-end is generally preferred for better alignment.
5.  **✅ Relevant Organism:** Is a high-quality reference genome available?

### 2.4 Case Study: Deconstructing Project PRJNA526724

Let's apply our checklist to the project we'll be using for this tutorial.

*   **Project Link:** [PRJNA526724 on NCBI BioProject](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA526724)
*   **Title:** *Transcriptome of human prostate cancer cells*
*   **Design:** *RNA was harvested... to study the basal transcriptome of LNCaP and 22rv1 cells...*

**Evaluation:** This project is a perfect fit. It's a clear comparison between two human prostate cancer cell lines (`LNCaP` vs. `22Rv1`) with multiple paired-end samples, allowing us to select three replicates for each condition.

### 2.5 Let's Get the Data: An Efficient and Robust Workflow

This section outlines a professional workflow to download and prepare the raw sequencing data.

#### Step 1: Install NCBI SRA-Tools
The SRA Toolkit is essential for accessing SRA data. You can install it manually or with Conda.

<details>
<summary><strong>Method A: Manual Installation (Recommended for Full Control)</strong></summary>

This method gives you direct control over the software version and location.

```bash
# Download the latest SRA Toolkit for Ubuntu Linux.
# Always check the official NCBI SRA Toolkit page for the most current link.
wget --output-document sratoolkit.tar.gz https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current-ubuntu64.tar.gz

# Unpack the archive
tar -vxzf sratoolkit.tar.gz

# IMPORTANT: Add the tools to your system's PATH.
# Replace the path below with the actual, absolute path to your unpacked sratoolkit folder.
export PATH="/path/to/your/sratoolkit.3.2.1-ubuntu64/bin:$PATH"

# Verify the installation by checking the version.
prefetch --version

# Optional but recommended: Run the interactive configuration for first-time setup.
vdb-config -i
```
</details>
<details>
    
<summary><strong>Method B: Using Conda (Easier)</strong></summary>
Conda handles the installation and path management for you, which is simpler for beginners.

```bash
# Install sra-tools into a dedicated conda environment
conda create -n sra-tools sra-tools -y

# Activate the environment every time you want to use the tools
conda activate sra-tools
```
</details>

#### Step 2: Prepare Your Workspace
Good organization is a hallmark of a good bioinformatician.
```bash
# Create our main project directory and subdirectories for data
mkdir -p rna-seq-project/data/{raw_fastq,sra}
cd rna-seq-project
```
Next, create a file named srr_ids.txt to list the samples we want. This is cleaner and more scalable than typing them on the command line. We'll use 3 replicates from each cell line.
```bash
# Create a file named srr_ids.txt with these contents:
SRR8757537
SRR8757538
SRR8757539
SRR8757543
SRR8757544
SRR8757545
```
#### Step 3: Create the Download & Processing Script
This script uses best practices: prefetch for robust downloading and fasterq-dump for speedy, multi-threaded conversion to FASTQ.

Create a file named download_data.sh and paste this code:
```bash
#!/bin/bash
# A robust script to download SRA data and convert it to compressed FASTQ files.

# This command ensures that the script will exit immediately if any command fails.
set -e

# --- Configuration ---
ID_FILE="srr_ids.txt"                  # File with SRA accession numbers.
OUTPUT_DIR="data/raw_fastq"            # Final directory for compressed FASTQ files.
SRA_DIR="data/sra"                     # Temporary directory for SRA downloads.
THREADS=6                              # Number of threads for fasterq-dump. Adjust for your system.

# --- Script Start ---
echo "Starting SRA data download and processing..."

# 1. Download SRA files using prefetch.
# 'prefetch' is a robust download manager that can resume interrupted downloads.
echo "Downloading SRA files listed in ${ID_FILE}..."
prefetch --option-file "${ID_FILE}" --output-directory "${SRA_DIR}"

# 2. Convert SRA files to FASTQ format.
echo "Converting SRA files to FASTQ using fasterq-dump..."
cat "${ID_FILE}" | while read sra_id; do
    echo "-------------------------------------------"
    echo "Processing ${sra_id}"

    # 'fasterq-dump' is a multithreaded and significantly faster alternative to fastq-dump.
    fasterq-dump "${SRA_DIR}/${sra_id}" -O "${OUTPUT_DIR}" -e "${THREADS}"

    # Compress the output FASTQ files to save space.
    echo "Compressing FASTQ files for ${sra_id}..."
    gzip "${OUTPUT_DIR}/${sra_id}"*.fastq

    echo "Finished processing ${sra_id}."
done

echo "-------------------------------------------"
echo "All processing complete."
echo "Final FASTQ files are in: ${OUTPUT_DIR}"
```
#### Step 4: Run the Script
Make the script executable and run it.

💡 **Pro Tip:** Use screen or tmux
Downloads can take a long time. If you're on a remote server, run the script inside a terminal multiplexer like screen or tmux. This allows the process to continue even if you get disconnected.
tmux new -s download_session
bash download_data.sh
(You can now safely detach with Ctrl+b then d)
```bash
chmod +x download_data.sh
./download_data.sh
```
#### Step 5: Validate the Downloads (CRITICAL STEP!)
Network glitches can corrupt files. A valid FASTQ file must have a line count that is perfectly divisible by 4. This step verifies integrity.
```bash
cd data/raw_fastq/

for file in *.fastq.gz; do
  # 'zcat' uncompresses on-the-fly, and 'wc -l' counts lines.
  lines=$(zcat "$file" | wc -l)
  
  # The modulo operator '%' checks for a remainder.
  if [ $((lines % 4)) -ne 0 ]; then
    echo "⚠️  CORRUPTED: $file (Line count: $lines - Not divisible by 4)"
  else
    echo "✅ Complete:   $file (Line count: $lines)"
  fi
done
```
If you find any ⚠️ CORRUPTED files, simply delete them (rm SRRXXXXXX*.fastq.gz) and re-run the download_data.sh script. The script is smart enough to only re-process the missing files.

#### Congratulations! You have successfully identified, downloaded, and validated a real-world RNA-Seq dataset using a professional and efficient workflow.

**Next Step:** In Chapter 3, we will perform a thorough Quality Control (QC) check on these raw FASTQ files using tools like FastQC and MultiQC to assess their quality before alignment.
