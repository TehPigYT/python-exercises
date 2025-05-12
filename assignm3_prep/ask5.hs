module Ask5 where

distance :: (Double, Double) -> (Double, Double) -> Double
distance (x, y) (w, z) = sqrt ((w-x)^2+(z-y)^2)
