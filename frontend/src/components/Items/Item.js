import React, { useState } from "react";

export default function Item({ problem, answer, number, solve_url }) {
  const [value, setValue] = useState("");
  const [isCorrect, setCorrect] = useState(null);

  console.log(solve_url);
  function handleSubmit(e) {
    e.preventDefault();
    const numericValue = parseFloat(value);
    console.log(answer);
    if (!isNaN(numericValue)) {
      if (
        +value > +answer - 0.01 * answer &&
        +value < +answer + 0.01 * answer
      ) {
        console.log("correct");
        setCorrect(true);
      } else {
        console.log("wrong");
        setCorrect(false);
      }
    }
  }

  function handleChange(e) {
    setValue(e.target.value);
  }

  const borderColorAnswer =
    isCorrect === null ? "" : isCorrect ? "#2f9e44" : "#e03131";

  return (
    <form onSubmit={handleSubmit}>
      <li className="problems">
        <div class="problem--box">
          <div>
            <p>Question {number}</p>
          </div>
          <div>
            <p>
              {isCorrect === null ? "" : isCorrect === true ? "Right" : "Wrong"}
            </p>
          </div>
        </div>

        <div class="problem--problem">
          <p>{problem}</p>
          <div className="answer-box">
            <input
              type="text"
              value={value}
              onChange={handleChange}
              class="answer--box"
            />
            {isCorrect === null ? (
              <></>
            ) : isCorrect === true ? (
              <span style={{ color: "#367933" }}>&#10003;</span>
            ) : (
              <span style={{ color: "#CA311F" }}>&#10005;</span>
            )}
          </div>

          {isCorrect === null ? (
            <></>
          ) : (
            <img src={`${solve_url}`} alt={number} />
          )}
        </div>
      </li>
    </form>
  );
}
