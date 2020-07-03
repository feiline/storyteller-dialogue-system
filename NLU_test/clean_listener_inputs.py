import re

def create_document_affirm(path_file, new_path):
    file = open(path_file)
    lines = file.readlines()
    new_file = []
    with open(path_file, 'r') as file:
        for line in lines:
            if "(affirm)" in line:
                new_file.append(line)

    file.close()

    with open(new_path, "w") as f:
        for line in new_file:
            f.write(line)

    file.close()


def create_document_request_increment(path_file, new_path):
    file = open(path_file)
    lines = file.readlines()
    new_file = []
    with open(path_file, 'r') as file:
        for line in lines:
            if "(request_increment)" in line:
                new_file.append(line)

    file.close()

    with open(new_path, "w") as f:
        for line in new_file:
            f.write(line)

    file.close()


def create_document_thanks(path_file, new_path):
    file = open(path_file)
    lines = file.readlines()
    new_file = []
    with open(path_file, 'r') as file:
        for line in lines:
            if "(thanks)" in line:
                new_file.append(line)

    file.close()

    with open(new_path, "w") as f:
        for line in new_file:
            f.write(line)

    file.close()


def clean_dataset(path_file, new_path):
    """ method to clean a txt file
    :return txt file cleaned """
    file = open(path_file)
    lines = file.readlines()
    new_file = []
    with open(path_file, 'r') as file:
        for line in lines:
            if "User:" in line:
                new_file.append(line)

    file.close()

    with open(new_path, "w") as f:
        for line in new_file:
            f.write(line)

    file.close()


def main():
    path_file = "cleaned_listener_input.txt"
    new_path_file = "listener_request_increment.txt"
    # clean_dataset(path_file, new_path_file)
    create_document_request_increment(path_file, new_path_file)



if __name__ == '__main__':
    main()