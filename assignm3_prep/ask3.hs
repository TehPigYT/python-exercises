-- recursive
countEven :: [Int] -> Int
countEven [] = 0
countEven (x:xs) =
  if even x
    then 1 + countEven xs
    else countEven xs

-- comprehension
countEven2 :: [Int] -> Int
countEven2 list = length [x | x <- list, even x]
