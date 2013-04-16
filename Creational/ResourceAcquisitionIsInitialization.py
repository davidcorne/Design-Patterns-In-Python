#!/usr/bin/env python
# Written by: DGC

# python imports

# local imports

#==============================================================================
class RAII(object):
    
    def __init__(self):
        pass

    def __enter__(self):
        print("Resource Allocated")

    def __exit__(self, exception_type, exception_value, traceback):
        all_none = all(
            arg is None for arg in [exception_type, exception_value, traceback]
            )
        if (not all_none):
            print("Exception: " + str(exception_type) + " raised")
        print("Resource Freed")
        print("")

#==============================================================================
if (__name__ == "__main__"):
    with RAII() as r:
        pass
    with RAII() as r:
        raise Exception
    print("end")
