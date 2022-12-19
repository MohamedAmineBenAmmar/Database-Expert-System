import React from "react";
import { Button } from "primereact/button";
import { Checkbox } from "primereact/checkbox";

export default function Constraints({
  handleSuggestions,
  handleConstraints,
  constraints,
}) {
  const facts = {
    HighAvailability: "Does the project require high availability?",
    StrongConsistency: "Does the project require strong consistency?",
    HighPerformance: "Does the project require high performance?",
    ComplexQuerying: "Does the project require complex querying capabilities?",
    Transactions: "Does the project require support for transactions?",
    HorizontalScaling:
      "Does the project require support for horizontal scaling?",
    MultiRegionDeployment:
      "Does the project require support for multi-region deployment?",
    GraphDataModeling:
      "Does the project require support for graph data modeling?",
    GeospatialData: "Does the project require support for geospatial data?",
    LargeAmountOfData: "Does the project have a large amount of data?",
    HighVolumeOfReadsAndWrites:
      "Does the project have a high volume of reads and writes?",
    StrictSecurityRequirements:
      "Does the project have strict security requirements?",
    StrictComplianceRequirements:
      "Does the project have strict compliance requirements?",
    MachineLearning: "Does the project require support for machine learning?",
    StreamProcessing: "Does the project require support for stream processing?",
    SearchCapabilities:
      "Does the project require support for search capabilities?",
    FullTextSearch: "Does the project require support for full-text search?",
    RealTimeAnalytics:
      "Does the project require support for real-time analytics?",
    InMemoryProcessing:
      "Does the project require support for in-memory processing?",
    DocumentDataModeling:
      "Does the project require support for document data modeling?",
  };

  const questions = Object.keys(facts).map((fact, index) => (
    <div className="field-checkbox">
      <Checkbox
        inputId={fact}
        id={fact}
        name={fact}
        value={constraints[fact]}
        onChange={handleConstraints}
        checked={constraints[fact]}
      />
      <label htmlFor="city1" className="block text-900 font-medium ">
        {facts[fact]}
      </label>
    </div>
  ));
  return (
    <div className="flex align-items-center justify-content-center p-4">
      <div className="surface-card p-4 shadow-8 border-round w-full lg:w-6">
        <div className="text-center mb-5">
          <img
            src="assets/images/hyper.svg"
            alt="hyper"
            height={50}
            className="mb-3"
          />
          <div className="text-900 text-3xl font-medium mb-3">
            Set the requirements of your project
          </div>
          <span className="text-600 font-medium line-height-3">
            By clicking on run engine our system will provide you with the best
            databases to use that suits your project
          </span>
        </div>

        <form onSubmit={handleSuggestions}>
          {questions}
          <Button label="Run Engine" icon="pi pi-sync" className="w-full" />
        </form>
      </div>
    </div>
  );
}
