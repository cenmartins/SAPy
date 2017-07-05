from setuptools import setup

setup(name="SAPy",
      packages=["sapy"],
      package_data={"sapy": ["icons/*.svg"]},
      classifiers=["Example :: Invalid"],
      # Declare orangedemo package to contain widgets for the "SAPy" category
      entry_points={"orange.widgets": "SAPy = sapy"},
      )
