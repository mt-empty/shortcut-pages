import sys
import json
import re


def test(args):
   
    # regexp for special characters in aliases 
    aliasREGEX = r"[+<>\\/:*#$%&{}!'`\"@=|]"

    error_flag = False

    try:
        scriptPath, json_path = args
        page_name = json_path[:-5]
    except:
        print(scriptPath, "Requires a single JSON file only, quitting")
        quit()

    with open(json_path, "r") as infile:
        
        try:
            data = json.load(infile)
        except:
            print("Invalid JSON file, quitting\n")
            quit()

        try: 
            data["isGUI"]
        except:
            print("Error: [isGUI] value is required\n")
            error_flag = True
            
      
        def validate_upper_section():
            try:
                data["name"]
            except:
                print("Error: [name] value is required\n")
                error_flag = True
                
            try:
                data["metadata"]["sourceUrl"]
            except:
                print("Error: [sourceUrl] value is required\n")
                error_flag = True
                
            try:
                for alias in data["aliases"]:
                    if " " in alias:
                        print("Spaces are not allowed in aliases")
                        raise Exception
                    if alias == page_name:
                        print("Aliases same as page name are not allowed in aliases")
                        raise Exception
                    elif re.search(aliasREGEX, alias):
                        print("Invalid character used in", alias)
                        raise Exception 
                        
            except KeyError:
                # aliases are optional
                pass
            except Exception:
                print("Error: Invalid alias '{}' for {}\n".format(alias, page_name))
                error_flag = True
            
        def validate_middle_sections():
            try:
                data["sections"].items()
            except:
                error_flag = True
                print("Error: sections value is required\n")
            
            for key, value in data["sections"].items():                  
                for item in value:
                    try:
                        item['key']
                        item['val']

                    except:
                        print("invalid item " + value + "\n")
                        error_flag = True
        validate_upper_section()
        validate_middle_sections()

        if error_flag:
            print("Please correct the above errors")
        else:
            print("No errors found")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error, not enough arguments,\nUsage: validate_page.py path_to_page.json")
        exit(0)
    test(sys.argv)
