import { renderHook, act } from "@testing-library/react";
import { describe, it, expect } from "vitest";
import useCounter from "../src/hooks/useCounter";

describe("useCounter", () => {
  it("should increment, decrement and reset", () => {
    const { result } = renderHook(() => useCounter(0, 2));

    act(() => result.current.inc());
    expect(result.current.count).toBe(2);

    act(() => result.current.dec());
    expect(result.current.count).toBe(0);

    act(() => result.current.inc());
    act(() => result.current.reset());
    expect(result.current.count).toBe(0);
  });
});
