import sys, inspect
import src
from src import *

class_functions = {}
class_doc = {}

def find_classes():
    for module in src.__all__:
        for name, obj in inspect.getmembers(sys.modules['src.' + module]):
            if inspect.isclass(obj):
                functions = [func for func in inspect.getmembers(obj) if inspect.isfunction(func[1])]
                func_dict = {}
                for member in functions:

                    if  member.__doc__ and "__" not in member:
                        # print("adding member: {0}".format(member))
                        func_dict[member[0]] = (inspect.getdoc(member[1]), inspect.signature(member[1]))
                class_functions[name] = func_dict
                class_doc[name] = inspect.getdoc(obj) 

def create_md_file(classname, classdoc, functions):
    if len(functions) < 1 and classdoc is "": return
    
    title = "# {0} \n ```\n {1} \n```\n"
    function_def = "## {0}{1} \n\n  \n\n > {2} \n\n"

    classdoc.replace("\n", "\n\n") if classdoc is not None else 0

    full_file = title.format(classname, classdoc)
    
    for fn in functions:
        if functions[fn][0] is not None:
            # functions[fn][0] is the docstring, functions[fn][1] is the signature, 
            fstring = functions[fn][0]
            fstring = fstring.replace("\n", "\n\n ")
            fstring = fstring.replace("Keyword arguments:", "**Keyword arguments:**")
            fstring = fstring.replace("Returns:", "**Returns:**")
            full_file += function_def.format(fn, functions[fn][1], fstring)

    full_file += "--- "
    file = open("docs/{0}.md".format(classname), "w") 
    file.write(full_file)


find_classes()
for cn in class_functions:
    create_md_file(cn, class_doc[cn], class_functions[cn])

print(type(find_classes))
