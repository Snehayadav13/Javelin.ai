# Javelin.AI
## AI-Powered Clinical Trial Intelligence Platform

---

## 🚀 Quick Start

### 1. Setup Environment

```bash
# Create project directory
mkdir Javelin.AI
cd Javelin.AI

# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Add Your Data

```
Javelin.AI/
├── data/                          ← Put your study folders here
│   ├── Study 1_CPID_Input Files/
│   │   ├── Study_1_EDC_Metrics.xlsx
│   │   ├── Study_1_Visit_Tracker.xlsx
│   │   └── ... (9 files)
│   ├── Study 2_CPID_Input Files/
│   └── ... (22 study folders)
├── src/
├── outputs/
└── ...
```

### 3. Run Data Discovery

```bash
python src/01_data_discovery.py
```

This will:
- Scan all your study folders
- Classify files into 9 types
- Check column mappings
- Report any issues

### 4. Review & Fix Issues

Check `outputs/discovery_issues.txt` for any problems.

### 5. Build Master Table

```bash
python src/02_build_master_table.py
```

---

## 📁 Project Structure

```
Javelin.AI/
├── data/                    # Your raw data (22 study folders)
├── src/
│   ├── 01_data_discovery.py    # Step 1: Scan & classify files
│   ├── 02_build_master_table.py # Step 2: Create unified table
│   ├── 03_dqi_scoring.py       # Step 3: Calculate DQI with SHAP
│   ├── 04_knowledge_graph.py   # Step 4: Build graph
│   ├── 05_rag_pipeline.py      # Step 5: RAG + CoV
│   └── app.py                  # Streamlit dashboard
├── outputs/
│   ├── file_mapping.csv        # File classifications
│   ├── column_report.csv       # Column mappings
│   ├── master_subject.csv      # Unified subject table
│   └── master_site.csv         # Aggregated site table
├── models/
│   └── tabpfn_model.pkl        # Trained model
├── config/
│   └── column_mappings.yaml    # Manual overrides
├── requirements.txt
└── README.md
```

---

## 🔧 Configuration

If automatic column detection fails, you can add manual overrides in `config/column_mappings.yaml`:

```yaml
# Example override
Study_5:
  edc_metrics:
    subject_id: "Patient Number"  # Non-standard column name
    site_id: "Center ID"
```

---

## 📊 Pipeline Steps

| Step | Script | Output |
|------|--------|--------|
| 1 | `01_data_discovery.py` | file_mapping.csv, column_report.csv |
| 2 | `02_build_master_table.py` | master_subject.csv, master_site.csv |
| 3 | `03_dqi_scoring.py` | DQI scores, SHAP weights |
| 4 | `04_knowledge_graph.py` | graph.html (interactive) |
| 5 | `05_rag_pipeline.py` | RAG system ready |
| 6 | `app.py` | Streamlit dashboard |

---

## 🎯 Innovations

1. **Data-Driven DQI** - Weights from SHAP, not arbitrary
2. **Graph-Based Discovery** - Find site clusters & patterns  
3. **CoV-RAG** - Self-verifying AI responses

---

## 📝 Notes

- Requires Python 3.9+
- For LLM: Install Ollama and run `ollama pull llama3.1:8b`
- Dashboard: `streamlit run src/app.py`
