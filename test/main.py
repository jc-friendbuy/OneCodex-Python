
from __future__ import print_function
import nose
import sys
from os import path


def setup():
    """
    Add the source path to the system path, so that modules can be imported from the api source
    packages.

    This allows tests to be run for each of the api versions, by importing from the correct root
    package.

    For example, to test the Analysis class in the api v0, the import would be:

    from v0.analyses.Analysis import Analysis
    """
    print("Setting up testing environment")
    current_path = path.realpath(sys.argv[0])
    api_version_source_path = path.join(current_path, "../src/")
    sys.path = [path.realpath(api_version_source_path)] + sys.path


# Program entry point
setup()
nose.main()
