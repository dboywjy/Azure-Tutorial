## Azure Machine Learning

### prerequisites

#### Data

The data is created through Sklearn. The creation code can be found in './generate_data.ipynb'.

#### Azure Account

You can register a student account and get 200 credits.

Then you should do the following steps:

1. create a workspace
2. subscribe to a compute instance
3. create a notebbook


### Quick start

1. Create handle to workspace
2. Access the registered data asset
    - you should upload your data into your data store
3. Create a job environment for pipeline steps
4. Build the training pipeline
5. Create component 2: training (using yaml definition)
6. Create the pipeline from components
7. Submit the job
8. Create a new online endpoint
9. Deploy the model to the endpoint
10. Test with a sample query
11. Clean up resources
    - the virtual machine will consistently use the credits if you do not close it

The quick start notebook can be found './quick_start.ipynb', you only need to fill in the first cell with your workspace information. Then you can keep executing the cells.

#### Some key words explanations:
- workspace: the place where you store your data, models, and compute resources
  
- compute instance: You can see it as a virtual machine. 
    - And if the compute instance you are using can not meet the requirement in the code below, you can choose a lower deployment instance type or a better [compute instance type](https://learn.microsoft.com/en-us/azure/virtual-machines/dcv2-series).

    ```
    blue_deployment = ManagedOnlineDeployment(  
    name="blue",  
    endpoint_name=online_endpoint_name,  
    model=model,  
    instance_type="Standard_DS2_v2",
    instance_count=1,)
    ```

- pipeline: Azure Pipelines automatically builds and tests code projects. It supports all major languages and project types and combines continuous integration, continuous delivery, and continuous testing to build, test, and deliver your code to any destination

- components: You can treat is as a syntax and you just need to add fixed code like building LEGO.

- endpoint: Endpoints act as the entry points or destinations for client applications to interact with a web service or API. You can see it as one kind of API(Application Programming Interface).











