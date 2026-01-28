# JAVELIN.AI

**AI-Powered Clinical Trial Data Quality Intelligence Platform**

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: Competition](https://img.shields.io/badge/license-NEST%202.0-orange.svg)](#license)

JAVELIN.AI is an end-to-end solution for monitoring, analyzing, and improving clinical trial data quality across multi-site global studies. It implements ICH E6(R2) risk-based quality management through a 9-phase analytical pipeline.

**Built for the NEST 2.0 Innovation Challenge** (Problem Statement 1: Integrated Insight-Driven Data-Flow Model)

---

## Table of Contents

- [Quick Start](#quick-start)
- [Installation](#installation)
- [Configuration](#configuration)
  - [Directory Structure](#directory-structure)
  - [DQI Weights](#dqi-weights)
  - [Thresholds](#thresholds)
  - [Pipeline Defaults](#pipeline-defaults)
  - [File Patterns](#file-patterns)
  - [Column Mappings](#column-mappings)
- [Pipeline Execution](#pipeline-execution)
  - [Run Full Pipeline](#run-full-pipeline)
  - [Run Individual Phases](#run-individual-phases)
  - [Pipeline Options](#pipeline-options)
- [Phase Reference](#phase-reference)
- [Validation](#validation)
- [Dashboard](#dashboard)
- [Output Structure](#output-structure)
- [Data Setup](#data-setup)
- [Documentation](#documentation)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Quick Start

```bash
# Clone repository
git clone https://github.com/vybhav72954/Javelin.ai.git
cd Javelin.AI

# Install dependencies
pip install -r requirements.txt

# Place data in data/ directory (see Data Setup)

# Run complete pipeline
python src/run_pipeline.py --all

# Launch dashboard
streamlit run src/app.py
```

---

## Installation

### Prerequisites

| Requirement | Version | Purpose |
|-------------|---------|---------|
| Python | 3.9+ | Runtime |
| Ollama | Latest | LLM inference (Phases 05, 07) |

### Step 1: Python Dependencies

```bash
pip install -r requirements.txt
```



### Step 2: Ollama Setup (Optional)

Required only for AI-powered recommendations (Phases 05 and 07).

```bash
# Install Ollama (see https://ollama.ai)
curl -fsSL https://ollama.ai/install.sh | sh

# Pull Mistral model
ollama pull mistral

# Verify installation
ollama list
```

**Supported models:** `mistral` (default), `llama3`, `llama2`, `codellama`

> **Note:** Phases 05 and 07 will run in rule-based mode if Ollama is unavailable.

---

## Configuration

All pipeline behavior is controlled through `src/config.py`. This is the single source of truth for paths, weights, thresholds, and feature definitions.

### Directory Structure

```python
from config import PROJECT_ROOT, DATA_DIR, OUTPUT_DIR, PHASE_DIRS

PROJECT_ROOT    # Root directory (auto-detected)
DATA_DIR        # Input data: PROJECT_ROOT / "data"
OUTPUT_DIR      # All outputs: PROJECT_ROOT / "outputs"
PHASE_DIRS      # Phase-specific directories: {"phase_01": OUTPUT_DIR / "phase01", ...}
```

**Phase output directories:**

| Key | Path | Content |
|-----|------|---------|
| `phase_00` | `outputs/phase00/` | Diagnostics |
| `phase_01` | `outputs/phase01/` | Data Discovery |
| `phase_02` | `outputs/phase02/` | Master Tables |
| `phase_03` | `outputs/phase03/` | DQI Scores |
| `phase_04` | `outputs/phase04/` | Knowledge Graph |
| `phase_05` | `outputs/phase05/` | Recommendations |
| `phase_06` | `outputs/phase06/` | Anomaly Detection |
| `phase_07` | `outputs/phase07/` | Multi-Agent Analysis |
| `phase_08` | `outputs/phase08/` | Site Clustering |
| `phase_09` | `outputs/phase09/` | Root Cause Analysis |
| `validation` | `outputs/validation/` | Cross-Validation |
| `logs` | `outputs/logs/` | Pipeline Logs |

---

### DQI Weights

The Data Quality Index is computed using clinically-weighted features aligned with ICH E6(R2) and FDA guidance. Weights are defined in `DQI_WEIGHTS`:

```python
from config import DQI_WEIGHTS, DQI_WEIGHT_VALUES
```

**Weight Configuration:**

| Feature | Weight | Tier | Regulatory Rationale |
|---------|--------|------|----------------------|
| `sae_pending_count` | 20% | Safety | Pending SAE reviews require immediate regulatory attention (ICH E6(R2) 4.11) |
| `uncoded_meddra_count` | 15% | Safety | Uncoded AE terms prevent safety signal detection (ICH E2A) |
| `missing_visit_count` | 12% | Completeness | Missing visits indicate protocol deviations (ICH E6(R2) 5.18.4) |
| `missing_pages_count` | 10% | Completeness | Incomplete CRFs are common FDA Form 483 findings |
| `lab_issues_count` | 10% | Completeness | Lab data critical for safety assessments (ICH E6(R2) 4.8.10) |
| `max_days_outstanding` | 8% | Timeliness | Delayed data entry reduces real-time monitoring capability |
| `max_days_page_missing` | 6% | Timeliness | Long-outstanding pages indicate systemic site issues |
| `uncoded_whodd_count` | 6% | Coding | Affects concomitant medication tracking |
| `edrr_open_issues` | 5% | Reconciliation | External data reconciliation needs resolution |
| `n_issue_types` | 5% | Composite | Multiple issue types indicate systemic problems |
| `inactivated_forms_count` | 3% | Administrative | Data corrections, lowest clinical impact |

**Total: 100%**

**Tier Summary:**

| Tier | Total Weight | Features |
|------|--------------|----------|
| Safety | 35% | SAE pending, Uncoded MedDRA |
| Completeness | 32% | Missing visits, Missing pages, Lab issues |
| Timeliness | 14% | Days outstanding, Days page missing |
| Coding | 6% | Uncoded WHODrug |
| Reconciliation | 5% | EDRR open issues |
| Composite | 5% | Number of issue types |
| Administrative | 3% | Inactivated forms |

**Customizing Weights:**

```python
# In config.py, modify DQI_WEIGHTS:
DQI_WEIGHTS = {
    'sae_pending_count': {
        'weight': 0.25,  # Increase safety weight
        'tier': 'Safety',
        'rationale': 'Your custom rationale'
    },
    # ... other features
}

# Weights must sum to 1.0 (validated at import)
```

---

### Thresholds

Risk classification and algorithm parameters are controlled via the `THRESHOLDS` class:

```python
from config import THRESHOLDS
```

**Risk Classification Thresholds:**

| Parameter | Value | Description |
|-----------|-------|-------------|
| `HIGH_RISK_PERCENTILE` | 0.90 | Subject DQI ≥ 90th percentile → High Risk |
| `MIN_HIGH_THRESHOLD` | 0.10 | Minimum DQI score for High Risk classification |
| `SITE_HIGH_PERCENTILE` | 0.85 | Site DQI ≥ 85th percentile → High Risk |
| `SITE_MEDIUM_PERCENTILE` | 0.50 | Site DQI ≥ 50th percentile → Medium Risk |
| `STUDY_HIGH_PERCENTILE` | 0.85 | Study-level High Risk threshold |
| `REGION_HIGH_PERCENTILE` | 0.85 | Region-level High Risk threshold |
| `COUNTRY_HIGH_PERCENTILE` | 0.85 | Country-level High Risk threshold |

**Outlier Handling:**

| Parameter | Value | Description |
|-----------|-------|-------------|
| `OUTLIER_IQR_MULTIPLIER` | 3.0 | IQR multiplier for outlier detection |
| `MAX_DAYS_CAP` | 1825 | Maximum days cap (5 years) |
| `MIN_SAMPLES_FOR_PERCENTILE` | 20 | Minimum samples for percentile calculation |

**Algorithm Parameters:**

| Parameter | Value | Description |
|-----------|-------|-------------|
| `VALIDATION_FOLDS` | 5 | K-fold cross-validation folds |
| `STABILITY_THRESHOLD` | 0.05 | Maximum acceptable threshold variation |
| `ANOMALY_CONTAMINATION` | 0.05 | Isolation Forest contamination rate |
| `ZSCORE_THRESHOLD` | 3.0 | Z-score threshold for anomalies |
| `MAX_CLUSTERS` | 10 | Maximum clusters for auto-detection |
| `MIN_CLUSTER_SIZE` | 5 | Minimum sites per cluster |

---

### Pipeline Defaults

Default arguments for phases with CLI options:

```python
from config import PIPELINE_DEFAULTS, get_phase_defaults

# Get defaults for Phase 05
defaults = get_phase_defaults('05')
# {'model': 'mistral', 'top_sites': 5}
```

| Phase | Parameter | Default | Description |
|-------|-----------|---------|-------------|
| **05** | `model` | `mistral` | Ollama model for recommendations |
| **05** | `top_sites` | `5` | Sites to generate recommendations for |
| **07** | `model` | `mistral` | Ollama model for multi-agent |
| **07** | `top_sites` | `3` | Sites for multi-agent analysis |
| **07** | `fast` | `False` | Skip LLM, rule-based only |
| **08** | `algorithm` | `gmm` | Clustering algorithm |
| **08** | `n_clusters` | `None` | Auto-detect if None |
| **08** | `eps` | `0.5` | DBSCAN epsilon |
| **08** | `min_samples` | `5` | DBSCAN min samples |
| **09** | `include_clusters` | `True` | Include Phase 08 clusters |
| **09** | `top_sites` | `10` | Top issues to analyze |

---

### File Patterns

The pipeline auto-discovers data files using regex patterns in `FILE_PATTERNS`:

```python
from config import FILE_PATTERNS
```

| File Type | Patterns | Example Match |
|-----------|----------|---------------|
| `edc_metrics` | `CPID.*EDC.*Metrics`, `EDC.*Metrics` | `CPID_EDC_Metrics.xlsx` |
| `visit_tracker` | `Visit.*Tracker`, `Missing.*visit` | `Visit_Projection_Tracker.xlsx` |
| `missing_lab` | `Missing.*Lab`, `Lab.*Range` | `Missing_Lab_Name_Report.xlsx` |
| `sae_dashboard` | `eSAE.*Dashboard`, `SAE.*Dashboard` | `eSAE_Dashboard.xlsx` |
| `missing_pages` | `Missing.*Pages.*Report` | `Global_Missing_Pages_Report.xlsx` |
| `meddra_coding` | `GlobalCodingReport.*MedDRA`, `MedDRA` | `GlobalCodingReport_MedDRA.xlsx` |
| `whodd_coding` | `GlobalCodingReport.*WHODD`, `WHODrug` | `GlobalCodingReport_WHODrug.xlsx` |
| `inactivated` | `Inactivated.*Forms`, `Inactivated` | `Inactivated_Forms_Report.xlsx` |
| `edrr` | `Compiled.*EDRR`, `EDRR` | `Compiled_EDRR.xlsx` |

---

### Column Mappings

Column name variations are normalized using `COLUMN_MAPPINGS`:

```python
from config import COLUMN_MAPPINGS
```

**Example — EDC Metrics:**

| Canonical Column | Accepted Variations |
|------------------|---------------------|
| `subject_id` | `Subject ID`, `Subject`, `SubjectID`, `SUBJECT ID` |
| `site_id` | `Site ID`, `Site`, `SiteID`, `SITE ID`, `Site Number` |
| `country` | `Country`, `COUNTRY` |
| `region` | `Region`, `REGION` |
| `subject_status` | `Subject Status`, `Status` |

**Example — SAE Dashboard:**

| Canonical Column | Accepted Variations |
|------------------|---------------------|
| `subject_id` | `Patient ID`, `Subject`, `Subject ID`, `PatientID` |
| `site_id` | `Site`, `Site ID` |
| `review_status` | `Review Status`, `ReviewStatus` |
| `action_status` | `Action Status`, `ActionStatus` |

---

### Feature Lists

Predefined feature lists for different analysis types:

```python
from config import (
    NUMERIC_ISSUE_COLUMNS,    # 11 features used in DQI calculation
    CLUSTERING_FEATURES,       # 9 features for site clustering
    ANOMALY_FEATURES,          # 4 features for anomaly detection
    CATEGORICAL_COLUMNS,       # country, region, subject_status
    OUTLIER_CAP_COLUMNS,       # Columns with outlier capping
)
```

**Numeric Issue Columns (DQI Input):**

```python
NUMERIC_ISSUE_COLUMNS = [
    'missing_visit_count',
    'max_days_outstanding',
    'lab_issues_count',
    'sae_total_count',
    'sae_pending_count',
    'missing_pages_count',
    'max_days_page_missing',
    'uncoded_meddra_count',
    'uncoded_whodd_count',
    'inactivated_forms_count',
    'edrr_open_issues',
]
```

**Clustering Features:**

```python
CLUSTERING_FEATURES = [
    'avg_dqi_score',
    'subject_count',
    'high_risk_rate',
    'sae_pending_count',
    'missing_visit_count',
    'lab_issues_count',
    'missing_pages_count',
    'uncoded_meddra_count',
    'uncoded_whodd_count',
]
```

---

### Helper Functions

```python
from config import (
    ensure_output_dirs,      # Create all output directories
    ensure_phase_dir,        # Create specific phase directory
    get_phase_dir,           # Get path for phase
    get_output_file,         # Get path for output file
    get_phase_script_path,   # Get path to phase script
    get_phase_defaults,      # Get default args for phase
    validate_config,         # Validate configuration consistency
)

# Examples
ensure_output_dirs()                    # Create all directories
path = get_phase_dir('phase_03')        # Path to phase03 output
script = get_phase_script_path('05')    # Path to 05_recommendations_engine.py
```

---

## Pipeline Execution

### Run Full Pipeline

```bash
# Standard execution (Phases 01-09, excluding 00 and 04)
python src/run_pipeline.py --all

# Include pre-flight diagnostics
python src/run_pipeline.py --all --diagnostics

# Include knowledge graph generation
python src/run_pipeline.py --all --include-kg

# Skip already-completed phases
python src/run_pipeline.py --all --skip-completed

# Full pipeline with all options
python src/run_pipeline.py --all --diagnostics --include-kg
```

### Run Individual Phases

```bash
# Run specific phase
python src/run_pipeline.py --phase 03

# Or run phase script directly with options
python src/phases/08_site_clustering.py --algorithm kmeans --n-clusters 5
```

### Pipeline Options

| Option | Description |
|--------|-------------|
| `--all` | Run all mandatory phases (01-03, 05-09) |
| `--phase <N>` | Run specific phase only (e.g., `--phase 03`) |
| `--diagnostics` | Include Phase 00 before pipeline |
| `--include-kg` | Include Phase 04 (knowledge graph) |
| `--skip-completed` | Skip phases with existing outputs |

### Execution Flow

```
Phase 00 (optional) → Phase 01 → Phase 02 → Phase 03 → Phase 04 (optional)
                                                              ↓
Phase 09 ← Phase 08 ← Phase 07 ← Phase 06 ← Phase 05 ←───────┘
```

---

## Phase Reference

### Phase 00: Diagnostics

Pre-pipeline validation and data quality checks.

```bash
python src/phases/00_diagnostics.py
```

**Outputs:**
- `outputs/phase00/diagnostics_report.txt`
- `outputs/phase00/diagnostics_details.json`

---

### Phase 01: Data Discovery

Scans data directory and classifies files into 9 standardized types.

```bash
python src/phases/01_data_discovery.py
```

**Outputs:**
- `outputs/phase01/file_mapping.csv`
- `outputs/phase01/column_report.csv`
- `outputs/phase01/discovery_issues.txt`

---

### Phase 02: Build Master Table

Creates unified subject-level and site-level master tables.

```bash
python src/phases/02_build_master_table.py
```

**Outputs:**
- `outputs/phase02/master_subject.csv`
- `outputs/phase02/master_site.csv`
- `outputs/phase02/master_study.csv`

---

### Phase 03: Calculate DQI

Computes Data Quality Index scores using configured weights.

```bash
python src/phases/03_calculate_dqi.py
```

**Outputs:**
- `outputs/phase03/master_subject_with_dqi.csv`
- `outputs/phase03/master_site_with_dqi.csv`
- `outputs/phase03/master_study_with_dqi.csv`
- `outputs/phase03/master_region_with_dqi.csv`
- `outputs/phase03/master_country_with_dqi.csv`
- `outputs/phase03/dqi_weights.csv`
- `outputs/phase03/dqi_model_report.txt`

---

### Phase 04: Knowledge Graph

Builds hierarchical knowledge graph.

```bash
python src/phases/04_knowledge_graph.py [OPTIONS]
```

| Option | Description |
|--------|-------------|
| `--subgraphs <list>` | Comma-separated: `highrisk`, `topstudies`, `sample`, or `all` |
| `--high-risk-only` | Create only high-risk subgraph (faster) |

**Outputs:**
- `outputs/phase04/knowledge_graph.graphml`
- `outputs/phase04/knowledge_graph_nodes.csv`
- `outputs/phase04/knowledge_graph_edges.csv`
- `outputs/phase04/knowledge_graph_summary.json`

---

### Phase 05: Recommendations Engine

Generates AI-powered recommendations.

```bash
python src/phases/05_recommendations_engine.py [OPTIONS]
```

| Option | Default | Description |
|--------|---------|-------------|
| `--model` | `mistral` | Ollama model |
| `--top-sites` | `20` | Sites to analyze |

**Outputs:**
- `outputs/phase05/recommendations_by_site.csv`
- `outputs/phase05/recommendations_by_country.csv`
- `outputs/phase05/recommendations_by_region.csv`
- `outputs/phase05/action_items.json`
- `outputs/phase05/executive_summary.txt`
- `outputs/phase05/recommendations_report.md`

---

### Phase 06: Anomaly Detection

Statistical anomaly detection.

```bash
python src/phases/06_anomaly_detection.py
```

**Outputs:**
- `outputs/phase06/anomalies_detected.csv`
- `outputs/phase06/site_anomaly_scores.csv`
- `outputs/phase06/anomaly_report.md`
- `outputs/phase06/anomaly_summary.json`

---

### Phase 07: Multi-Agent System

Specialized AI agents for multi-perspective analysis.

```bash
python src/phases/07_multi_agent_system.py [OPTIONS]
```

| Option | Default | Description |
|--------|---------|-------------|
| `--model` | `mistral` | Ollama model |
| `--top-sites` | `50` | Sites to analyze |
| `--fast` | `false` | Rule-based only (no LLM) |

**Outputs:**
- `outputs/phase07/multi_agent_recommendations.csv`
- `outputs/phase07/agent_analysis.json`
- `outputs/phase07/multi_agent_report.md`

---

### Phase 08: Site Clustering

Groups sites by performance patterns.

```bash
python src/phases/08_site_clustering.py [OPTIONS]
```

| Option | Default | Description |
|--------|---------|-------------|
| `--algorithm` | `gmm` | `gmm`, `kmeans`, or `dbscan` |
| `--n-clusters` | Auto | Number of clusters |
| `--auto` | `false` | Force auto-detection |
| `--eps` | `0.5` | DBSCAN epsilon |
| `--min-samples` | `5` | DBSCAN min samples |

**Outputs:**
- `outputs/phase08/site_clusters.csv`
- `outputs/phase08/cluster_profiles.csv`
- `outputs/phase08/cluster_report.md`
- `outputs/phase08/cluster_summary.json`
- `outputs/phase08/cluster_distribution.png`
- `outputs/phase08/cluster_heatmap.png`
- `outputs/phase08/cluster_pca.png`

---

### Phase 09: Root Cause Analysis

Identifies root causes using co-occurrence analysis.

```bash
python src/phases/09_root_cause_analysis.py [OPTIONS]
```

| Option | Default | Description |
|--------|---------|-------------|
| `--include-clusters` | `true` | Include Phase 08 clusters |
| `--no-clusters` | `false` | Skip cluster integration |
| `--top-sites` | `10` | Top issues to analyze |

**Outputs:**
- `outputs/phase09/root_cause_analysis.csv`
- `outputs/phase09/issue_cooccurrence.csv`
- `outputs/phase09/geographic_patterns.csv`
- `outputs/phase09/contributing_factors.csv`
- `outputs/phase09/root_cause_report.md`
- `outputs/phase09/root_cause_summary.json`

---

## Validation

### K-Fold Cross-Validation

Validates DQI methodology robustness.

```bash
python src/validation.py [OPTIONS]
```

| Option | Default | Description |
|--------|---------|-------------|
| `--folds` | `5` | Cross-validation folds |
| `--include-sensitivity` | `false` | Run weight sensitivity analysis |
| `--seed` | `42` | Random seed |

**Validation Metrics:**

| Metric | Target | Description |
|--------|--------|-------------|
| Threshold Stability | CV < 5% | 90th percentile consistency |
| Category Agreement | > 95% | Risk category consistency |
| Ranking Correlation | > 0.8 | Site ranking consistency |
| SAE Capture Rate | 100% | All SAE subjects → High Risk |

**Outputs:**
- `outputs/validation/kfold_validation_results.csv`
- `outputs/validation/kfold_validation_report.md`
- `outputs/validation/kfold_validation_details.json`
- `outputs/validation/test_predictions.csv` — **Validation file**
- `outputs/validation/VALIDATION_METHODOLOGY.md`

---

## Dashboard

```bash
streamlit run src/app.py
```

**URL:** http://localhost:8501

---

## Output Structure

```
outputs/
├── logs/
│   └── pipeline_run_YYYYMMDD_HHMMSS.log
├── phase00/                    # Diagnostics
├── phase01/                    # Data Discovery
├── phase02/                    # Master Tables
├── phase03/                    # DQI Scores
├── phase04/                    # Knowledge Graph
├── phase05/                    # Recommendations
├── phase06/                    # Anomaly Detection
├── phase07/                    # Multi-Agent Analysis
├── phase08/                    # Site Clustering
├── phase09/                    # Root Cause Analysis
└── validation/
    ├── test_predictions.csv    # Competition submission
    └── ...
```

---

## Data Setup

### Directory Structure

```
Javelin.AI/
├── data/
│   ├── Study_1_CPID_Input Files - Anonymization/
│   │   ├── EDC Metrics/
│   │   ├── Lab Reconciliation Report/
│   │   ├── Coding Status - MedDRA/
│   │   ├── Coding Status - WHODrug/
│   │   ├── Data Issues Visit Tracker/
│   │   ├── Data Issues Query Aging/
│   │   ├── Data Issues Page Tracker/
│   │   ├── Site CRA Metrics/
│   │   └── Safety Review Status/
│   ├── Study_2_CPID_Input Files - Anonymization/
│   └── ...
├── src/
├── outputs/
└── docs/
```

### Expected File Types

| Data Source | Key Columns | Purpose |
|-------------|-------------|---------|
| EDC Metrics | Subject ID, Site ID, Country | Subject enrollment |
| Visit Tracker | Subject ID, Missing Visit Count | Protocol compliance |
| Query Aging | Subject ID, Max Days Outstanding | Data timeliness |
| Lab Reconciliation | Subject ID, Lab Issues Count | Lab data quality |
| MedDRA Coding | Subject ID, Uncoded Count | AE coding status |
| WHODrug Coding | Subject ID, Uncoded Count | Medication coding |
| Page Tracker | Subject ID, Missing Pages Count | CRF completeness |
| Site CRA Metrics | Site ID, EDRR Open Issues | Site performance |
| Safety Review | Subject ID, SAE Pending Count | Safety oversight |

---

## Documentation

| Document | Location | Description |
|----------|----------|-------------|
| Methodology & Regulatory Alignment | `docs/METHODOLOGY_REGULATORY_ALIGNMENT.md` | ICH E6(R2), FDA alignment |
| DQI Validation & Sensitivity | `docs/DQI_VALIDATION_SENSITIVITY_ANALYSIS.md` | Weight validation |
| Validation Methodology | `outputs/validation/VALIDATION_METHODOLOGY.md` | Cross-validation approach |

---

## Troubleshooting

### Common Issues

**Pipeline fails at Phase 01:**
```
ERROR: Data directory not found
```
→ Ensure `data/` directory exists with study folders.

**Ollama connection refused:**
```
ERROR: Could not connect to Ollama
```
→ Start Ollama: `ollama serve` or use `--fast` flag.

**Memory error:**
```
MemoryError: Unable to allocate array
```
→ Use `--high-risk-only` or increase system memory.

### Logs

```bash
# View latest log
cat outputs/logs/pipeline_run_*.log | tail -100

# Find errors
grep "ERROR" outputs/logs/pipeline_run_*.log
```

### Resume After Failure

```bash
# Resume from failed phase
python src/run_pipeline.py --phase <N>

# Skip completed phases
python src/run_pipeline.py --all --skip-completed
```

---

## License

Developed for **NEST 2.0 Innovation Challenge** — Novartis

---

## Team

**Team CWTY**
- Vybhav Chaturvedi
- Pranav Taneja
- Sneha Yadav

---

*For detailed methodology, see `docs/METHODOLOGY_REGULATORY_ALIGNMENT.md`*
