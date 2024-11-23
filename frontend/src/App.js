import ItemsList from "./components/Items/ItemsList";
import { Routes, Route } from "react-router-dom";
import Main from "./components/Main/HomePage";

export default function App() {
  return (
    <>
      <Routes>
        <Route path="/problems" element={<ItemsList />} />
        <Route path="/" element={<Main />} />
      </Routes>
    </>
  );
}
