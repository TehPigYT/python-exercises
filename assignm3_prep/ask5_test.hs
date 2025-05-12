import Ask5
import Test.HUnit

tests :: Test
tests = TestList
  [ "distance" ~: abs (distance (3,4) (7,8.1) - 5.728) < 1e-3 ~?= True
  ]

main :: IO()
main = do
  _ <- runTestTT tests
  return ()
