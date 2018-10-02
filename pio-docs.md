Installing Apache PredictionIO on Linux / MacOS
===============================================

Step 01: Downloading PredictionIO Binary Distribution



		https://predictionio.apache.org/templates/recommendation/quickstart/
1. Install and Run PredictionIO

2. Create a new Engine from an Engine Template

3. Generate an App ID and Access Key

4. Collecting Data

5. Deploy the Engine as a Service
Building
Training the Predictive Model
Deploying the Engine

6. Use the Engine

			https://predictionio.apache.org/templates/recommendation/quickstart/



Step 00: Choosing and Downloading an Engine Template



Step 01:

Step 01:

Step 01:

Step 01:

Step 01:

Step 01:


Import Events from Input File








pio app new myUniverseApp --access-key cts#2018

pio app new URApp --access-key CTS#2018


pio app new handmade --access-key CTS#2018


Name: MyURApp
=============
pio app new MyURApp 

ACCESS_KEY=zQxUVyk9g_9ufF2ZQ9rcLqaFGLgyTPmUqbQRwl8yISOAKSs7wNlTuhZJlZVx9Gzm





Import data with"

python3 examples/import_handmade.py --access_key CTS#2018"

Copy handmade-engine.json to engine.json

Run 'pio build', 'pio train', and 'pio deploy'

he queries mus




All docs for the Universal Recommender:
---------------------------------------
https://github.com/actionml/docs.actionml.com


e1b3007ff0720e78a640088775cb52153d55e9af



Engine Commands
===============

https://predictionio.apache.org/cli/


If you are using PostgreSQL or MySQL, skip pio-start-all and pio-stop-all, and do PredictionIO-0.13.0/bin/pio eventserver & instead.


Engine commands need to be run from the directory that contains the engine project. --debug and --verbose flags will provide debug and third-party informational messages.

```sh
PATH=$PATH:/home/yourname/PredictionIO/bin; export PATH		-> To set PIO binary command path


pio <command> [options] <args>...

pio eventserver 
pio eventserver & -> Start the event server

pio status -> Check the status of the dependencies

pio build -> Build the engine at the current directory.

pio train -> Kick off a training using an engine.

pio deploy -> Deploy an engine as an engine server.

pio batchpredict -> Process bulk predictions using an engine.

For deploy & batchpredict, if --engine-instance-id is not specified, it will use the latest trained instance.


pio dashboard   -> Start the dashboard


jps -l  -> Verify that you have everything started

pio build; pio train; pio deploy

pio build && pio train && pio deploy

```
General Commands:


curl -i -X GET http://localhost:7070	-> To check Server Status



Step : To export The Prediction IO Path
---------------------------------------
Let’s now export the Prediction IO path so we could freely use the pio command without pointing to it’s bin every time. Run the following command in your terminal:

PATH=$PATH:/home/abdurrazzak/pio/PredictionIO-0.13.0/bin; export PATH


PATH=$PATH:/opt/PIO/PredictionIO-0.13.0/bin; export PATH


PATH=$PATH:/home/abdurrazzak/pio/PredictionIO-0.12.1/bin; export PATH



PATH=$PATH:/home/abdurrazzak/PredictionIO-0.12.1/bin; export PATH


PATH=$PATH:/opt/PIO/PredictionIO-0.12.0-incubating/bin; export PATH


App ID and Access Key in the template '/home/abdurrazzak/MyECommerceRecommendation' for '/home/abdurrazzak/PredictionIO-0.12.1/'
-------------------------------------------------------------------------------------------------------------------------------

     	     Name |   ID |                         Access Key
-------------------------------------------------------------------------------------------
 	   MyApp1 |    2 | iP7QaLESl_RBa4B7QjXGRUdaA4V5EqsXL4ZP8XH-Eet6vZgM_z0d01aOVFbUBXoo 
ourrecommendation |    1 | hfIGieUM-R9qHMljwN8N1WO2kyaeOZW0CkB_GhDT3JX3MtEL4a57yKDEI7q7EyUU 


App ID and Access Key in the template '/home/abdurrazzak/pio/MyRecommendation' for '/home/abdurrazzak/PredictionIO-0.12.1/'
--------------------------------------------------------------------------------------------------------------------------

     	     Name |   ID |                         Access Key
-------------------------------------------------------------------------------------------
        MyTestApp |    3 | _o21kwiP8TPc3WrWxYZMwoKeYAGKR7t9afsywdnRgZaOXdcrBRVv22KvC73mOIqY 
 

App ID and Access Key in the template '/opt/PIO/lingpipe-MultiLabelClassification' for '/opt/PIO/PredictionIO-0.12.0-incubating'
-------------------------------------------------------------------------------------------------------------------------------

     	     Name |   ID |                         Access Key
-------------------------------------------------------------------------------------------
           myecom |    1 | tkb1cKoBXZZXAmqBK99aKdKmRGnxyy9yApVxgQ6ofEhr5GGnJH_8OKZIeZbTPlsG
ClassificationApp |    2 | _bAy_LfWiaztZDfx2jqFwbzLZsfeT5V6WG09m-XdyFqwYlMT-8dFQhoQRO8jPO4K
 
 



For convenience, set your access key to the shell variable:
-----------------------------------------------------------
ourrecommendation
-----------------
ACCESS_KEY=hfIGieUM-R9qHMljwN8N1WO2kyaeOZW0CkB_GhDT3JX3MtEL4a57yKDEI7q7EyUU

For MyApp1
----------
ACCESS_KEY=iP7QaLESl_RBa4B7QjXGRUdaA4V5EqsXL4ZP8XH-Eet6vZgM_z0d01aOVFbUBXoo

For MyTestApp
-------------
ACCESS_KEY="_o21kwiP8TPc3WrWxYZMwoKeYAGKR7t9afsywdnRgZaOXdcrBRVv22KvC73mOIqY"



For mecom:
----------
ACCESS_KEY=tkb1cKoBXZZXAmqBK99aKdKmRGnxyy9yApVxgQ6ofEhr5GGnJH_8OKZIeZbTPlsG


For ClassificationApp:
---------------------
ACCESS_KEY=_bAy_LfWiaztZDfx2jqFwbzLZsfeT5V6WG09m-XdyFqwYlMT-8dFQhoQRO8jPO4K


Name: MyURApp
=============
ACCESS_KEY=Q_Kark_8cxTn4YAZm-Kg-HNsnIqvyvopItR99neiEa23cz0NdTrGXGTphoBuD6ph


Name: URApp
ACCESS_KEY=CTS#2018
 

ACCESS_KEY=3CWD0e2YE1Dm5nWvmGqW0aRXXbWvgIWZiFSy_BbMsNCQEkOjbyTaf_6dkv7sv40v 



python data/import_eventserver.py --access_key tkb1cKoBXZZXAmqBK99aKdKmRGnxyy9yApVxgQ6ofEhr5GGnJH_8OKZIeZbTPlsG

curl -i -X GET "http://localhost:7070/events.json?accessKey=tkb1cKoBXZZXAmqBK99aKdKmRGnxyy9yApVxgQ6ofEhr5GGnJH_8OKZIeZbTPlsG"



pio import --appid 3 --input data/sample_movielens_data.txt

pio import --appid 1 --input data/sample-handmade-data.txt



Command Line		https://predictionio.apache.org/cli/#event-server-commands



Event Server Commands:
======================

pio app data-delete <your_app_name> -> Delete All Events of an App





predictionio Package Documentation
==================================		
    https://pythonhosted.org/PredictionIO/predictionio.html



PredictionIO Command Line:
========================== 			https://predictionio.apache.org/cli/#event-server-commands




To start the event server:			http://predictionio.apache.org/datacollection/eventapi/
--------------------------
pio eventserver		[OR] pio eventserver --ip 127.0.0.1 





> curl -i -X POST http://localhost:7070/events.json?accessKey=$ACCESS_KEY \
-H "Content-Type: application/json" \
-d '{
  "event" : "rate",
  "entityType" : "user",
  "entityId" : "u50",
  "targetEntityType" : "item",
  "targetEntityId" : "i50",
  "properties" : {
    "rating" : 5
  }
  "eventTime" : "2014-11-02T09:39:45.618-08:00"
}'



> curl -i -X POST http://localhost:7070/events.json?accessKey=$ACCESS_KEY \
-H "Content-Type: application/json" \
-d '{
  "event" : "buy",
  "entityType" : "user",
  "entityId" : "u49",
  "targetEntityType" : "item",
  "targetEntityId" : "i51",
  "eventTime" : "2014-11-10T12:34:56.123-08:00"
}'
> 



> abdurrazzak@ws15:~/pio/MyRecommendation$ curl -i -X POST http://localhost:7070/events.json?accessKey=$ACCESS_KEY \
> -H "Content-Type: application/json" \
> -d '{
>   "event" : "rate",
>   "entityType" : "user",
>   "entityId" : "u0",
>   "targetEntityType" : "item",
>   "targetEntityId" : "i0",
>   "properties" : {
>     "rating" : 5
>   }
>   "eventTime" : "2014-11-02T09:39:45.618-08:00"
> }'

HTTP/1.1 201 Created
Server: spray-can/1.3.3
Date: Wed, 19 Sep 2018 05:12:32 GMT
Content-Type: application/json; charset=UTF-8
Content-Length: 46

{"eventId":"c7d51e3d2ae54ff3b71a38f08cda8af9"}



abdurrazzak@ws15:~/pio/MyRecommendation$ curl -i -X POST http://localhost:7070/events.json?accessKey=$ACCESS_KEY \
> -H "Content-Type: application/json" \
> -d '{
>   "event" : "buy",
>   "entityType" : "user",
>   "entityId" : "u1",
>   "targetEntityType" : "item",
>   "targetEntityId" : "i2",
>   "eventTime" : "2014-11-10T12:34:56.123-08:00"
> }'

HTTP/1.1 201 Created
Server: spray-can/1.3.3
Date: Wed, 19 Sep 2018 05:13:07 GMT
Content-Type: application/json; charset=UTF-8
Content-Length: 46

{"eventId":"2916070823fa4d71a0624471cb957682"}






----------------------------------------------


Resources/References:

- Installing Apache PredictionIO on Linux / Mac OS X:
  https://predictionio.apache.org/install/install-linux/
  https://predictionio.apache.org/


- How to build a recommendation engine using Apache’s Prediction IO Machine Learning Server on Ubuntu 
  https://medium.freecodecamp.org/building-an-recommendation-engine-with-apache-prediction-io-ml-server-aed0319e0d8

- How to Install and Use Apache PredictionIO for Machine Learning on CentOS 7
  https://www.vultr.com/docs/how-to-install-and-use-apache-predictionio-for-machine-learning-on-centos-7


-------------------------------------------




Step# 1: Download Apache Prediction IO
---------------------------------------
git clone https://github.com/apache/predictionio.git







Installing Apache PredictionIO® from Source Code
===============================================
http://predictionio.apache.org/install/install-sourcecode/


















