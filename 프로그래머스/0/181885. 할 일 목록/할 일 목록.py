def solution(todo_list, finished):
    answer = []
    for todo, boolen in zip(todo_list, finished):
        if not boolen:
            answer.append(todo)
    return answer