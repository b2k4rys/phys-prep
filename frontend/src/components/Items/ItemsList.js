import React, { useEffect, useState } from "react";
import axios from "axios";
import Item from "./Item";

export default function ItemsList() {
  const [items, setItems] = useState([]);
  const [rangeSubmit, setRangeSubmit] = useState(false);
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/posts/")
      .then((response) => {
        setItems(response.data);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  const answers = items.map((item) => ({
    number: item.number,
    answer: item.answer,
  }));

  const [range, setRange] = useState([0, 6]);
  function handleChangeRange(index, e) {
    if (+e.target.value >= 0 && +e.target.value <= 100) {
      const newRange = [...range];
      newRange[index] = +e.target.value;
      setRange(newRange);
    } else {
      setRange(range);
    }
  }

  function handleSubmitRange(e) {
    e.preventDefault();
    setRangeSubmit(true);
  }

  function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));

      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  }

  const newItems = shuffleArray(items.slice(range[0], range[1] + 1));
  console.log(newItems);

  return (
    <div>
      <form onSubmit={(e) => handleSubmitRange(e)} class="range--submit">
        <input
          type="text"
          value={range[0]}
          onChange={(e) => handleChangeRange(0, e)}
        />
        <input
          type="text"
          value={range[1]}
          onChange={(e) => handleChangeRange(1, e)}
        />
        <button type="submit">Submit</button>
      </form>
      {rangeSubmit === true ? (
        <ul>
          {newItems.map((item) => (
            <Item
              key={item.id}
              problem={item.body}
              answer={item.answer}
              number={item.number}
              answers={answers}
              solve_url={item.solve_url}
            />
          ))}
        </ul>
      ) : (
        <></>
      )}
    </div>
  );
}
