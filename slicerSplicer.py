# Constants for section names and filenames
SECTIONS = ["print", "printer", "filament", "physical_printer"]
OUTPUT_FILENAMES = ["print.ini", "printer.ini", "filament.ini", "physical_printer"]


def extract_sections(input_lines):
    sections = {section: [] for section in SECTIONS}
    current_section = None

    for line in input_lines:
        stripped_line = line.strip()
        # TODO: make current_section read only up till first colon.
        if stripped_line.startswith("[") and stripped_line.endswith("]"):
            colon_position = 0
            for i in range(len(stripped_line)):
                if stripped_line[i] != ":":
                    continue
                else:
                    colon_position = i
                    break

            current_section = stripped_line[1:colon_position].lower()
            sections[current_section].append(line)
        elif current_section in SECTIONS:
            sections[current_section].append(line)

    return sections


def write_sections(sections):
    for section, lines in sections.items():
        filename = f"{section}.ini"
        with open(filename, "w") as output_file:
            output_file.writelines(lines)


def split_ini_file(filename):
    with open(filename, "r") as input_file:
        input_lines = input_file.readlines()

    sections = extract_sections(input_lines)
    write_sections(sections)


if __name__ == "__main__":
    input_filename = (
        "SuperSlicer_config_bundle.ini"  # Replace with your actual input .ini filename
    )
    split_ini_file(input_filename)
