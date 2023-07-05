from setuptools import setup, find_packages

# setup(
#     name='src-layout-package',
#     version='0.0.1',
#     packages=find_packages(where='src'),
#     package_dir={'': 'src'},
#     description="src layout package",
# )
# src > mypackage

setup(
    name='src-layout-package',
    version='0.0.1',
    packages=find_packages(where='src'),
    package_dir={'top': 'src'},
    description="src layout package",
)
# src as mypackage