import os
from datetime import datetime

import pymupdf


for dir in os.walk("."):

    if not dir[1]:
        for file in dir[2]:


            doc = pymupdf.open(f"{dir[0]}/{file}")


            year = dir[0].replace("./", "")  # 2025
            level = file.replace(".pdf", "")  # level-1
            timestamp = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")

            data_folder = f"../data/topic-outlines/{year}/{level}/"
            out_path = f"../data/topic-outlines/{year}/{level}/{timestamp}.txt"


            if not os.path.exists(data_folder):
                os.makedirs(data_folder)

            out = open(out_path, "wb")

            for page in doc: # iterate the document pages
                text = page.get_text().encode("utf8") # get plain text (is in UTF-8)
                out.write(text) # write text of page
                out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
            out.close()
