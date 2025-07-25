# Chapter 2: Finding and Acquiring Your Data

In Chapter 1, we covered the biological theory behind RNA-Seq. Now, we move from theory to practice. Most bioinformatics research, especially during a PhD, involves analyzing publicly available data. This chapter will teach you how to find, evaluate, and download a dataset for our tutorial.

### 2.1 A Global Library: Public Sequencing Repositories

When researchers publish a study using sequencing data, they are required to deposit their raw data into a public database. This is fantastic for the scientific community, as it allows others to verify the results and explore the data for new discoveries.

The two most important repositories are:
*   **NCBI Gene Expression Omnibus (GEO):** A database focused on functional genomics data, including RNA-Seq and microarrays. It's excellent for browsing experiments by publication or biological context.
*   **European Nucleotide Archive (ENA):** A comprehensive repository for all nucleotide sequence data.

These databases, along with the DNA Data Bank of Japan (DDBJ), synchronize their data. A project submitted to one will typically be accessible through the others. We will use GEO and its connected **Sequence Read Archive (SRA)** for our example.

### 2.2 The Art of Searching for Data

Finding the right dataset is a skill. Your search should be guided by your biological question.

**Step 1: Brainstorm Keywords**
Think about the key components of a potential experiment:
*   **Organism:** `Homo sapiens`, `Mus musculus`, `Arabidopsis thaliana`
*   **Disease/Condition:** `prostate cancer`, `alzheimer's disease`, `drought stress`
*   **Technology:** `RNA-Seq`, `transcriptome`, `next generation sequencing`
*   **Cell Type/Tissue:** `LNCaP cells`, `neuron`, `root tissue`
*   **Treatment:** `steroid deprivation`, `drug treatment`

**Step 2: Combine Keywords**
Use Boolean operators (`AND`, `OR`) to refine your search on the [NCBI GEO Datasets](https://www.ncbi.nlm.nih.gov/gds) website.

For example, a search for our project might look like this:
`("Homo sapiens"[Organism]) AND ("prostate cancer"[MeSH Terms]) AND ("Expression profiling by high throughput sequencing"[DataSet Type])`

### 2.3 The Quality Checklist: How to Evaluate a Dataset

Not all datasets are created equal. Before you download gigabytes of data, you must evaluate the project to see if it's suitable for your analysis.

Here is a checklist:
1.  **✅ Clear Objective:** Does the project summary clearly state the biological question?
2.  **✅ Sound Experimental Design:** Is it a simple, clean comparison? (e.g., Treatment vs. Control). Are the groups well-defined?
3.  **✅ Sufficient Replicates:** Are there at least 3 biological replicates for each condition? This is crucial for statistical power. More is better.
4.  **✅ Correct Technology:** Is it actually RNA-Seq? Is it short-read (Illumina) or long-read? Is it paired-end or single-end? Paired-end is generally preferred as it provides more robust alignment.
5.  **✅ Relevant Organism:** Is it the organism you want to study? Is a high-quality reference genome available for it?

### 2.4 Case Study: Deconstructing Project PRJNA526724

Let's apply our checklist to the project we'll be using for this tutorial.

**Project Link:** [PRJNA526724 on NCBI BioProject](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA526724)

-   **Title:** *Transcriptome of human prostate cancer cells*
-   **Overall Design:** *RNA was harvested after 72h of steroid deprivation to study the basal transcriptome of LNCaP and 22rv1 cells, two human AR-positive prostate cancer cell lines.*

Let's evaluate it:

1.  **Objective:** Very clear. The goal is to compare the baseline transcriptome of two different prostate cancer cell lines (LNCaP and 22Rv1).
2.  **Experimental Design:** Excellent. It's a straightforward comparison between two groups: `LNCaP` vs. `22Rv1`.
3.  **Replicates:** The project page links to the SRA Run Selector, which shows there are 9 samples in total. We will need to investigate further to see the breakdown per group.
4.  **Technology:** The project description specifies "RNA-seq."
5.  **Organism:** Human (`Homo sapiens`). A high-quality reference genome is readily available.

**Conclusion:** This dataset is an excellent candidate for a differential gene expression tutorial.

### 2.5 Let's Get the Data: Downloading from the SRA

Now for the fun part: downloading the raw data to our Linux environment. We will use a toolkit from NCBI called **SRA-Tools**.

#### Step 1: Install SRA-Tools
The best way to install bioinformatics software is with `conda`. If you don't have it, please install [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/).

```bash
# Install sra-tools into its own conda environment
conda create -n sra-tools sra-tools -y

# Activate the environment
conda activate sra-tools

Step 2: Get the Sample Accession List

Go to the SRA Run Selector for PRJNA526724.

You will see a table of all the samples in this project. Each sample has a unique ID that starts with SRR.

In the "Layout" column, we see PAIRED, confirming this is paired-end data.

From the "Sample Name" column, we can see which samples belong to which cell line. Let's pick 3 replicates for each to keep our analysis manageable.

LNCaP: SRR8757537, SRR8757538, SRR8757539

22Rv1: SRR8757543, SRR8757544, SRR8757545

Step 3: Download and Extract the Data with a Script

We will write a simple shell script to download these 6 samples. First, let's create a directory to hold our raw data.

Generated bash
mkdir -p rna-seq-project/data/raw_fastq
cd rna-seq-project/data/raw_fastq

Now, create a script called download_data.sh and paste the following content into it.

Generated bash
#!/bin/bash
# A script to download and extract FASTQ files for our project.

# Ensure we are in the sra-tools environment
# conda activate sra-tools

echo "Starting download process..."

# List of SRA accession numbers for our 6 samples
sra_numbers=(
    "SRR8757537" "SRR8757538" "SRR8757539" # LNCaP samples
    "SRR8757543" "SRR8757544" "SRR8757545" # 22Rv1 samples
)

# Loop through the accession numbers
for sra in "${sra_numbers[@]}"
do
    echo "-------------------------------------------"
    echo "Processing sample: ${sra}"

    # 1. Download the SRA file
    # 'prefetch' is a tool from sra-tools that robustly downloads data.
    echo "Downloading ${sra}..."
    prefetch "${sra}"

    # 2. Convert the SRA file to paired-end FASTQ files
    # '--split-files' creates separate files for read 1 and read 2 (_1.fastq.gz and _2.fastq.gz)
    # '--gzip' compresses the output to save space
    echo "Converting ${sra} to FASTQ..."
    fastq-dump --split-files --gzip "${sra}/${sra}.sra"

    echo "Finished processing ${sra}."
    echo "-------------------------------------------"
done

echo "All downloads and conversions are complete."

Step 4: Run the Script

Save the file and make it executable. Then, run it.

Generated bash
chmod +x download_data.sh
./download_data.sh

Pro Tip: Use screen or tmux
These downloads can take a long time and require a stable internet connection. If you are working on a remote server, it is highly recommended to run the download script inside a screen or tmux session. This allows the process to continue running even if you get disconnected.

After the script finishes, you will have 12 files in your raw_fastq directory (2 for each of the 6 samples), for example:

SRR8757537_1.fastq.gz

SRR8757537_2.fastq.gz

...and so on.

Congratulations! You have successfully identified, evaluated, and downloaded a real-world RNA-Seq dataset. You now have the raw material for our analysis.

Next Step: In the next chapter, we will perform a critical Quality Control (QC) check on these raw FASTQ files to ensure they are suitable for analysis.
