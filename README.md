# HyperCube API

Let you access all your Data on HyperCube Data Platform 

visit https://www.hcube.io

# Quick installation

In order to run the HyperAPI module, you need at least Python v3.6+ installed on your system and running as the main python environment. Then you need to install PiPy and do the following commands.

#### On Linux and MacOS
````
$> python --version
Python 3.6.5
````

````
# Taking into account that your main python is Python 3.6+
$> curl -O https://bootstrap.pypa.io/get-pip.py
$> python get-pip.py
$> python pip install -r requirements.txt
````
Then you can run a python prompt
````
$> PYTHONPATH=<path to the HyperAPI directory> python
import HyperAPI
````
