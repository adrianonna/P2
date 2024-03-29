import { fibonacci } from './fibonacci-array.js'

describe('Fibonacci series', () => {

  test('making the first 0 numbers', () => {
    expect(fibonacci(0)).toEqual([])
  })

  test('making the first 1 numbers', () => {
    expect(fibonacci(1)).toEqual([0])
  })

  test('making the first 2 numbers', () => {
    expect(fibonacci(2)).toEqual([0, 1])
  })

  test('making the first 4 numbers', () => {
    expect(fibonacci(4)).toEqual([0, 1, 1, 2])
  })

  test('making the first 6 numbers', () => {
    expect(fibonacci(6)).toEqual([0, 1, 1, 2, 3, 5])
  })

})
