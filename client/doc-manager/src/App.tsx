import { BrowserRouter, Routes, Route } from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import MyFilesPage from "./pages/MyFilesPage"

function App() {
  return (
      <BrowserRouter>
          <Routes>
              <Route path="/" element={<LoginPage />} />
              <Route path="/files" element={<MyFilesPage />} />
          </Routes>
    </BrowserRouter>
  );
}

export default App;

