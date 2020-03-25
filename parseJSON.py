import sys
import json
import os
import re

from collections import OrderedDict

"""
(?<!\\)[\[\{\]\}]|\\(?={|\]|}|\[)

match [ or { or ] or } if not preceded by /
or
match \ if not followed by [ or { or } or ]

for more examples: https://regex101.com/r/G9hbnZ/17

"""
# regexp to parse json file
REGEX = r'(?<!\\)[\[\{\]\}]|\\(?={|\]|}|\[)'


# regexp for special characters in aliases
aliasREGEX = r"[+<>\\/:*#$%&{}!'`\"@=|]"

# used by the client for ANSI escape code colors
TITLE_TAG = "# "
CATEGORY_TAG = "$ "
SHORTCUT_TAG = "`"
DESCRIPTION_START_TAG = "{{"
DESCRIPTION_END_TAG = "}}"
NORMAL_TEXT_TAG = "> "


def parse(args):
    """parses json into appropriate md pretty format
    assumes JSON file is located under json/ folder

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

                # with open("programs.md", "a") as prgs:
                #     prgs.write(program_name + ", ")

                try:
                    outfile.write(
                        NORMAL_TEXT_TAG + "Source: " + data["metadata"]["sourceUrl"] + "\n\n")
                except:
                    with open("parseLog.md", "a") as log:
                        log.write("Source error: " + json_path + "\n")
                        # log.write(json_path + "\n")

                try:
                    # remove duplicates
                    temp = list(dict.fromkeys(
                        [a.replace(" ", "-") for a in data["aliases"]]))

                    for alias in temp:
                        # ignore aliases that already exist for the same program
                        if alias == program_name:
                            continue
                        elif re.search(aliasREGEX, alias):
                            continue
                        else:
                            aliases.append(alias)

                    if aliases:
                        outfile.write(NORMAL_TEXT_TAG +
                                      "Aliases: " + ", ".join(aliases) + "\n\n")

                except KeyError:
                    # aliases are optional
                    pass
                except Exception as e:
                    with open("aliasError.md", "a") as log:
                        log.write(str(e) + " for program: " + program_name +
                                  ",with aliases: " + str(data["aliases"]) + "\n")

            def middleSection():
                for key, value in data["sections"].items():
                    outfile.write(CATEGORY_TAG + key + "\n")

                    for item in value:
                        try:
                            shortcut = re.sub(REGEX, "", item['key'])
                            shortcut = SHORTCUT_TAG + shortcut
                            description = DESCRIPTION_START_TAG + \
                                item['val'] + DESCRIPTION_END_TAG

                            if len(shortcut) > 30:
                                outfile.write("{:4}{}\n{:2}{:32} {} \n".format(
                                    "", shortcut, NORMAL_TEXT_TAG, "", description))
                            else:
                                outfile.write("{:4}{:30} {} \n".format(
                                    "", shortcut, description))
                        except:
                            with open("parseLog.md", "a") as log:
                                log.write("Description error: " +
                                          json_path+"\n")
                                # log.write(json_path+"\n")
                                quit(1)
                    outfile.write("\n")

            # creating symlinks named after aliases of the original file
            def createAliases(aliases):
                try:

                    for alias in aliases:

                        alias_path = destination + alias + ".md"
                        os.symlink(program_name + ".md", alias_path)

                except Exception as e:
                    if e.errno == 17:  # file exists
                        pass
                    else:
                        with open("createAliasError.md", "a") as log:
                            log.write(str(e) + " when creating aliases for program: " + program_name +
                                      ", with aliases: " + str(aliases) + "\n")

            upperSection()
            middleSection()
            createAliases(aliases)


if __name__ == "__main__":
    parse(sys.argv)
