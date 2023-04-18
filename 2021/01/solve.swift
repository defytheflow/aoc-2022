import Foundation

let data = try String(contentsOfFile: "input.txt")

let result_one = solve_one(data: data)
print(result_one)
assert(result_one == 1288)

let result_two = solve_two(data: data)
print(result_two)
assert(result_two == 1311)

func solve_one(data: String) -> Int {
    solve(data: data, count: 1)
}

func solve_two(data: String) -> Int {
    solve(data: data, count: 3)
}

func solve(data: String, count: Int) -> Int {
    let measurements = parse_input(data: data)
    var increases = 0

    for i in count..<measurements.count {
        if measurements[i] > measurements[i - count] {
            increases += 1
        }
    }

    return increases
}

func parse_input(data: String) -> [Int] {
    data
        .split(separator: "\n")
        .map { Int($0)! }
}
