# main.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

from modulefinder import Module
from utilitiesPackage.utilities import *

if __name__ == "__main__":
    print("Starting...")
    from groupPackage.test import *
    module_names, modules = run_modules_in_package("groupPackage")

    #print("Modules that were loaded:")
    #for module in modules:
    #    print(module)

    expected_function = "print_me"   # No parens should be used here
    for module in modules:
        #print(module)
        attributes = sorted(dir(module))
        #if attributes:
        #    for attribute in attributes:
        #        print(attribute)
        function = getattr(module, expected_function)
        if callable(function):
            print("Executing", expected_function + "()", "in", module.__str__().split("\\\\")[-1][:-2])
            function()