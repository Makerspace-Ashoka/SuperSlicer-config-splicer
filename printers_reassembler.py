import re


def split_ini_files(input_filenames):
    # Define the keywords to search for
    keywords = ["Augustus", "Augustine", "May"]

    # Process each input file for each keyword
    for keyword in keywords:
        sections = []

        for input_filename in input_filenames:
            section_checker = False
            with open(input_filename, "r") as input_file:
                lines = input_file.readlines()
            for line in lines:
                section_validator(line, keyword, sections, section_checker)

        # Write sections containing the keyword to an output file
        if sections:
            write_sections(sections, keyword)


def write_sections(keys, file_title):
    output_filename = f"{file_title}.ini"
    with open(output_filename, "w") as output_file:
        output_file.writelines(keys)


def section_validator(input_line, keyphrase, repo, header_check):
    stripped_line = input_line.strip()
    if stripped_line.startswith("[") and stripped_line.endswith("]"):
        match = re.search(keyphrase, input_line)
        print(match)

        if match:
            header_check = True
            print("its a match")
            repo.append(input_line)
            return repo
        else:
            header_check = False
            print("unmatched")
            return
    elif header_check == True:
        repo.append(input_line)
    elif header_check == False:
        return
    # elif header_check == True:
    #     repo.append(input_line)

    # return repo


if __name__ == "__main__":
    input_filenames = ["print.ini", "printer.ini", "filament.ini"]
    split_ini_files(input_filenames)
