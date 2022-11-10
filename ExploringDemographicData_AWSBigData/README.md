# Amazon Athena

## Seventh Project Challenge


### Description:

Explore the power of SQL in a fully managed BigData tool on AWS, Amazon Athena. 

Project requirements: 
 - Amazon S3
 - Amazon Glue
 - Amazon Athena
 - Amazon QuickSight

### Resolution:

Project paths:
1. Create bucket in Amazon S3;
2. Create Glue Crawler;
3. Create application in Amazon Athena;
4. Create tables;
5. Visualize data in Amazon QuickSight.


### Creating bucket in Amazon S3

- Amazon S3 Console -> Buckets -> Create bucket -> Bucket name [nome_do bucket] - Create bucket
- Create two folders (Onefolder called ```/output``` and another with the your dataset name. This name will define the name of the table created in Glue)
- Upload the data files located in the folder  ```/data```

#### Creating Glue Crawler

- Amazon Glue Console -> Crawlers -> Add Crawler
- Source type [Data Stores] -> Crawl all folders
- Data store [S3] -> Include path [inout data directory path]
- Create IAM Role
- Frequency [Run on demand]
- Database name [a_database_name]
- Group behavior [Create a single schema for each S3 path]
- Finish
- Databases -> Tables -> View data from created tables

### Creating application in Amazon Athen

- Query editor -> Settings -> Manage settings -> Query result location and encryption -> Browse S3 -> select the bucket created
- Select Database -> create queries (folder examples ```/src```)
- Check unsaved queries in bucket created in S3
- Save queries -> Execute again -> Verify the bucket created in S3 

#### Creating tables

- Generate table DDL
- Copy the generated query 
- Select the database and create a new table in a new query

### Visualizing data in Amazon QuickSight

- Signup (in case you don't have account) -> Choose [Standard]
- Datasets -> Create new dataset -> Athena -> Name [DataSetName] -> Create
- Select database -> select table -> Edit or preview -> Save & visualize
- Create visualizations by selecting columns, creating filters and parameters, and selecting Visual types for charts.


Adapted from: Prof. Cassiano Ricardo de Oliveira Peres - [Digital Innovation One](https://www.dio.me/) and [GitHub](https://github.com/cassianobrexbit/dio-live-athena)
