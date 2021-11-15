
import sys
sys.path.append('../.') # add parent folder to  PYTHONPATH
#if sys.version_info[0] >= 3:
#    raw_input = input

try:
    import a23pars
    import interpret

    # If a filename has been specified, we read program from there:
    if len(sys.argv) == 2:
        text = open(sys.argv[1]).read()
    else :
        # Read input program from terminal: 
        print("Type program; OK to do it on multiple lines; terminate with  !")
        print("  as the first symbol on a line by itself:")
        print()
        text = ""
        line = input("")
        while line == ""  or  line[0] != "!" :
           text = text + " " + line + "\n"
           line = input("")

    tree = a23pars.parse(text)
    print("Parse tree:")
    print(tree)
    print("Execution:")
    interpret.interpretPTREE(tree)
except:  # an error:
   import traceback
   traceback.print_exc()

print(input("Press Enter key to terminate"))

