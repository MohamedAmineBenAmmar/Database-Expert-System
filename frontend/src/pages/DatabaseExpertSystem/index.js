import React, { useState } from "react";
import { getSuggestions } from "../../services";
import { TabView, TabPanel } from "primereact/tabview";

import Suggestions from "./Suggestions";
import Constraints from "./Constraints";

export default function DatabaseExpertSystem() {
  const [constraints, setConstraints] = useState({
    HighAvailability: false,
    StrongConsistency: false,
    HighPerformance: false,
    ComplexQuerying: false,
    Transactions: false,
    HorizontalScaling: false,
    MultiRegionDeployment: false,
    GraphDataModeling: false,
    GeospatialData: false,
    LargeAmountOfData: false,
    HighVolumeOfReadsAndWrites: false,
    StrictSecurityRequirements: false,
    StrictComplianceRequirements: false,
    MachineLearning: false,
    StreamProcessing: false,
    SearchCapabilities: false,
    FullTextSearch: false,
    RealTimeAnalytics: false,
    InMemoryProcessing: false,
    DocumentDataModeling: false,
  });

  const [activeIndex, setActiveIndex] = useState(0);

  const [suggestions, setSuggestions] = useState(null);

  const handleSuggestions = async (e) => {
    e.preventDefault();
    console.log("request body");
    console.log(constraints);

    try {
      let response = await getSuggestions(constraints);
      console.log("the server reponse");
      console.log(response);
      setSuggestions(response);
      setActiveIndex(1)
    } catch (error) {
      console.error(error);
    }
  };

  const handleTabChange = (e) => {
    if (e.index === 0) {
      setConstraints({
        HighAvailability: false,
        StrongConsistency: false,
        HighPerformance: false,
        ComplexQuerying: false,
        Transactions: false,
        HorizontalScaling: false,
        MultiRegionDeployment: false,
        GraphDataModeling: false,
        GeospatialData: false,
        LargeAmountOfData: false,
        HighVolumeOfReadsAndWrites: false,
        StrictSecurityRequirements: false,
        StrictComplianceRequirements: false,
        MachineLearning: false,
        StreamProcessing: false,
        SearchCapabilities: false,
        FullTextSearch: false,
        RealTimeAnalytics: false,
        InMemoryProcessing: false,
        DocumentDataModeling: false,
      });

      setSuggestions(null)      
    }
    setActiveIndex(e.index);
  };

  const projectConstraintsTabHeader = (options) => {
    return (
      <button
        type="button"
        onClick={options.onClick}
        className={options.className}
      >
        <i className="pi pi-cog mr-2" />
        {options.titleElement}
      </button>
    );
  };

  const suggestionsTabHeader = (options) => {
    return (
      <button
        type="button"
        onClick={options.onClick}
        className={options.className}
      >
        <i className="pi pi-sitemap mr-2" />
        {options.titleElement}
      </button>
    );
  };

  return (
    <div className="card">
      <TabView activeIndex={activeIndex} onTabChange={handleTabChange}>
        <TabPanel
          header="Project Constraints"
          headerTemplate={projectConstraintsTabHeader}
        >
          <Constraints />
        </TabPanel>
        <TabPanel
          header="Suggestions"
          headerTemplate={suggestionsTabHeader}
          headerClassName="ml-1 "
          // disabled={suggestions === null && true}
        >
          <Suggestions />
        </TabPanel>
      </TabView>
    </div>
  );
}
