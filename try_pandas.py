# I'm using Spark Cloud Community Edition, sicne my own machine cannot have the right numpy for pandas...
# So, in this code, so features could only be used in Spark Cloud Python Notebook
# Try pandas :)

# cell 1 - load the data (I upload the .csv into Spark Cloud first)
import pandas as pd
import numpy as np

## The path here is the .csv file path in HDFS
pdata = sqlContext.read.format('csv').load("/FileStore/tables/[file name in HDFS]", 
                                       index_col="ID", header =True).toPandas()
                                       
                                       
# cell 2 - Bollean Indexing
pdata.loc[(pdata["Gender"]=="Female") & (pdata["Salary_Account"]=="ICICI Bank") & (pdata["Mobile_Verified"]=="Y"), 
["Gender", "Salary_Account", "Mobile_Verified"]]


# cell 3 - apply function, similar to R apply()
def get_missing_data(x):
  return sum(x.isnull())

print "find missing data for each column:"
print pdata.apply(get_missing_data, axis = 0)

print "find missing data for each row:"
print pdata.apply(get_missing_data, axis = 1)
