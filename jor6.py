import sys

if len(sys.argv) > 1:
    script_name = sys.argv[0]
    scores = list(map(float, sys.argv[1:]))
    print("User provided scores:")
else:
    script_name = sys.argv[0]
    scores = [50, 60, 70, 80, 90]
    print("No input given - using default scores:")

total = sum(scores)
average = total / len(scores)

print("Script Name:", script_name)
print("Scores:", scores)
print("Sum of Scores:", total)
print("Average Score:", average)
