import LoginPanel from "./components/Login/Login";
import Register from "./components/Register/Register"; // Import the Register component
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      <Route path="/register" element={<Register />} /> {'https://alexandru007-8000.theianext-0-labs-prod-misc-tools-us-east-0.proxy.cognitiveclass.ai/register/'}
    </Routes>
  );
}

export default App;