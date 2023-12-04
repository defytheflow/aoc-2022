import fs from "node:fs";

type Input = unknown;

main();

function main() {
  const input = parseInput("input.txt");

  const resultOne = solveOne(input);
  console.log(resultOne);
  console.assert(resultOne == Infinity);

  const resultTwo = solveTwo(input);
  console.log(resultTwo);
  console.assert(resultTwo == Infinity);
}

function solveOne(input: Input): unknown {}

function solveTwo(input: Input): unknown {}

function parseInput(filename: string): Input {
  return fs.readFileSync(filename).toString().trimEnd();
}
