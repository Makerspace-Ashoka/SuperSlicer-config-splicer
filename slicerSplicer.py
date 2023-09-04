import re

# Constants for section names and filenames

SECTIONS = ["print", "printer", "filament", "physical_printer"]
OUTPUT_FILENAMES = ["print.ini", "printer.ini", "filament.ini", "physical_printer"]
privacy_section = ["print_host"]


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
            if current_section in SECTIONS:
                sections[current_section].append(line)
            else:
                break
        elif current_section in SECTIONS:
            added_line = internal_privacy(line)
            if added_line:
                sections[current_section].append(added_line)

    return sections


def write_sections(sections):
    for section, lines in sections.items():
        filename = f"{section}.ini"
        with open(filename, "w") as output_file:
            output_file.writelines(lines)


def internal_privacy(input_string):
    output_line = input_string
    for privacy_field in privacy_section:
        hostname_checker = re.match(privacy_field, input_string)
        equal_position = 0
        if hostname_checker:
            for i in range(len(input_string)):
                if input_string[i] == "e":
                    equal_position = i
                    output_line = privacy_field + " =\n"
                    return output_line
                else:
                    continue
        else:
            return output_line


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
