# ISO/IEC 27001:2022 Gap Analysis Tool

This project provides a simple **Gap Analysis Tool** to help organizations evaluate their compliance with **ISO/IEC 27001:2022** information security controls.  

The script compares a baseline list of ISO controls with the organization's current implementation status (implemented, partial, or missing) and generates a **compliance gap report**.

---

## Features
- Loads ISO/IEC 27001:2022 Annex A control set.
- Compares against the organization's current state.
- Identifies implemented, partially implemented, and missing controls.
- Generates a compliance report (`output/report.txt`).
- Easy to extend with additional controls or formats.

---

## How It Works
1. `iso27001_controls.json` contains the baseline ISO controls.  
2. `sample_current_state.json` represents the organization's security posture.  
3. Run the script to generate `report.txt` in the `output` folder.  

---

# Run the script
python gap_analysis.py
