import re


def split_ini_files(input_filenames):
    # Define the keywords to search for
    keywords = ["Augustus", "Augustine", "May"]

    # Process each input file for each keyword
    for keyword in keywords:
        sections = []

        for input_filename in input_filenames:
            with open(input_filename, "r") as input_file:
                lines = input_file.readlines()
            section_checker = False
            for line in lines:
                stripped_line = line.strip()
                if stripped_line.startswith("[") and stripped_line.endswith("]"):
                    match = re.search(keyword, stripped_line)
                    print(match)

                    if match:
                        section_checker = True
                        print("its a match")
                        sections.append(line)

                    else:
                        section_checker = False
                        print("unmatched")

                elif section_checker == True:
                    sections.append(line)

                elif section_checker == False:
                    continue

        # Write sections containing the keyword to an output file
        if sections:
            write_sections(sections, keyword)


def write_sections(keys, file_title):
    output_filename = f"{file_title}.ini"
    with open(output_filename, "w") as output_file:
        output_file.writelines(keys)


if __name__ == "__main__":
    input_filenames = [
        "print.ini",
        "printer.ini",
        "filament.ini",
        "physical_printer.ini",
    ]
    split_ini_files(input_filenames)
