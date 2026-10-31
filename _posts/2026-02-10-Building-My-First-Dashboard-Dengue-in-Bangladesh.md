---
title: "Building My First Dashboard: Dengue Virus in Bangladesh"
date: 2026-02-10 12:00:00 +0600
categories: [Viral Genomics, Learning]
tags: [Dengue, R Shiny, Bioconductor, Bangladesh, Dashboards]
description: "I built an R Shiny dashboard for 13 dengue virus sequences from Bangladesh's 2023 outbreak. Here is what it showed, and what I would build differently now."
---

## TL;DR

In 2023, Bangladesh had its worst dengue year on record. I collected the **13 published dengue virus sequences** from that outbreak (12 from Dhaka, 1 from Chattogram), checked their quality in R, and built an interactive **Shiny dashboard** to explore them. All 13 are **DENV-2**, and the source studies place them in the **Cosmopolitan genotype**. It was my first real dashboard, and looking back, it also taught me what a proper viral genomics analysis needs. Code is on [GitHub](https://github.com/mdabrarfaiyaj/bangladeshi-dengue-strain-tracker), with the [live dashboard](https://u3j9z9-md0abrar-faiyaj.shinyapps.io/bangladesh-denv-tracker/).

## Why I picked this

Every monsoon in Dhaka comes with dengue. In 2023, hospitals were overflowing and almost everyone knew someone who got sick. I wanted my first viral genomics project to be about something I had lived through, not a textbook virus.

## Two steps: prototype, then the real thing

**Step 1: a prototype with reference genomes (January 2026).** I first built the whole pipeline on two standard reference genomes (DENV-1 and DENV-2 from NCBI RefSeq). The goal was only to learn: download sequences with a Bash script, run quality checks with Bioconductor, and connect everything to a Shiny app. The prototype is on [GitHub](https://github.com/mdabrarfaiyaj/dengue-variant-tracker-prototype), clearly labelled as a learning version.

**Step 2: real Bangladeshi sequences (February 2026).** Then I replaced the reference genomes with the real 2023 outbreak sequences:

- **12 sequences from Dhaka** (Nasif et al., 2024), each 7,472 bases of the virus's coding region
- **1 complete genome from Chattogram** (Hossain et al., 2025), 10,723 bases

## An analogy: a weather app for a virus

A weather app doesn't make it rain. It collects measurements, checks them, and shows them in a way people can understand at a glance. That's what a surveillance dashboard does for a virus: it turns sequences in a database into something a public health team can look at in a minute.

## What I did

1. **Quality control** with Biostrings: length, GC content and the number of unknown bases (N) for each sequence
2. **Motif counting**: how often short sequence patterns (like the start codon ATG or the poly-A signal AATAAA) appear
3. **A Shiny dashboard with 8 tabs**: summary, genomics, phylogenetic context, epidemiology, geography, timeline, motifs and the full data table

## What I found

- **All 13 sequences passed quality control.** None had unknown bases, and GC content was very similar in all of them (45.5–45.8%).
- **All 13 are DENV-2.** The two source studies place them in the **Cosmopolitan genotype**, a lineage that has spread widely across Asia.
- **The Dhaka sequences are almost identical** to each other in composition, which fits a single fast-spreading outbreak strain.

## What I would do differently now

Looking back with more experience, I want to be honest about the limits of this first version:

- **The "phylogeny" tab shows the published classification**, drawn as a diagram. It is not a tree I built myself. A real analysis would align the sequences with reference genomes for each genotype (for example with MAFFT) and build a tree (for example with IQ-TREE).
- **Counting short motifs isn't very informative.** A pattern like ATG appears hundreds of times in any genome by chance. Comparing each sequence with a reference to find real **mutations**, especially in the envelope (E) gene that antibodies target, would say much more.
- **13 sequences is a small window** on an outbreak with hundreds of thousands of cases.

That's not a reason to hide the project. It's a record of where I started, and the next version has a clear plan.

## Conclusion

This project taught me how to go from sequences in a database to a working, public dashboard, and that building the dashboard is the easy part. The hard part, and the science, is in the analysis behind it. Like a weather app, a virus dashboard is only as good as the measurements it shows.

## Citations

1. Nasif et al. *Microbiology Resource Announcements*. 2024. doi:[10.1128/mra.00162-24](https://doi.org/10.1128/mra.00162-24) (12 DENV-2 sequences from Dhaka, 2023)
2. Hossain et al. Complete genome sequence of dengue virus serotype 2 obtained from Chattogram, Bangladesh. *Microbiology Resource Announcements*. 2025. doi:[10.1128/mra.00023-25](https://doi.org/10.1128/mra.00023-25)
3. Pagès H, Aboyoun P, Gentleman R, DebRoy S. Biostrings: efficient manipulation of biological strings. Bioconductor R package.
