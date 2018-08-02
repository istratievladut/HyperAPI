.. hyper_api documentation master file, created by
   sphinx-quickstart on Wed May 16 11:22:58 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to hyper_api's documentation!
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

API reference
=====================================   

Project
-------

.. automodule:: project
   :members:

Dataset
-------

.. automodule:: dataset
   :members:

Target
------

.. automodule:: target
   :members:

Xray
----

.. automodule:: xray
   :members:

.. automodule:: xrayvariable
   :members:
   
Ruleset
-------

.. automodule:: ruleset
   :members:
   
Model
-----

.. automodule:: model
   :members:
   
Examples
==================

Each of these examples is built upon the previous ones so they should be executed in order.

Authentication
---------------
* Copy the API token from your Settings in HyperCube
* In a new Notebook on HyperCube, paste the token to initialize the Api::

	API_TOKEN = 'PASTE YOUR TOKEN HERE'
	from hypercube_api import Api
	api = Api(token=API_TOKEN)


    
Project
-------
* Create a project: get_or_create, create
* List and filter projects: filter
* Retrieve a project: get
* Set a project as default: set_as_default
* Delete a project: delete::

	# Create a project
	PRJ_NAME = "Demo_API_Project"
	project = api.Project.get_or_create(PRJ_NAME)
	
	# List
	print('List of projects:')
	for _project in api.Project.filter(): print('\t- {}'.format(_project.name))
	
	# Retrieve a project
	project = api.Project.get(PRJ_NAME)
	
	# Set project as default
	project.set_as_default()
	
	# Display info about the project
	print(project)
	print('Is "{}" default project ?: {}'.format(project.name, project.is_default))


Dataset
-------

* Create a dataset: get_or_create, create, create_from_dataframe
* List and filter datasets: filter
* Retrieve a dataset: get
* Set a dataset as default: set_as_default
* Split the dataset: split
* Delete a dataset: delete::

	# Upload data file on HyperCube platform:
	# In the Notebook interface, click 'Upload Files' button and select the data file
	# This is 'Titanic.csv' in our example
	
	# Define Dataset Name and Path
	DS_NAME = "Demo_API_Dataset"
	import os
	DS_PATH = os.path.join(os.getcwd(), 'Titanic.csv')
	
	# Create
	dataset = project.Dataset.get_or_create(DS_NAME, DS_PATH, delimiter=';')
	
	# List and filter
	print(project.Dataset.filter())
	#print(project.datasets)
	
	# Retrieve a dataset
	dataset = project.Dataset.get(DS_NAME)
	
	# Set dataset as default
	dataset.set_as_default()
	
	# Display info about the dataset
	print(dataset)
	print('Is "{}" default dataset ?: {}'.format(dataset.name, dataset.is_default))
	
	# Split dataset : train/test
	dataset_train, dataset_test = dataset.split()
	print('Name of the train dataset: {}'.format(dataset_train.name))
	print('Name of the test dataset: {}'.format(dataset_test.name))


Variable
--------
* List and filter variables: filter
* Retrieve a variable: get
* Ignore / Keep a variable: ignore / keep::

	# List variables
	print(dataset.Variable.filter())
	#print(dataset.variables)
	
	# Retrieve a variable
	variable = dataset.Variable.get('Survival_Status')
	variable_2 = dataset.Variable.get('ID')
	
	# Display info about the variable
	print(variable)
	print('Variable missing value count: {}'.format(variable.missing_value_count))
	print('Variable modalities: {}'.format(variable.modalities))
	
	# Ignore a variable
	variable_2.ignore()


Target
-------
* Create a target: create, create_targets, create_description
* List and filter targets: filter
* Retrieve a target: get
* Delete a target: delete::

	# Create a target or a description
	# Note that the creation of a target automatically creates the corresponding description
	target = project.Target.create(variable, 'alive')
	target_2 = project.Target.create(dataset.Variable.get('Age'), scoreTypes=["Average value", 
	                                 "Standard deviation", "Shift"])
	
	# List targets
	print(project.Target.filter())
	#print(project.targets)
	
	# Get a target or description
	TARGET_NAME = variable.name + '_description'
	description = project.Target.get(TARGET_NAME)
	
	# Display info about the target
	print(target)
	print('Target type: {}'.format(target.indicator_type))


Xray
------

* Create a Xray: get_or_create, create
* List and filter Xrays: filter
* Retrieve a Xray: get
* Delete a Xray: delete

* List Xray variables: Variable.filter
* Retrieve a Xray variable: Variable.get
* Sort Xray variables by contrast rate: Variable.sort
* Get contrast rates on a Xray variable: contrast_rates::

	# Create Xray
	XRAY_NAME = "Demo_API_Xray"
	xray = project.Xray.get_or_create(dataset, XRAY_NAME, description)
	
	# List Xrays
	print(project.Xray.filter())   # lists on the project
	#print(dataset.xrays)          # lists on the dataset
	
	# Get Xray
	xray = project.Xray.get(XRAY_NAME)
	
	# List Xray variables
	print(xray.Variable.filter())   # unsorted
	#print(xray.variables)          # sorted on contrast rate if possible
	
	# Sort Xray variables by contrast rate
	print(xray.Variable.sort(description.variable_name, reverse=True))
	
	# Retrieve a Xray variable
	xray_var = xray.Variable.get('Age')
	
	# Display info about the Xray variable
	print(xray_var)
	print('contrast rate: {}'.format(xray_var.contrast_rates.get(description.variable_name)))


Ruleset
---------

* Create a Ruleset: get_or_create, create
* List and filter Rulesets: filter
* Retrieve a Ruleset: get
* Retrieve rules on the Ruleset: get_rules
* Minmize the Ruleset : minimize
* Create a Model from the Ruleset: predict_from_ruleset
* Delete a ruleset::

	# Create Ruleset
	RULESET_NAME = "Demo_API_Ruleset"
	ruleset = project.Ruleset.get_or_create(dataset, RULESET_NAME, target)
	
	other_key_indicator_1 = project.Ruleset.create_kpi_option(target_2, 
	                                                          average_value_min=30, 
	                                                          average_value_max=100)
	RULESET_NAME_2 = "Demo_API_Ruleset_2"
	ruleset_2 = project.Ruleset.get_or_create(dataset, RULESET_NAME_2, target, 
	                                          compute_other_key_indicators=[other_key_indicator_1])
	
	# List Rulesets
	print(project.Ruleset.filter())   # lists on the project
	#print(dataset.rulesets)          # lists on the dataset
	
	# Retrieve a Ruleset
	ruleset = project.Ruleset.get(RULESET_NAME)
	
	# Retrieve all rules on the Ruleset
	ruleset.get_rules()
	
	# Minimize the ruleset
	minimized_ruleset = ruleset.minimize('Demo_API_Minimized_Ruleset')
	
	# Create a Model from the Ruleset
	model = ruleset.predict_from_ruleset()
	print(model)


Model
-------
* Create a HyperCube model: get_or_create_hypercube, create_hypercube
* List and filter Rulesets: filter
* Retrieve a Ruleset: get
* Delete a model: delete

* Score the model on a test set: predict_scores
* Apply the model (As in the HyperCube UI): apply
* Export the scores: export_scores
* Export the model: export_model

* Display curves: display_curve
* Confusion matrix: get_confusion_matrix::

	# Create a HyperCube model
	MODEL_NAME = "Demo_API_Model"
	model = project.Model.get_or_create_hypercube(dataset=dataset_train, name=MODEL_NAME, target=target)
	
	# List Models
	print(project.Model.filter())
	#print(project.models)
	
	# Retrieve a Model
	model = project.Model.get(MODEL_NAME)
	
	# Display info about a Model
	print(model)
	print('Model name : {}'.format(model.name))

	# Score the test dataset
	scores = model.predict_scores(dataset_test)
	print('type of output: {}'.format(type(scores)))
	print(scores)
	
	# Apply the model as in the HyperCube UI
	applied_model = model.apply(dataset_test, 'Demo_API_Applied_Model')
	print(applied_model)

	# Export the scores
	SCORE_FILE=r'ENTER PATH HERE\scores.csv'
	applied_model.export_scores(SCORE_FILE)

	# Export the model
	MODEL_FILE=r'ENTER PATH HERE\H3Model.py'
	applied_model.export_model(MODEL_FILE, format='Python')
	
	# Display curves
	model.display_curve()                        # ROC curve
	model.display_curve(curve = 'Lift curve')
	model.display_curve(curve = 'Gain curve')
	model.display_curve(curve = 'Precision Recall')

	# Confusion matrix
	conf = model.get_confusion_matrix(0.1)
	conf.false_negatives


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
