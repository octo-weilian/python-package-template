# Simple Python project template 2022

Notes: 
* `pyproject.toml` with PEP621 (new style metadata)
* `my_app.utils` example package with standard logging and configuration methods
* `__main__.py` entrypoint with `my_app.__main__:main` as console script  
* `pytest` for testing
* `pip` for installation interface
* `build` for packaging and distribution 
* `setuptools>=61.0` for build backend

How to use (Linux):
1. Copy template and cd to the directory    
`cd /python-project-template-2022`
2. Create a virtual environment    
`python3 -m venv .venv`
3. Activate the virtual environment     
`source .venv/bin/activate`

4. Upgrade pip and setuptools   
`pip install pip setuptools --upgrade`

4. Start develop mode (pip editable mode/ editable install). This will also install the dependencies specified in `pyproject.toml`.   
`python3 -m pip install -e .`

5. Test the console command     
`my_app hello`

6. Run a test. The test is run against the current editable install outside the code.   
`pytest -sv`

7. Build distribution packages (tarball and wheels)
`python3 -m build`

<br>

<iframe
  src="https://carbon.now.sh/embed?bg=rgba%28255%2C255%2C255%2C1%29&t=vscode&wt=none&l=application%2Fx-sh&width=680&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=13px&lh=150%25&si=false&es=2x&wm=false&code=%28.venv%29%2520username%2540desktop%253A%7E%252Frepo%252Fpython-package-template%2524%2520my_app%2520hello%250A02-Jan%252019%253A46%253A56%2520main%2520%255BINFO%255D%2520-%2520Input%2520arguments%253A%2520%255B%27hello%27%255D%250A02-Jan%252019%253A46%253A56%2520main%2520%255BINFO%255D%2520-%2520Set%2520parameters%2520in%2520%252Fhome%252Fusername%252Frepo%252Fpython-package-template%252Fsrc%252Fmy_app%252Fconf.ini%253A%250Aparam_a%2520%2520%2520%253Afile.txt%250Aparam_b%2520%2520%2520%253ATrue%250Aparam_c%2520%2520%2520%253A100%250Aparam_d%2520%2520%2520%253A0.5"
  style="width: 1024px; height: 380px; border:0; transform: scale(1); overflow:hidden;"
  sandbox="allow-scripts allow-same-origin">
</iframe>

Tips:
* Disable pip install on your global environment     
`pip config set global.require-virtualenv True`

