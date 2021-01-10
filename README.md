# ETL for MongoDB
In this ETL process, data is extracted from Excel and txt files, transform and loaded into MongoDB. Whole process is done using Python script.  To apply separation of the ETL process steps, whole code is separated is three scrips: ExtractScript.py, TransformScript.py and LoadScript.py. Additional scripts as CommonFuncScript.py contains common functions that can be used by any of these three scripts and ReportScript.py contains functions for report generation.
<img src="https://github.com/EmiDim/ETLforMongoDB/blob/main/PythonScriptFlow.PNG">

## Extract Source Data
Process of extracting data is written in Python ExtractScript.py.  Each file extraction is done in its own function and returns table of extracted data.

## Transform Data
Process of extracting data is written in Python ExtractScript.py.  Each file’s extracted data is transformed in its own function and returns table of transformed data.

## Load Destination Data
Process of loading data is written in Python LoadScript.py. Connection string for mongoDB is wrapped in getMongoConnectionStr() function so that maintenance will be easier. 
Loading to MongoDB is done in Load2Mongo() function using pymongo library.
