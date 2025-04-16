# utilities.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

import pkgutil
import importlib
import sys
import os
import traceback # Optional: for detailed error reporting

def run_modules_in_package(package_name, verbose = False):
    """
    Finds and imports (runs) all modules directly within the specified package.

    @param: package_name (str): The name of the package to scan.
    @return list: The module names that were imported
    """
    print(f"--- Attempting to run modules in package: {package_name} ---")

    try:
        # 1. Import the package itself to get its path
        package = importlib.import_module(package_name)
        package_path = package.__path__ # __path__ is a list of paths for the package
        package_prefix = package.__name__ + '.' # e.g., 'groupPackage.'

        if verbose: print(f"Package '{package_name}' found at: {package_path}")

    except ImportError:
        print(f"Error: Package '{package_name}' not found.")
        print("Ensure the package exists and this script is run from a location")
        print("where Python can find it (e.g., the directory containing the package).")
        return
    except AttributeError:
         print(f"Error: Package '{package_name}' does not seem to be a package ")
         print("(it might be missing an __init__.py file or is not structured correctly).")
         return

    # 2. Iterate over modules within the package path
    modules_found = 0
    modules_run = 0
    modules_failed = 0
    module_names = []
    modules_imported = []
    # Use pkgutil.walk_packages for recursive search if needed
    # For non-recursive (only modules directly in groupPackage):
    for _, module_name, is_pkg in pkgutil.iter_modules(package_path, prefix=package_prefix):
        module_names.append(module_name)
        modules_found += 1
        if is_pkg:
            # print(f"Skipping sub-package: {module_name}") # Optional: uncomment to see subpackages
            # If you want to recursively run modules in subpackages,
            # you would call this function again here:
            # run_modules_in_package(module_name)
            continue # Skip packages, only run modules (.py files)

        # 3. Import (and thus run) the module
        try:
            if verbose: print(f"\nAttempting to run module: {module_name}...")
            module_that_was_imported = importlib.import_module(module_name)
            modules_imported.append(module_that_was_imported)
            if verbose: print(f"Successfully ran module: {module_name}")
            modules_run += 1
        except Exception as e:
            print(f"Error running module {module_name}:")
            # traceback.print_exc() # Uncomment for full traceback
            print(f"  Error Type: {type(e).__name__}")
            print(f"  Error Details: {e}")
            modules_failed += 1
    if verbose:
        print("\n--- Finished running modules ---")
        print(f"Summary:")
        print(f"  Modules found (including subpackages): {modules_found}")
        print(f"  Modules attempted to run: {modules_run + modules_failed}")
        print(f"  Modules run successfully: {modules_run}")
        print(f"  Modules failed to run: {modules_failed}")

    return module_names, modules_imported

