from experta import *

# Define the facts
class HighAvailability(Fact):
    pass

class StrongConsistency(Fact):
    pass

class HighPerformance(Fact):
    pass

class ComplexQuerying(Fact):
    pass

class Transactions(Fact):
    pass

class HorizontalScaling(Fact):
    pass

class MultiRegionDeployment(Fact):
    pass

class GraphDataModeling(Fact):
    pass

class GeospatialData(Fact):
    pass

class LargeAmountOfData(Fact):
    pass

class HighVolumeOfReadsAndWrites(Fact):
    pass

class StrictSecurityRequirements(Fact):
    pass

class StrictComplianceRequirements(Fact):
    pass

class MachineLearning(Fact):
    pass

class StreamProcessing(Fact):
    pass

class SearchCapabilities(Fact):
    pass

class FullTextSearch(Fact):
    pass

class RealTimeAnalytics(Fact):
    pass

class InMemoryProcessing(Fact):
    pass

class DocumentDataModeling(Fact):
    pass

db_facts = {
    "HighAvailability": HighAvailability,
    "StrongConsistency": StrongConsistency,
    "HighPerformance": HighPerformance,
    "ComplexQuerying": ComplexQuerying,
    "Transactions": Transactions,
    "HorizontalScaling": HorizontalScaling,
    "MultiRegionDeployment": MultiRegionDeployment,
    "GraphDataModeling": GraphDataModeling,
    "GeospatialData": GeospatialData,
    "LargeAmountOfData": LargeAmountOfData,
    "HighVolumeOfReadsAndWrites": HighVolumeOfReadsAndWrites,
    "StrictSecurityRequirements": StrictSecurityRequirements,
    "StrictComplianceRequirements": StrictComplianceRequirements,
    "MachineLearning": MachineLearning,
    "StreamProcessing": StreamProcessing,
    "SearchCapabilities": SearchCapabilities,
    "FullTextSearch": FullTextSearch,
    "RealTimeAnalytics": RealTimeAnalytics,
    "InMemoryProcessing": InMemoryProcessing,
    "DocumentDataModeling": DocumentDataModeling,
}

# Define the rules
class DatabaseExpertSystem(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.suggestion = []


    @Rule(AND(HighAvailability(), StrongConsistency()))  # This is the LHS
    def distributed_database(self):
        print("Recommend a distributed database such as Apache Cassandra or Google Cloud Bigtable")

    @Rule(AND(ComplexQuerying(), Transactions()))  # This is the LHS
    def relational_database(self):
        print("Recommend a relational database such as MySQL or PostgreSQL")

    @Rule(GraphDataModeling())  # This is the LHS
    def graph_database(self):
        print("Recommend a graph database such as Neo4j or Amazon Neptune")

    @Rule(GeospatialData())  # This is the LHS
    def geospatial_database(self):
        print("Recommend a database with geospatial indexing capabilities such as MongoDB or PostGIS")

    @Rule(AND(LargeAmountOfData(), HighVolumeOfReadsAndWrites()))  # This is the LHS
    def large_data_volume_database(self):
        print("Recommend a distributed database such as Cassandra or DynamoDB")

    @Rule(StrictSecurityRequirements())  # This is the LHS
    def secure_database(self):
        print("Recommend a database with robust security features such as Oracle or Microsoft SQL Server")

    @Rule(StrictComplianceRequirements())  # This is the LHS
    def compliant_database(self):
        print("Recommend a database with strong compliance capabilities such as IBM Db2 or SAP HANA")

    @Rule(MachineLearning())  # This is the LHS
    def machine_learning_database(self):
        print("Recommend a database with machine learning capabilities such as Google Cloud BigQuery or Amazon SageMaker")

    @Rule(StreamProcessing())  # This is the LHS
    def stream_processing_database(self):
        print("Recommend a database with stream processing capabilities such as Apache Kafka or Amazon Kinesis")

    @Rule(SearchCapabilities())  # This is the LHS
    def search_database(self):
        print("Recommend a database with search indexing capabilities such as Elasticsearch or Solr")

    @Rule(FullTextSearch())  # This is the LHS
    def full_text_search_database(self):
        print("Recommend a database with full-text search capabilities such as Elasticsearch or Solr")

    @Rule(RealTimeAnalytics())  # This is the LHS
    def real_time_analytics_database(self):
        print("Recommend a database with real-time analytics capabilities such as Google Cloud BigQuery or Amazon Redshift")

    @Rule(InMemoryProcessing())  # This is the LHS
    def in_memory_database(self):
        print("Recommend a database with in-memory capabilities such as Redis or Memcached")

    @Rule(DocumentDataModeling())  # This is the LHS
    def document_database(self):
        print("Recommend a document database such as MongoDB or Couchbase")


# Create an instance of the ExpertSystem class
db_expert_sys = DatabaseExpertSystem()

# Reset the system to clear any previous state
db_expert_sys.reset()

# Ask the user the questions and gather the information
for db_fact in db_facts:
    answer = input(f"Does the project require {db_fact}? [y/n]")
    if answer == 'y':
        db_expert_sys.declare(db_facts[db_fact]())

# Run the expert system and make a recommendation
db_expert_sys.run()


    

    

    
        
    


    

    

    

    

    

    