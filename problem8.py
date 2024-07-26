"""
Our football team has finished the championship. Our team's match results are recorded
 in a collection of strings. Each match is represented by a string in the format x:y, 
 where x is our team and y is our opponents score. The rules to calculate score is 
If x > y: 3 points
If x < y: 0 point
If x = y: 1 point
We need to write a function that takes this collection and returns the number 
of points our team (x) got in the championship by the rules given above.
"""
def calculate_points(results):
    
    points = [(3*(int(x)>int(y)) + 1 * (int(x)==int(y))) for result in results for x,y in[result.split(":")]]
    return sum(points)

match_points = ["3:1","1:1","0:2","4:2"]
total_points = calculate_points(match_points)
print(total_points)