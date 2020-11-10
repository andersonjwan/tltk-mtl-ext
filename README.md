# Temporal Logic ToolKit MTL Extended

The temporal logic toolkit MTL extended is an extension of the Python library [tltk-mtl](https://pypi.org/project/tltk-mtl/). It enables the user to seamlessly write MTL formulas using specific syntax passed as a string to a parser translator that returns the formulated logical MTL statement.

## How to Use

To use the module, there is no currently available pip installation; therefore, everything will have to be organized locally by you.

### Dependencies
In order to run take advantage of the library, the following dependencies must be installed:

1. Python3
2. TLTk MTL Python Library
3. ANTLRv4 Python Runtime

#### Installing TLTk MTL Python Library
The TLTk MTL Python library has four dependencies, so be sure that you have all before installing it. The list of dependencies are:

1. pip wheel
2. GNU-G++ Compiler
3. Make
4. Python3 Developer's Package

To install the **TLTK MTL Python Library**, run the following command:

```bash
pip3 install --user wheel
pip3 install --user tltk_mtl
```

#### Installing ANTLRv4 Python Runtime
With the `tltk-mtl` Python library installed, you should then install the **ANTLRv4 Python3 Runtime**. This can be done by running the following command:

```bash
pip3 install --user antlr4-python3-runtime
```

### Setting Path
Since the module is not installed system-wide, you can import the module various ways; however, the most dynamic on Linux systems would be to set the `$PYTHONPATH` environment variable to point to the path of the folder where `tltk_mtl_ext.py` is located.

In most cases this will be: `/path/to/tltk-mtl-ext/src/`

## Examples
There are various examples in the examples folder with **a** denoting the normal TLTk MTL syntax and **b** denoting the new use of a string to indicate the higher level logical formula.

If you have any questions, feel free to email me at jwande18@asu.edu.
