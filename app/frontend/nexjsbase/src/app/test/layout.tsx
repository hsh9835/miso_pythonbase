import { ReactDOM } from "react";

export default function TestLayout({ children }): ReactDOM {
  return (
    <>
      <div className={"w2/3 h50px bg-white"}>{children}</div>
    </>
  );
}
