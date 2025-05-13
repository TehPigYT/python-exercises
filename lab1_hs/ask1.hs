import System.IO

main :: IO()
main = do
  putStr "Length side base in m: "
  hFlush stdout
  input1 <- getLine
  putStr "Height of pyramid in m: "
  hFlush stdout
  input2 <- getLine
  let nb = read input1 :: Double
      nh = read input2 :: Double
      bricks = volumeSquarePyramid nb nh / volumeBox 0.19 0.09 0.06
  putStrLn ("Number of stone bricks = " ++ show bricks)

volumeBox :: (Num a) => a -> a -> a -> a
volumeBox w h d = w * h * d

volumeSquarePyramid :: (Fractional a) => a -> a -> a
volumeSquarePyramid b h = b * b * h / 3
