"""
Javelin.AI - Setup Verification
================================
Run this to verify your environment is set up correctly.

Usage:
    python src/00_verify_setup.py
"""

import sys
from pathlib import Path

def check_python_version():
    """Check Python version."""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 9:
        print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"❌ Python version: {version.major}.{version.minor}.{version.micro} (need 3.9+)")
        return False

def check_directories():
    """Check required directories exist."""
    required = ['data', 'src', 'outputs', 'models', 'config']
    all_exist = True
    
    for dir_name in required:
        path = Path(dir_name)
        if path.exists():
            print(f"✅ Directory exists: {dir_name}/")
        else:
            print(f"❌ Directory missing: {dir_name}/")
            all_exist = False
    
    return all_exist

def check_data_folder():
    """Check if data folder has study folders."""
    data_path = Path('data')
    
    if not data_path.exists():
        print("❌ Data folder not found")
        return False
    
    study_folders = [f for f in data_path.iterdir() if f.is_dir()]
    
    if study_folders:
        print(f"✅ Found {len(study_folders)} study folders in data/")
        for folder in study_folders[:3]:
            excel_count = len(list(folder.glob("*.xlsx"))) + len(list(folder.glob("*.xls")))
            print(f"   └── {folder.name} ({excel_count} Excel files)")
        if len(study_folders) > 3:
            print(f"   └── ... and {len(study_folders) - 3} more")
        return True
    else:
        print("⚠️  No study folders found in data/")
        print("   Add your study folders to the data/ directory")
        return False

def check_packages():
    """Check required packages are installed."""
    packages = {
        'pandas': 'pandas',
        'openpyxl': 'openpyxl',
        'numpy': 'numpy',
    }
    
    optional_packages = {
        'tabpfn': 'tabpfn',
        'shap': 'shap',
        'networkx': 'networkx',
        'streamlit': 'streamlit',
        'chromadb': 'chromadb',
    }
    
    all_installed = True
    
    print("\nRequired packages:")
    for name, module in packages.items():
        try:
            __import__(module)
            print(f"  ✅ {name}")
        except ImportError:
            print(f"  ❌ {name} (pip install {name})")
            all_installed = False
    
    print("\nOptional packages (install when needed):")
    for name, module in optional_packages.items():
        try:
            __import__(module)
            print(f"  ✅ {name}")
        except ImportError:
            print(f"  ⬚ {name} (not installed yet)")
    
    return all_installed

def main():
    print("=" * 60)
    print("JAVELIN.AI - SETUP VERIFICATION")
    print("=" * 60)
    print()
    
    results = []
    
    print("1. Python Version")
    print("-" * 40)
    results.append(check_python_version())
    print()
    
    print("2. Directory Structure")
    print("-" * 40)
    results.append(check_directories())
    print()
    
    print("3. Data Folder")
    print("-" * 40)
    results.append(check_data_folder())
    print()
    
    print("4. Python Packages")
    print("-" * 40)
    results.append(check_packages())
    print()
    
    print("=" * 60)
    if all(results):
        print("✅ ALL CHECKS PASSED - Ready to run!")
        print("\nNext step: python src/01_data_discovery.py")
    else:
        print("⚠️  SOME CHECKS FAILED - See above for details")
    print("=" * 60)

if __name__ == "__main__":
    main()
