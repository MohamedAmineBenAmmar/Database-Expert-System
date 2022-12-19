import React from "react";
import { Chip } from "primereact/chip";
import { Message } from "primereact/message";
import capitalize from "../../utils/capitalize";

export default function Suggestions({ suggestions }) {
  const displaySuggestions = suggestions.map((suggestion) => (
    <li className="flex align-items-center py-3 px-2 border-top-1 border-300 flex-wrap">
      <div className="text-500 w-6 md:w-2 font-medium">
        {capitalize(suggestion.characteristics)}
      </div>
      <div className="text-900 w-full md:w-5 md:flex-order-0 flex-order-1">
        {suggestion.recommendations.map((recommendation) => (
          <Chip label={recommendation} className="mr-2" />
        ))}
      </div>
      <div className="md:w-5 flex justify-content-end">
        {suggestion.requirements.map((requirement) => (
          <>
            <p className="w-full">{requirement}</p>
            <br />
          </>
        ))}
      </div>
    </li>
  ));

  return (
    <div className="surface-0 p-4">
      <div className="font-medium text-3xl text-900 mb-3">
        Suggested databases for your project
      </div>
      <div className="text-500 mb-5">
        Our system may suggest multiple databases. The system will propose
        databases that suits your needs. In a case of a complex project a mix
        between databases in a distibuted environment is a must.
      </div>
      {suggestions.length === 0 ? (
        <Message className="w-full" severity="warn" text="There is no recommendations based on the constraints specified earlier" />
      ) : (
        <ul className="list-none p-0 m-0">       
        {displaySuggestions}
      </ul>
      )}
      
    </div>
  );
}
