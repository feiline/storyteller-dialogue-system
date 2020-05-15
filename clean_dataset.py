import re


def clean_dataset(path_file, new_path):
    """ method to clean a txt file
    :return txt file cleaned """
    file = open(path_file)
    lines = file.readlines()
    new_file = []
    with open(path_file, 'r') as file:
        old_line_1 = ''
        old_line_2 = ''
        chat = 1

        # print(data)

        for line in lines:
            # print("Line before: " + line)
            # replace the "Chat: Chat_***" with "Chat: n" with "n" == int
            if "Chat_" in line:
                line = re.sub(r'Chat_\w*', str(chat), line)
                chat += 1

            # replace the "U_**" with "User 1" or "User 2"
            if "U_" in line:
                if old_line_1 == '':
                    old_line_1 = line
                    line = re.sub(r'U_\w*', "User", line)
                elif old_line_1 != line and old_line_2 == '':
                    old_line_2 = line
                    line = re.sub(r'U_\w*', "Storyteller", line)
                elif line == old_line_1:
                    line = re.sub(r'U_\w*', "User", line)
                elif line == old_line_2:
                    line = re.sub(r'U_\w*', "Storyteller", line)
                elif line != old_line_1 and line != old_line_2:
                    old_line_1 = line
                    line = re.sub(r'U_\w*', "User", line)
                    old_line_2 = ''

            new_file.append(line)
            # print("Line after: " + line)

    file.close()

    with open(new_path, "w") as f:
        for line in new_file:
            f.write(line)

            # print(words)
            # print("Line after:" + line)
    file.close()



def main():
    path_file = "./Storytelling_Data/chats_23-11-18.txt"
    new_path_file ="./Cleaned_Data/chats_23-11-18.txt"
    clean_dataset(path_file, new_path_file)


if __name__ == '__main__':
    main()