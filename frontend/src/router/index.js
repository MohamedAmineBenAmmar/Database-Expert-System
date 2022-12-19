import { Routes, Route } from "react-router-dom";

import AppLayout from "../layout";
import Landing from "../pages/Landing";
import DatabaseExpertSystem from "../pages/DatabaseExpertSystem"

export default function RouterConfig() {
  return (
    <Routes>
      <Route path="/" element={<AppLayout />}>
        <Route index element={<Landing />} />
        <Route path="/suggest" element={<DatabaseExpertSystem />} />
      </Route>
    </Routes>
  );
}