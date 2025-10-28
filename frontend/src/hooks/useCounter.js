import { useState } from "react";

export default function useCounter(initial = 0, step = 1) {
  const [count, setCount] = useState(initial);

  const inc = () => setCount((c) => c + step);
  const dec = () => setCount((c) => c - step);
  const reset = () => setCount(initial);

  return { count, inc, dec, reset };
}
