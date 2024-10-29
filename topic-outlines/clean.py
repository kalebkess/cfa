import os

filepath = "../data/topic-outlines/2024/level-3/2024-10-28-21:51:32.txt"


def filter_lines(filepath):

    with open(filepath, "r") as f:
        
        doc = f.readlines()

        substrings = [
            "For candidate use only",
            "The candidate should be able to",
            "Topic Outlines"
        ]

        filtered_list = [item for item in doc if not any(sub in item for sub in substrings)]  # remove lines that contain substrings
        filtered_list = [item for item in filtered_list if len(item) > 2]  # remove empty lines
        # filtered_list = [item.strip() for item in filtered_list]  # remove empty lines

        return filtered_list




def process_strings(string_list):
    if not string_list:
        return []

    result = []
    for i in range(len(string_list)):
        current_string = string_list[i]
        
        # Check if this is not the last string and the next string starts with lowercase or space
        if i < len(string_list) - 1 and (string_list[i+1].startswith(' ') or string_list[i+1][0].islower()):
            # Remove the newline character if it exists at the end
            current_string = current_string.rstrip('\n')
        
        result.append(current_string)

    return result




def main():
        #

        filtered_list = filter_lines(filepath)
        lines = process_strings(filtered_list)

        with open("tmp.txt", "w") as f:
             f.writelines(lines)

        with open("tmp.txt", "r") as f:
             lines = f.readlines()


        result = []

        for i, current_line in enumerate(lines):
            # print(current_line)
            previous_line = lines[i-1] if i > 0 else None
            next_line = lines[i+1] if i < len(lines) - 1 else None

            # Topic
            if next_line == "LEARNING OUTCOMES\n":
                 result.append(
                      {
                           "line": current_line,
                           "type": "Topic"
                      }
                 )


            # Module
            elif ( next_line != None ) and ( next_line.startswith("□") and not current_line.startswith("□") ):
                 result.append(
                      {
                           "line": current_line,
                           "type": "Module"
                      }
                 )



            # LOS
            elif current_line.startswith("□"):
                 result.append(
                      {
                           "line": current_line,
                           "type": "LOS"
                      }
                 )




            else:
                 result.append(
                      {
                           "line": current_line,
                           "type": "N/A"
                      }
                 )

        

        for r in result:
            #  if r['type'] == "Topic":
            print(f"{r["type"]}: {r["line"]}")



        with open("tmp.txt", "w") as f:
             f.writelines(lines)



if __name__ == "__main__":
     main()