# Amazon Athena

## Seventh Project Challenge


### Description:

Explore the power of SQL in a fully managed Big Data tools on AWS. 

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
![alt text](https://github.com/Pmms89/DIO_Bootcamp_DataScience-Geracao-Tech-Unimed-BH-/blob/main/ExploringDemographicData_AWSBigData/Step_by_step_images/1_Create_bucket.png)

- Create two folders (One folder called ```/output``` and another with the your dataset name. This name will define the name of the table created in Glue)
![alt text](https://github.com/Pmms89/DIO_Bootcamp_DataScience-Geracao-Tech-Unimed-BH-/blob/main/ExploringDemographicData_AWSBigData/Step_by_step_images/2_Creating_folder.png)

![alt text](https://github.com/Pmms89/DIO_Bootcamp_DataScience-Geracao-Tech-Unimed-BH-/blob/main/ExploringDemographicData_AWSBigData/Step_by_step_images/3_Creating_folder2.png)

- Upload the data files located in the folder  ```/data```

![alt text](https://github.com/Pmms89/DIO_Bootcamp_DataScience-Geracao-Tech-Unimed-BH-/blob/main/ExploringDemographicData_AWSBigData/Step_by_step_images/4_Upload.png)

![alt text](https://github.com/Pmms89/DIO_Bootcamp_DataScience-Geracao-Tech-Unimed-BH-/blob/main/ExploringDemographicData_AWSBigData/Step_by_step_images/5_Add_files.png)

#### Creating Glue Crawler

- Amazon Glue Console -> Crawlers -> Add Crawler
![alt text](https://github.com/Pmms89/DIO_Bootcamp_DataScience-Geracao-Tech-Unimed-BH-/blob/main/ExploringDemographicData_AWSBigData/Step_by_step_images/6_AWS_Glue_crawler.png)

- Source type [Data Stores] -> Crawl all folders
- Data store [S3] -> Include path [input data directory path]
![alt text](https://github.com/Pmms89/DIO_Bootcamp_DataScience-Geracao-Tech-Unimed-BH-/blob/main/ExploringDemographicData_AWSBigData/Step_by_step_images/7_Add_data_fromFolder_NOT_File.png)

- Create IAM Role
![alt text](https://github.com/Pmms89/DIO_Bootcamp_DataScience-Geracao-Tech-Unimed-BH-/blob/main/ExploringDemographicData_AWSBigData/Step_by_step_images/8_IAM_Role.png)

- Frequency [Run on demand]
![alt text](https://github.com/Pmms89/DIO_Bootcamp_DataScience-Geracao-Tech-Unimed-BH-/blob/main/ExploringDemographicData_AWSBigData/Step_by_step_images/9_Run_Crawler.png)

- Database name [a_database_name]
- Group behavior [Create a single schema for each S3 path]
- Finish
- Databases -> Tables -> View data from created tables
![alt text](https://github.com/Pmms89/DIO_Bootcamp_DataScience-Geracao-Tech-Unimed-BH-/blob/main/ExploringDemographicData_AWSBigData/Step_by_step_images/10_See_Table.png)
P.S.: You can change data type in the table.

### Creating application in Amazon Athena

![alt text](https://github.com/Pmms89/DIO_Bootcamp_DataScience-Geracao-Tech-Unimed-BH-/blob/main/ExploringDemographicData_AWSBigData/Step_by_step_images/11_Athena.png)

![alt text](https://github.com/Pmms89/DIO_Bootcamp_DataScience-Geracao-Tech-Unimed-BH-/blob/main/ExploringDemographicData_AWSBigData/Step_by_step_images/12_Database_Table_recognized.png)

- Query editor -> Settings -> Manage settings -> Query result location and encryption -> Browse S3 -> select the bucket created
![alt text](https://github.com/Pmms89/DIO_Bootcamp_DataScience-Geracao-Tech-Unimed-BH-/blob/main/ExploringDemographicData_AWSBigData/Step_by_step_images/13_Define_whereQueries_willBe_saved.png)

![alt text](https://github.com/Pmms89/DIO_Bootcamp_DataScience-Geracao-Tech-Unimed-BH-/blob/main/ExploringDemographicData_AWSBigData/Step_by_step_images/14_Manage_save.png)

![alt text](https://github.com/Pmms89/DIO_Bootcamp_DataScience-Geracao-Tech-Unimed-BH-/blob/main/ExploringDemographicData_AWSBigData/Step_by_step_images/15_Define_output_save.png)

- Select Database -> create queries (folder examples ```/src```)
![alt text](https://github.com/Pmms89/DIO_Bootcamp_DataScience-Geracao-Tech-Unimed-BH-/blob/main/ExploringDemographicData_AWSBigData/Step_by_step_images/16_Now_You_can_Run_SQL_Queries.png)
P.S.: The queries are saved in .csv file format; you also can create new tables from the original table

- Check unsaved queries in bucket created in S3
- Save queries -> Execute again -> Verify the bucket created in S3 
![alt text](https://github.com/Pmms89/DIO_Bootcamp_DataScience-Geracao-Tech-Unimed-BH-/blob/main/ExploringDemographicData_AWSBigData/Step_by_step_images/17_Open_specific_query.png)

![alt text](https://github.com/Pmms89/DIO_Bootcamp_DataScience-Geracao-Tech-Unimed-BH-/blob/main/ExploringDemographicData_AWSBigData/Step_by_step_images/18_extract_result.png)

#### Creating tables

- Generate table DDL
- Copy the generated query 
- Select the database and create a new table in a new query

### Visualizing data in Amazon QuickSight

- Signup (in case you don't have account) -> Choose [Standard]
![alt text](https://github.com/Pmms89/DIO_Bootcamp_DataScience-Geracao-Tech-Unimed-BH-/blob/main/ExploringDemographicData_AWSBigData/Step_by_step_images/19_Quicksight.png)

- Datasets -> Create new dataset -> Athena -> Name [DataSetName] -> Create
- Select database -> select table -> Edit or preview -> Save & visualize
![alt text](https://github.com/Pmms89/DIO_Bootcamp_DataScience-Geracao-Tech-Unimed-BH-/blob/main/ExploringDemographicData_AWSBigData/Step_by_step_images/20_ADD_New_datasets.png)

![alt text](https://github.com/Pmms89/DIO_Bootcamp_DataScience-Geracao-Tech-Unimed-BH-/blob/main/ExploringDemographicData_AWSBigData/Step_by_step_images/21_dataset_basedOn_Athena.png)

![alt text](https://github.com/Pmms89/DIO_Bootcamp_DataScience-Geracao-Tech-Unimed-BH-/blob/main/ExploringDemographicData_AWSBigData/Step_by_step_images/22_Choose_database.png)
P.S.: Remember to set QuickSight at the same region of your dataset otherwise you can not find it!!


- Create visualizations by selecting columns, creating filters and parameters, and selecting Visual types for charts.

![alt text](https://github.com/Pmms89/DIO_Bootcamp_DataScience-Geracao-Tech-Unimed-BH-/blob/main/ExploringDemographicData_AWSBigData/Step_by_step_images/23_Create_Dashboard.png)


### References
Adapted from: Prof. Cassiano Ricardo de Oliveira Peres - [Digital Innovation One](https://www.dio.me/) and [GitHub](https://github.com/cassianobrexbit/dio-live-athena)
