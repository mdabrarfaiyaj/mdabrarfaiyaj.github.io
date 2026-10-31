"""
make_projects_section.py
Replaces the "Research Notes" section of the homepage with a Mike-style
"Featured Work / Projects" section: one card per top project, each with a GitHub link.
The menu item "research notes" becomes "projects".

To add or remove a project later, edit the PROJECTS list below and run the script again.

Run from your portfolio folder:   python make_projects_section.py
"""
from pathlib import Path

GH = "https://github.com/mdabrarfaiyaj/"

# (label, title, one-line description, repo name)
PROJECTS = [
    ("Python · Structural Bioinformatics", "Cancer Mutation Hotspots in 3D",
     "Maps TCGA tumor mutations in TP53, KRAS and PIK3CA onto PDB and AlphaFold structures, "
     "with 3D clustering tests and interactive viewers.",
     "cancer-mutation-3d-hotspots"),
    ("Nextflow Pipeline", "Bacterial Pangenome & AMR Pipeline",
     "Nextflow DSL2 workflow for genome QC, annotation, pangenome construction, "
     "resistance-gene detection and core-genome phylogeny.",
     "human-gut-bacterial-pangenome-analysis"),
    ("R · Shiny · Quarto", "Typhoid AMR Surveillance, Bangladesh",
     "Reanalysis of 12,435 Salmonella Typhi isolates and 1,664 genomes, "
     "with an interactive dashboard and a reproducible report.",
     "Typhoid-Fever-in-Bangladesh"),
    ("R · DESeq2 · Shiny", "RNA-seq Pipeline & Dashboard",
     "Bulk RNA-seq from raw reads to differential expression (HISAT2, featureCounts, DESeq2), "
     "with an interactive dashboard that accepts your own data.",
     "rna-seq-shiny-pipeline"),
    ("R · Single Cell", "Metastatic Breast Cancer Atlas",
     "Single-cell and single-nucleus reanalysis with Harmony integration, "
     "pseudobulk profiles and variance partitioning.",
     "sc-snRNA-seq-metastatic-breast-cancer"),
    ("R · Shiny · Bioconductor", "Dengue Strain Tracker",
     "Quality control and an interactive dashboard for DENV-2 sequences "
     "from the 2023 outbreak in Bangladesh.",
     "bangladeshi-dengue-strain-tracker"),
]

cards = "".join(
    f'<div class="proj-card"><div class="proj-meta">{label}</div><h3>{title}</h3>'
    f'<p>{desc}</p><a class="proj-link" href="{GH}{repo}" target="_blank" rel="noopener">'
    f'View on GitHub &rarr;</a></div>'
    for label, title, desc, repo in PROJECTS
)

SECTION = (
    '<section class="section" id="projects"><div class="container">'
    '<span class="eyebrow">Featured Work</span><h2>Projects</h2>'
    '<p class="muted">Open-source tools and reproducible pipelines for the bioinformatics community.</p>'
    f'<div class="proj-grid">{cards}</div>'
    f'<a class="proj-all" href="{GH}?tab=repositories" target="_blank" rel="noopener">All repositories on GitHub &rarr;</a>'
    '</div><style>'
    '.proj-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:18px;margin-top:26px}'
    '.proj-card{display:flex;flex-direction:column;gap:10px;background:var(--surface);border:1px solid var(--line);'
    'border-radius:9px;padding:22px;transition:transform .2s,border-color .2s}'
    '.proj-card:hover{border-color:var(--accent);transform:translateY(-2px)}'
    ".proj-meta{font:11px 'JetBrains Mono',monospace;text-transform:uppercase;letter-spacing:.08em;color:var(--accent)}"
    '.proj-card h3{font-size:17px;line-height:1.35;margin:0}'
    '.proj-card p{font-size:13.5px;color:var(--dim);margin:0;flex-grow:1}'
    ".proj-link{font:12px 'JetBrains Mono',monospace;color:var(--accent);margin-top:4px}"
    ".proj-all{display:inline-block;margin-top:24px;border:1px solid var(--line);padding:9px 14px;border-radius:5px;"
    "font:12px 'JetBrains Mono',monospace}"
    '.proj-all:hover{border-color:var(--accent)}'
    '</style></section>'
)

p = Path("index.html")
h = p.read_text(encoding="utf-8")

for sid in ('id="projects"', 'id="notes"'):        # update in place if run again
    i = h.find(sid)
    if i != -1:
        s = h.rfind("<section", 0, i)
        e = h.find("</section>", i) + len("</section>")
        h = h[:s] + SECTION + h[e:]
        break
else:
    raise SystemExit("Could not find the Research Notes section - nothing changed.")

h = h.replace('<a href="#notes">research notes</a>', '<a href="#projects">projects</a>')
h = h.replace('href="#notes"', 'href="#projects"')
p.write_text(h, encoding="utf-8")
print(f"Featured Work section added with {len(PROJECTS)} projects.")
