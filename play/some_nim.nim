## Some comment about the module.

import nimpy

proc add(a: int, b: int): int {.exportpy.} =
    ## This is a docstring
    return a + b
