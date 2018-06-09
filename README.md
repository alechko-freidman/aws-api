# AWS API - List​ AWS​ ​services

List​ ​AWS​ ​services​ ​being​ ​used​ ​region​ ​wise

### Getting Started

There are two scripts in this project  

* **list_services_by_cost_exporer.py** uses aws cost explorer to show high level usage
* **list_services_by_config_svc.py** uses aws config service to show all discovered services. 
  * Please pay attention that the script shows only services currently supported by aws config service.

For detailed report much more complex solution is requred (similar to [JohannesEbke/aws_list_all](https://github.com/JohannesEbke/aws_list_all))
 

### Prerequisites

* aws config should be properly configured

```
aws configure --profile XXX
...
export AWS_PROFILE=XXX
```

* aws readonly permissions for **ec2, ce and config** services are required


### Examples

```
python list_services/list_services_by_cost.py
python list_services/list_services_by_config_svc.py
```

