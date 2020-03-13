import sys
import json
import os
import re

"""
(?<!\\)[\[\{\]\}]|\\(?={|\]|}|\[)

match [ or { or ] or } if not preceeded by /
or
match \ if not followed by [ or { or } or ]

for more examples: https://regex101.com/r/G9hbnZ/17

"""
# regexp to parse json file
REGEX = r'(?<!\\)[\[\{\]\}]|\\(?={|\]|}|\[)'


# regexp for special charachters in aliases 
aliasREGEX = r"[+<>\\/:*#$%&{}!'`\"@=|]"

TITLE_TAG = "# "
CATEGORY_TAG = "$ "
SHORTCUT_TAG = "`"
DESCRIPTION_START_TAG = "{{"
DESCRIPTION_END_TAG = "}}"
NORMAL_TEXT_TAG = "> "



def parse(args):
    """parses json into approperiate md pretty format

    Arguments:
        args {array} -- 
    """
    # destination = "programs/"
    scriptPath, destination, json_file = args
    program_name = json_file[:-5]
    markdown_path = destination + program_name + ".md"
    json_path = "json/" + json_file

    with open(json_path, "r") as infile:
        with open(markdown_path, "w+") as outfile:

            data = json.load(infile)
            aliases = []
            
            def upperSection():
                outfile.write(TITLE_TAG + data["name"] + "\n\n")

                with open("programs.md", "a") as prgs:
                    prgs.write(program_name + ", ")

                try:
                    outfile.write(
                        NORMAL_TEXT_TAG + "Source: " + data["metadata"]["sourceUrl"] + "\n\n")
                except:
                    with open("parseLog.md", "a") as log:
                        # log.write("Source error " + json_path + "\n")
                        log.write(json_path + "\n")
                        # quit()

                try:
                    aliases.extend(set([a.replace(" ", "-") for a in data["aliases"]]))
                    outfile.write(NORMAL_TEXT_TAG + "Aliases: " + ", ".join(aliases) + "\n\n")
                except:
                    pass
                    # with open("parseLog.md", "a") as log:
                    #     # log.write("Aliases error " + json_path + "\n")
                    #     log.write(json_path + "\n")
                    #     # quit()

                
            def middleSection():
                for key, value in data["sections"].items():
                    outfile.write(CATEGORY_TAG + key + "\n")
                    
                    for item in value:
                        try:
                            shortcut = re.sub(REGEX,"", item['key'])
                            shortcut = SHORTCUT_TAG + shortcut
                            description = DESCRIPTION_START_TAG + item['val'] + DESCRIPTION_END_TAG

                            if len(shortcut) > 30:
                                outfile.write("{:4}{}\n{:2}{:32} {} \n".format(
                                    "", shortcut,NORMAL_TEXT_TAG, "", description))
                            else:
                                outfile.write("{:4}{:30} {} \n".format(
                                    "", shortcut, description))
                        except:
                            with open("parseLog.md", "a") as log:
                                # log.write("Discription error " + json_path+"\n")
                                log.write(json_path+"\n")
                                quit()
                    outfile.write("\n")

            # creating symlinks named after aliases of the original file
            def createAliases(aliases):
                try:

                    for alias in aliases:
                        alias = alias.replace(" ", "-")

                        # ignore aliases that already exist for the same program
                        if alias == program_name:
                            continue
                        elif re.search(aliasREGEX, alias):
                            continue 
                        else:
                            alias_path = destination + \
                                alias + ".md"
                            os.symlink(program_name + ".md", alias_path)

                except KeyError:
                    pass
                except Exception as e:
                    with open("aliasError.md", "a") as log:
                        log.write(str(e) + " for program: " + program_name +
                                    ",with aliases: " + str(data["aliases"]) + "\n")

            upperSection()
            middleSection()
            createAliases(aliases)


if __name__ == "__main__":
    parse(sys.argv)
