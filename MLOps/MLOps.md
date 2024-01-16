## MLOps

### Overview
Machine Learning Operations (MLOps)

MLOps is based on Azure DevOps. The goals are:
- Faster experimentation and development of models
- Faster deployment of models into production
- Quality assurance and end-to-end lineage tracking

Machine Learning provides the following MLOps capabilities:
- Create reproducible machine learning pipelines.
- Create reusable software environments.
- Register, package, and deploy models from anywhere.
- Capture the governance data for the end-to-end machine learning lifecycle.
- Notify and alert on events in the machine learning lifecycle.
- Monitor machine learning applications for operational and machine learning-related issues.
- Automate the end-to-end machine learning lifecycle with Machine Learning and Azure Pipelines.

In model training, you may meet challenges for model training and deployment:
1. You need to train a model in a development workspace but deploy it an endpoint in a production workspace, possibly in a different Azure subscription or region.
2. You need to develop a training pipeline with test data or anonymized data in the development workspace but retrain the model with production data in the production workspace.

#### registry(注册表)

它将 ML 资产与工作区分离，并将它们托管在一个中心位置，从而使其可用于组织中的所有工作区。

实际流程可以这么理解：
![流程](./cross-workspace-mlops-with-registries.png)

Azure Machine Learning entities can be grouped into two broad categories：
- Assets such as **models**, **environments**, **components**, and **datasets** are durable entities that are workspace agnostic(无关的).
- Resources such as **compute**, **job**, and **endpoints** are transient entities that are workspace specific

Azure Machine Learning registries enable you to create and use those assets in different workspaces.

#### 






### Reference:
1. [MLOps Microsoft](https://learn.microsoft.com/zh-cn/azure/machine-learning/concept-model-management-and-deployment?view=azureml-api-2)
