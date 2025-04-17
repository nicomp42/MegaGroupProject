# main.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

import io
import contextlib
from modulefinder import Module
from utilitiesPackage.utilities import *


if __name__ == "__main__":
    print("Starting...")
    module_names, modules = run_modules_in_package("groupPackage")

    #print("Modules that were loaded:")
    #for module in modules:
    #    print(module)

    expected_function = "get_favorite_food"   # No parens should be used here
    favorite_foods = dict()
    success_count = 0
    failure_count = 0
    expected_class_name = "GroupCollaboration"
    output = io.StringIO()
    for module in modules:
        #print(module)
        attributes = sorted(dir(module))
        module_name = module.__str__().split("\\\\")[-1][:-2]
        #if attributes:
        #    print("Attributes...")
        #    for attribute in attributes:
        #        print(attribute)
        try:
            print("Instantiating class in", module.__str__().split("\\\\")[-1][:-2])
            cls = getattr(module, expected_class_name)
            instance = cls()   # Invokes __init__
            
            favorite_food = instance.get_favorite_food()
            favorite_foods[module_name] = favorite_food

            success_count = success_count + 1
            """
            function = getattr(module, expected_function)
            if callable(function):
                print("Executing", expected_function + "()", "in", module.__str__().split("\\\\")[-1][:-2])
                try:
                    favorite_food = getattr(module, expected_function)()
                    favorite_foods[module_name] = favorite_food
                    success_count = success_count + 1
                    #print("  favorite food is", favorite_food)
                except Exception as e:
                    print(e)
                    failure_count = failure_count + 1
             """
        except Exception as e:
            print(e)
            failure_count = failure_count + 1
    print("======================================================")
    print("Success count: ", success_count, "Failure count:", failure_count)
    print("Favorite Foods:")
    print(favorite_foods)