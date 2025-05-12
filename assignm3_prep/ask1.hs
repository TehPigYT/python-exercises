addFactorial :: Int -> Int
addFactorial n
  | odd n = product [x | x <- [1,3..n]]
  | otherwise = -1
  -- if odd n
    -- then product [1,3..n]
    -- else -1
