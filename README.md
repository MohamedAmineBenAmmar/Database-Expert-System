<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a>
    <img src="" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Expert.ai</h3>

  <p align="center">
    A Databases Suggestion System to recommand a database that fit with you !
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</div>
 <div align=”justify”>
  <p>
First, let's start by defining the 20 facts that we will use in the expert system. These facts will be used to gather information about the user's project and needs. 
Here are some examples of facts that could be relevant to consider when choosing a database: </p></div>
<hr>
<div align=”justify”>
<ol>
<li>
Does the project require high availability?</li>
<li>
Does the project require strong consistency?</li>
  <li>
Does the project require high performance?</li>
  <li>
Does the project require complex querying capabilities?</li>
  <li>
Does the project require support for transactions?</li>
  <li>
Does the project require support for horizontal scaling?</li>
  <li>
Does the project require support for multi-region deployment?</li>
  <li>
Does the project require support for graph data modeling?</li>
  <li>
Does the project require support for geospatial data?</li>
  <li>
Does the project have a large amount of data?</li>
  <li>
Does the project have a high volume of reads and writes?</li>
  <li>
Does the project have strict security requirements?</li>
  <li>
Does the project have strict compliance requirements?</li>
  <li>
Does the project require support for machine learning?</li>
  <li>
Does the project require support for stream processing?</li>
  <li>
Does the project require support for search capabilities?</li>
  <li>
Does the project require support for full-text search?</li>
  <li>
Does the project require support for real-time analytics?</li>
  <li>
Does the project require support for in-memory processing?</li>
  <li>
Does the project require support for document data modeling?</li>
</div>
  <hr>
<div>  
<p> Next, let's define the 20 rules that will be used to evaluate the facts and make a recommendation for the user. 
These rules should be based on the characteristics and capabilities of different databases, and should consider the facts gathered from the user's answers. 
Here are some examples of rules that could be used:
</p>
</div>
  <hr>
<div align=”justify”>
<ol>
  <li>
If the project requires high availability and strong consistency, recommend a distributed database such as Apache Cassandra or Google Cloud Bigtable.</li>
<li>
If the project requires high performance and support for horizontal scaling, recommend a distributed database such as MongoDB or Cassandra.</li>
<li>
If the project requires complex querying capabilities and support for transactions, recommend a relational database such as MySQL or PostgreSQL.</li>
<li>
If the project requires support for graph data modeling, recommend a graph database such as Neo4j or Amazon Neptune.</li>
<li>
If the project requires support for geospatial data, recommend a database with geospatial indexing capabilities such as MongoDB or PostGIS.</li>
<li>
If the project has a large amount of data and a high volume of reads and writes, recommend a distributed database such as Cassandra or DynamoDB.</li>
<li>
If the project has strict security requirements, recommend a database with robust security features such as Oracle or Microsoft SQL Server.</li>
<li>
If the project has strict compliance requirements, recommend a database with strong compliance capabilities such as IBM Db2 or SAP HANA.</li>
<li>
If the project requires support for machine learning, recommend a database with machine learning capabilities such as Google Cloud BigQuery or Amazon SageMaker.</li>
<li>
If the project requires support for stream processing, recommend a database with stream processing capabilities such as Apache Kafka or Amazon Kinesis.</li>
<li>
If the project requires support for search capabilities, recommend a database with search indexing capabilities such as Elasticsearch or Solr.</li>
<li>
If the project requires support for full-text search, recommend a database with full-text search capabilities such as Elasticsearch or Solr.</li>
<li>
If the project requires support for real-time analytics, recommend a database with real-time analytics capabilities such as Google Cloud BigQuery or Amazon Redshift.</li>
<li>
 If the project requires support for in-memory processing,</li>
<li>
If the project requires support for in-memory processing, recommend a database with in-memory capabilities such as Redis or Memcached.</li>
<li>
If the project requires support for document data modeling, recommend a document database such as MongoDB or Couchbase.</li>
<li>
If the project requires support for multi-region deployment, recommend a database with global distribution capabilities such as Cosmos DB or Cassandra.</li>
<li>
If the project requires strong consistency and support for transactions, recommend a database with ACID transactions such as MySQL or PostgreSQL.</li>
</li>
If the project requires support for horizontal scaling and high performance, recommend a database with a distributed architecture such as Cassandra or MongoDB.</li>
<li>
If the project requires support for geospatial data and complex querying capabilities, recommend a database with geospatial indexing and query support such as PostGIS or MongoDB.</li>
</ol>
</div>
<hr>
### Install dependencies
<hr>
<div>
Now that we have defined the facts and rules for our expert system, let's implement it using the experta library in Python.
First, we will need to install the experta library. 
You can do this by running the following command:
 <br>
  <br>
</div>

<!-- GETTING STARTED -->

```console
pip install experta
```

<hr>

Check the `database_expert.py` for the implementation
