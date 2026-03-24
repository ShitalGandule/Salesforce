if __name__ == '__main__':
    # Initialize the nested list
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    # 1. Identify unique sorted scores to find the second lowest
    unique_scores = sorted(list(set([s[1] for s in students])))
    second_lowest = unique_scores[1]
    
    # 2. Filter students matching the second lowest score
    second_lowest_students = [s[0] for s in students if s[1] == second_lowest]
    
    # 3. Sort names alphabetically and print
    for name in sorted(second_lowest_students):
        print(name)
