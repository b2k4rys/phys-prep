import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Main() {
  const [physSet, setSet] = useState("161");
  const [problemSetNum, setNum] = useState(1);

  const navigate = useNavigate();

  function handleChange(e) {
    setNum(e.target.value);
  }

  function handleSubmit() {
    if (physSet && problemSetNum) {
      navigate(`problems/${physSet}/${problemSetNum}`);
    }
  }
  return (
    <div>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Select the set</label>
          <select value={physSet} onChange={(e) => setSet(e.target.value)}>
            <option value="161">PHYS 161</option>
            <option value="162">PHYS 162</option>
          </select>
        </div>
        {physSet === null ? (
          <></>
        ) : (
          <>
            <label>Select the problem set number</label>
            <select value={problemSetNum} onChange={handleChange}>
              <option value="1">1</option>
              <option value="2">2</option>
              <option value="3">3</option>
              <option value="4">4</option>
            </select>
          </>
        )}
        <input type="submit" />
      </form>
    </div>
  );
}
