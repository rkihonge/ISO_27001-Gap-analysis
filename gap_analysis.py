import json

def load_controls(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def compare_controls(iso_controls, current_state):
    implemented = []
    missing = []
    partial = []

    for control, description in iso_controls.items():
        if control in current_state:
            if current_state[control] == "implemented":
                implemented.append(f"{control}: {description}")
            elif current_state[control] == "partial":
                partial.append(f"{control}: {description}")
            else:
                missing.append(f"{control}: {description}")
        else:
            missing.append(f"{control}: {description}")

    return implemented, partial, missing

def save_report(implemented, partial, missing, output_file="output/report.txt"):
    with open(output_file, "w") as f:
        f.write("ISO/IEC 27001:2022 Gap Analysis Report\n")
        f.write("="*50 + "\n\n")
        f.write("✅ Implemented Controls:\n")
        for c in implemented:
            f.write(f" - {c}\n")
        f.write("\n🟡 Partially Implemented Controls:\n")
        for c in partial:
            f.write(f" - {c}\n")
        f.write("\n❌ Missing Controls:\n")
        for c in missing:
            f.write(f" - {c}\n")

if __name__ == "__main__":
    iso_controls = load_controls("controls/iso27001_controls.json")
    current_state = load_controls("controls/sample_current_state.json")

    implemented, partial, missing = compare_controls(iso_controls, current_state)
    save_report(implemented, partial, missing)

    print("Gap analysis complete! See output/report.txt")
