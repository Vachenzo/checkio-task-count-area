"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        { "input": [[0,0,0,0,1,0,1,0,0],
                    [0,1,0,0,1,0,1,0,0],
                    [0,0,0,1,0,0,1,0,0],
                    [0,0,1,1,1,1,1,1,1],
                    [1,1,1,0,1,1,0,1,0],
                    [0,0,1,0,1,1,0,1,0],
                    [0,0,1,0,0,0,0,1,0],
                    [1,0,0,1,1,1,1,1,0],
                    [0,0,0,0,0,0,0,1,0]],
          "answer": [4,5,6,8,12,13],
        { "input": [[1,0,0,0,1,0,0,0,0],
                    [0,1,0,0,1,0,0,0,0],
                    [0,0,1,0,1,1,1,1,1],
                    [0,0,0,1,0,0,0,0,0],
                    [0,0,0,0,1,0,0,0,0],
                    [0,1,0,0,0,1,0,0,0],
                    [0,0,1,0,0,0,1,0,0],
                    [0,1,0,1,0,0,0,1,0],
                    [1,0,0,0,0,0,0,0,1]],
          "answer": [6,8,15,31],
        { "input": [[0,0,0,0,1,0,0,0,0],
                    [0,1,1,0,1,0,0,0,0],
                    [0,1,1,0,1,0,0,0,0],
                    [0,1,1,0,1,0,0,0,0],
                    [0,1,1,0,1,0,0,0,0],
                    [0,1,1,0,1,1,1,1,0],
                    [0,1,0,0,0,0,0,1,0],
                    [0,1,1,1,1,1,1,1,0],
                    [0,0,0,0,0,0,0,0,0]],
          "answer": [53],
        { "input": [[0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,1,1,1,1,1,1,1,0],
                    [0,0,0,1,0,0,0,1,1],
                    [0,0,0,0,0,0,1,0,0],
                    [1,1,1,1,0,0,0,1,0],
                    [0,1,0,0,1,0,1,0,0],
                    [0,0,1,0,0,1,0,0,0],
                    [0,1,0,0,0,0,1,0,0]],
          "answer": [4,8,10,36],
    ]
}
