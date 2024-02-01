"use client";

import { ReactDOM, useState } from "react";
import axios from "axios";

export default function test(): ReactDOM {
  // eslint-disable-next-line react-hooks/rules-of-hooks
  const [ttt, setTtt] = useState("hello");

  return (
    <>
      <div>
        <p className={"text-black"}>{ttt}</p>
        <button
          className={
            "pointer-events-auto ml-8 rounded-md bg-indigo-600 px-3 py-2 text-[0.8125rem] font-semibold leading-5 text-white hover:bg-indigo-500"
          }
          onClick={async () => {
            const data = { name: "I'm SeHwa" };
            const res = await axios
              .post("http://127.0.0.1:8000/spacy/test", data, {
                headers: {
                  "Content-Type": "application/json",
                },
              })
              .catch((err) => {
                alert(err);
              }); // /spacy/test2 엔드포인트에서 데이터를 가져오기 위한 비동기 함수
            setTtt(res.data.message);
          }}
        >
          miso
        </button>
        <button
          className={
            "pointer-events-auto ml-8 rounded-md bg-indigo-600 px-3 py-2 text-[0.8125rem] font-semibold leading-5 text-white hover:bg-indigo-500"
          }
          onClick={async () => {
            const data = { name: "I'm SeHwa" };
            const res = await axios
              .post("http://127.0.0.1:8000/spacy/test2", data, {
                headers: {
                  "Content-Type": "application/json",
                },
              })
              .catch((err) => {
                alert(err);
              }); // /spacy/test2 엔드포인트에서 데이터를 가져오기 위한 비동기 함수
            setTtt(res.data);
          }}
        >
          글 호출
        </button>
      </div>
    </>
  );
}
