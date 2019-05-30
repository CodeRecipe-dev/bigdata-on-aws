# Building up an AWS big data pipeline 

by: zaicheng wang

Mode info at: https://coderecipe.ai/architectures/86530220


### Prerequisites

Make sure you have AWS access key and secrete keys setup locally, following this video [here](https://www.youtube.com/watch?v=_f0d2pLJjiA)

### Download the code locally

```  
serverless create --template-url {} --path AWS-bigdata-pipeline
```

### Deploy to the cloud  

```
cd AWS-bigdata-pipeline

npm install serverless
npm install serverless-pseudo-parameters

serverless deploy --stage <your-stage-name>
```

### Put sample data to firehose using AWS CLI
```
cd AWS-bigdata-pipeline
aws firehose put-record --delivery-stream-name data-pipeline-dev-Deliverystream-XTJ8GY3H9DUH --record file://data/small.json

```

### Run Sql query on Athena
```sql
aws athena start-query-execution --cli-input-json file://athena-cli/start-query-execution.json
aws athena get-query-results --query-execution-id {query id from last command}
```

### Create Quicksight Dashboard
https://docs.aws.amazon.com/quicksight/latest/user/example-create-a-dashboard.html
