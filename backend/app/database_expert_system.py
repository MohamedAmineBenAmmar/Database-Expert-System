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
        self.suggestions = []


    @Rule(AND(HighAvailability(), StrongConsistency()))  # This is the LHS
    def distributed_database(self):
        print("Recommend a distributed database such as Apache Cassandra or Google Cloud Bigtable")
        self.suggestions.append({
            "recommendations": ["Apache Cassandra", " Google Cloud Bigtable"],
            "characteristics": "distributed database",
            "requirements": ["High availability", "Strong consistency"]
        })

    @Rule(AND(ComplexQuerying(), Transactions()))  # This is the LHS
    def relational_database(self):
        print("Recommend a relational database such as MySQL or PostgreSQL")
        self.suggestions.append({
            "recommendations": ["MySQL", " PostgreSQL"],
            "characteristics": "relational database",
            "requirements": ["Complex querying", "Transactions"]
        })

    @Rule(GraphDataModeling())  # This is the LHS
    def graph_database(self):
        print("Recommend a graph database such as Neo4j or Amazon Neptune")
        self.suggestions.append({
            "recommendations": ["Neo4j", "Amazon Neptune"],
            "characteristics": "graph database",
            "requirements": ["Graph data modeling"]
        })

    @Rule(GeospatialData())  # This is the LHS
    def geospatial_database(self):
        print("Recommend a database with geospatial indexing capabilities such as MongoDB or PostGIS")
        self.suggestions.append({
            "recommendations": ["MongoDB", "PostGIS"],
            "characteristics": "geospatial database",
            "requirements": ["Geospatial indexing capabilities"]
        })

    @Rule(AND(LargeAmountOfData(), HighVolumeOfReadsAndWrites()))  # This is the LHS
    def large_data_volume_database(self):
        print("Recommend a distributed database such as Cassandra or DynamoDB")
        self.suggestions.append({
            "recommendations": ["Cassandra", "DynamoDB"],
            "characteristics": "distributed database",
            "requirements": ["Large amount of data", "High volume of reads and writes"]
        })

    @Rule(StrictSecurityRequirements())  # This is the LHS
    def secure_database(self):
        print("Recommend a database with robust security features such as Oracle or Microsoft SQL Server")
        self.suggestions.append({
            "recommendations": ["Oracle", "Microsoft SQL Server"],
            "characteristics": "secure database",
            "requirements": ["Robust security", "Strict requirements"]
        })

    @Rule(StrictComplianceRequirements())  # This is the LHS
    def compliant_database(self):
        print("Recommend a database with strong compliance capabilities such as IBM Db2 or SAP HANA")
        self.suggestions.append({
            "recommendations": ["IBM Db2", "SAP HANA"],
            "characteristics": "compliant database",
            "requirements": ["Strong compliance capabilities"]
        })

    @Rule(MachineLearning())  # This is the LHS
    def machine_learning_database(self):
        print("Recommend a database with machine learning capabilities such as Google Cloud BigQuery or Amazon SageMaker")
        self.suggestions.append({
            "recommendations": ["Google Cloud BigQuery", "Amazon SageMaker"],
            "characteristics": "machine learning database",
            "requirements": ["Machine learning capabilities"]
        })

    @Rule(StreamProcessing())  # This is the LHS
    def stream_processing_database(self):
        print("Recommend a database with stream processing capabilities such as Apache Kafka or Amazon Kinesis")
        self.suggestions.append({
            "recommendations": ["Apache Kafka", "Amazon Kinesis"],
            "characteristics": "stream processing database",
            "requirements": ["Stream processing capabilities"]
        })

    @Rule(SearchCapabilities())  # This is the LHS
    def search_database(self):
        print("Recommend a database with search indexing capabilities such as Elasticsearch or Solr")
        self.suggestions.append({
            "recommendations": ["Elasticsearch", "Solr"],
            "characteristics": "search database",
            "requirements": ["Search capabilities", "Indexing capabilities"]
        })


    @Rule(FullTextSearch())  # This is the LHS
    def full_text_search_database(self):
        print("Recommend a database with full-text search capabilities such as Elasticsearch or Solr")
        self.suggestions.append({
            "recommendations": ["Elasticsearch", "Solr"],
            "characteristics": "full text search database",
            "requirements": ["Full-text search capabilities"]
        })

    @Rule(RealTimeAnalytics())  # This is the LHS
    def real_time_analytics_database(self):
        print("Recommend a database with real-time analytics capabilities such as Google Cloud BigQuery or Amazon Redshift")
        self.suggestions.append({
            "recommendations": ["Google Cloud BigQuery", "Amazon Redshift"],
            "characteristics": "real rime analytics",
            "requirements": ["Real-time analytics capabilities"]
        })

    @Rule(InMemoryProcessing())  # This is the LHS
    def in_memory_database(self):
        print("Recommend a database with in-memory capabilities such as Redis or Memcached")
        self.suggestions.append({
            "recommendations": ["Redis", "Memcached"],
            "characteristics": "in memory database",
            "requirements": ["In-memory capabilities"]
        })

    @Rule(DocumentDataModeling())  # This is the LHS
    def document_database(self):
        print("Recommend a document database such as MongoDB or Couchbase")
        self.suggestions.append({
            "recommendations": ["MongoDB", "Couchbase"],
            "characteristics": "document database",
            "requirements": ["Document data modeling"]
        })


# Create an instance of the ExpertSystem class
# db_expert_sys = DatabaseExpertSystem()

# Reset the system to clear any previous state
# db_expert_sys.reset()

# Ask the user the questions and gather the information
# for db_fact in db_facts:
#     answer = input(f"Does the project require {db_fact}? [y/n]")
#     if answer == 'y':
#         db_expert_sys.declare(db_facts[db_fact]())

# Run the expert system and make a recommendation
# db_expert_sys.run()


    

    

    
        
    


    

    

    

    

    

    