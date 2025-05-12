trapezoid :: Float -> Float -> Float -> Float
trapezoid b1 b2 h = ((b1 + b2) * h) / 2

trapezoidFixedBases :: Float -> Float
trapezoidFixedBases = trapezoid 10 5

main :: IO()
main = do
  print(trapezoid 20 15 7.5)
  print(trapezoidFixedBases 8.9)
