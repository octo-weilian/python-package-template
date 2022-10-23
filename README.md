# python-package-template
Repository for a reusable Python project/ package template. 

This template uses ```setuptools``` to build Python source distribution and/ or wheel. 
Make sure to pip install ```setuptools``` and ```wheel```.

Python project structure:  

```
my-app
│   appConfig.ini
│   main.py
│   README.md
│   requirements.txt
│   setup.bat
│   setup.py
│
└───my_app
    │   subpackage_a.py
    │   subpackage_b.py
    │   __init__.py
    │
    └───utils
            config.py
            logger.py
            __init__.py
```

File structure description:
- The utils module provide basic methods for configuration and logging 
- The main.py is the main program to execute the package
- The configuration *.ini file has to be generated manually. It is recommended to read the configuration file from the main program.
- Two example loggers: 
  - without termination (similar to ```print(end='\n')```)
  - with termination (similar to ```print(end='\r')```)

How to create a Python package:  
1. Create a project folder. This is also your root/ repository folder.    
```mkdir my-app```

2. Copy content of *python-package-template* to your project folder  

3. Create a virtual environment   
```python -m venv .venv```

5. Activate your virtual environment
```.venv\Scripts\activate.bat```

5. Install additional packages  
```pip install requests```

6. Develop your app in *my_app* folder. This is your main package. You can create subpackages/ folders.   
(Dont forget to include a ```__init__.py``` file for each subpackage) 

7. Output dependencies in requirements format  
```pip freeze > requirements.txt```

8. Run *setup.bat* to build source distribution and wheel   
