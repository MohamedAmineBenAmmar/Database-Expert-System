First, let's start by defining the 20 facts that we will use in the expert system. These facts will be used to gather information about the user's project and needs. 
Here are some examples of facts that could be relevant to consider when choosing a database:

1-  Does the project require high availability?
2-  Does the project require strong consistency?
3-  Does the project require high performance?
4-  Does the project require complex querying capabilities?
5-  Does the project require support for transactions?
6-  Does the project require support for horizontal scaling?
7-  Does the project require support for multi-region deployment?
8-  Does the project require support for graph data modeling?
9-  Does the project require support for geospatial data?
10- Does the project have a large amount of data?
11- Does the project have a high volume of reads and writes?
12- Does the project have strict security requirements?
13- Does the project have strict compliance requirements?
14- Does the project require support for machine learning?
15- Does the project require support for stream processing?
16- Does the project require support for search capabilities?
17- Does the project require support for full-text search?
18- Does the project require support for real-time analytics?
19- Does the project require support for in-memory processing?
20- Does the project require support for document data modeling?

Next, let's define the 20 rules that will be used to evaluate the facts and make a recommendation for the user. 
These rules should be based on the characteristics and capabilities of different databases, and should consider the facts gathered from the user's answers. 
Here are some examples of rules that could be used:

1-  If the project requires high availability and strong consistency, recommend a distributed database such as Apache Cassandra or Google Cloud Bigtable.
2-  If the project requires high performance and support for horizontal scaling, recommend a distributed database such as MongoDB or Cassandra.
3-  If the project requires complex querying capabilities and support for transactions, recommend a relational database such as MySQL or PostgreSQL.
4-  If the project requires support for graph data modeling, recommend a graph database such as Neo4j or Amazon Neptune.
5-  If the project requires support for geospatial data, recommend a database with geospatial indexing capabilities such as MongoDB or PostGIS.
6-  If the project has a large amount of data and a high volume of reads and writes, recommend a distributed database such as Cassandra or DynamoDB.
7-  If the project has strict security requirements, recommend a database with robust security features such as Oracle or Microsoft SQL Server.
8-  If the project has strict compliance requirements, recommend a database with strong compliance capabilities such as IBM Db2 or SAP HANA.
9-  If the project requires support for machine learning, recommend a database with machine learning capabilities such as Google Cloud BigQuery or Amazon SageMaker.
10- If the project requires support for stream processing, recommend a database with stream processing capabilities such as Apache Kafka or Amazon Kinesis.
11- If the project requires support for search capabilities, recommend a database with search indexing capabilities such as Elasticsearch or Solr.
12- If the project requires support for full-text search, recommend a database with full-text search capabilities such as Elasticsearch or Solr.
13- If the project requires support for real-time analytics, recommend a database with real-time analytics capabilities such as Google Cloud BigQuery or Amazon Redshift.
14- If the project requires support for in-memory processing,
15- If the project requires support for in-memory processing, recommend a database with in-memory capabilities such as Redis or Memcached.
16- If the project requires support for document data modeling, recommend a document database such as MongoDB or Couchbase.
17- If the project requires support for multi-region deployment, recommend a database with global distribution capabilities such as Cosmos DB or Cassandra.
18- If the project requires strong consistency and support for transactions, recommend a database with ACID transactions such as MySQL or PostgreSQL.
19- If the project requires support for horizontal scaling and high performance, recommend a database with a distributed architecture such as Cassandra or MongoDB.
20- If the project requires support for geospatial data and complex querying capabilities, recommend a database with geospatial indexing and query support such as PostGIS or MongoDB.

Now that we have defined the facts and rules for our expert system, let's implement it using the experta library in Python.
First, we will need to install the experta library. You can do this by running the following command:
pip install experta

Check the database_expert.py for the implementation