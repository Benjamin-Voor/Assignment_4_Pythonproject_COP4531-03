# If the language is not specified to be pseudocode, might I give Python a try?
def main():
    deadline: int = 0
    profit: int = 1
    k: int = 0
    table = [[2,30],[1,35],[2,25],[1,40]] # 2D array
    for count_job, job in enumerate(table):
        if k < job[deadline]:
            k = job[deadline]
    answer = [0 for i in range(k)]
    
    for count_job, job in enumerate(table):
        if answer[job[deadline]-1] < job[profit]:
            answer[job[deadline]-1] = job[profit]
    return answer

if __name__ == '__main__':
    print(main())
    print(sum(main()))