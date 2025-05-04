import sys

def renumber_from_line(file_path, start_line_content, start_number):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    found_index = None
    for idx, line in enumerate(lines):
        if start_line_content.strip() in line.strip():
            found_index = idx
            break

    if found_index is None:
        print(f"❌ Line with content '{start_line_content}' not found.")
        return

    new_lines = []
    current_number = start_number

    for idx, line in enumerate(lines):
        if idx < found_index:
            new_lines.append(line)
        else:
            content = line.strip()
            if content:
                # Remove old numbering if exists (optional)
                if '.' in content:
                    parts = content.split('.', 1)
                    if parts[0].isdigit():
                        content = parts[1].strip()
                new_line = f"{current_number}. {content}\n"
                new_lines.append(new_line)
                current_number += 1
            else:
                new_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print(f"✅ Successfully renumbered starting from '{start_line_content}' with number {start_number}.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python renumber_lines.py <file_path> <start_line_content> <start_number>")
        sys.exit(1)

    file_path = sys.argv[1]
    start_line_content = sys.argv[2]
    try:
        start_number = int(sys.argv[3])
    except ValueError:
        print("Start number must be an integer.")
        sys.exit(1)

    renumber_from_line(file_path, start_line_content, start_number)
