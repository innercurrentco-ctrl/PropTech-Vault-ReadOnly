import os

VAULT_ROOT = "."
OUTPUT_FILE = "vault_index.md"

def list_notes(start_path):
    notes = []
    for root, dirs, files in os.walk(start_path):
        for file in files:
            if file.endswith(".md") and file != OUTPUT_FILE:
                rel_path = os.path.relpath(os.path.join(root, file), start=VAULT_ROOT)
                notes.append(rel_path.replace("\\", "/"))
    return notes

def generate_index():
    notes = list_notes(VAULT_ROOT)
    notes.sort()
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# Vault Index\n\n")
        for note in notes:
            f.write(f"- [{note}]({note})\n")

if __name__ == "__main__":
    generate_index()
