#A number of points along the highway are in need of repair. An equal number of crews are available, stationed at various points along the highway. They must move along the highway to reach an assigned point. Given that one crew must be assigned to each job, what is the minimum total amount of distance traveled by all crews before they can begin work?
#For example, given crews at points {1,3,5} and required repairs at {3,5,7), one possible minimum assignment would be {1→3, 35, 57} for a total of 6 units traveled.
#Function Description
#Complete the function getMinCost in the editor below. The function should return the minimum possible total distance traveled as an integer.
#getMinCost has the following parameter(s): crewld[crewld[0],...crewld[n-1]]: a vector of integers jobld[jobld[0],...jobld[n-1]]: a vector of integers
#Constraints
#1≤n≤105
#• crewld[i]: 1≤ crewld[i] ≤ 10°
#• jobld[i]: 1≤jobld[i] ≤ 109

#▼ Input Format For Custom Testing
#The first line contains an integer, n, denoting the number of elements in crew_id and job_id.
#Each line i of the n subsequent lines (where 0≤i<n) contains an integer describing crew_id[i].
#The next line again contains the integer n as above.
#Each line i of the n subsequent lines (where 0<i<n) contains an integer describing job_id[i].
#Sample Case 0
#Sample Input For Custom Testing
#5
#5
#3
#1
#4
#6
#5
#9
#8
#3
#15
#1
#Sample Output
#17
#Explanation
#By index, crewld[i]→ jobld[i], {(0-0), (12), (24), (33), (4-1)} is one possible assignment for a minimum cost of 17. Showing element values, this is { (5 →9), (33), (11), (415), (68) } yielding a total travel distance of 4+0+0+11+2=17.
#To solve this problem, we need to find the minimum total distance traveled by all crews before they can begin work. One approach is to pair each crew with a job such that the distance traveled is minimized. We can achieve this by finding the nearest job for each crew and calculating the total distance. */



#Solution

import os


def getMinCost(crew_id, job_id):
    crew_id.sort()
    job_id.sort()
    min_total_distance = 0
    i, j = 0, 0
    while i < len(crew_id) and j < len(job_id):
        min_total_distance += abs(crew_id[i] - job_id[j])
        i += 1
        j += 1
    return min_total_distance


if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        print("Error: OUTPUT_PATH environment variable is not set.")
    else:
        try:
            crew_id_count = int(raw_input().strip())
            crew_id = [int(raw_input().strip()) for _ in range(crew_id_count)]

            job_id_count = int(raw_input().strip())
            job_id = [int(raw_input().strip()) for _ in range(job_id_count)]

            result = getMinCost(crew_id, job_id)

            fptr.write(str(result) + '\n')
        except ValueError:
            print("Error: Invalid input format.")
        finally:
            fptr.close()