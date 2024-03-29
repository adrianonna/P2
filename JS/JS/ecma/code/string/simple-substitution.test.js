import { substitution } from './simple-substitution.js'

describe('Basic Leet', () => {

  test('converting message to "lorem ipsum"', () => {
    // https://simple.wikipedia.org/wiki/Leet
    // http://www.robertecker.com/hp/research/leet-converter.php?lang=en
    expect(substitution('lorem ipsum', 'aegiost', '4361057')).toBe('l0r3m 1p5um')
  })
})


describe.skip('Simple Substitution', () => {
  test('converting to basic leet', () => {
    expect(substitution('lorem ipsum', 'aegiost', '4361057')).toBe('l0r3m 1p5um')
  })

  test('converting to custom leet', () => {
    expect(substitution('senha secreta', 'aegiost', '!@#$%&*')).toBe('&@nh! &@cr@*!')
  })
})

