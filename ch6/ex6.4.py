from collections import deque
from random import randrange

graph = {}
graph['wake_up'] = ['make_morning_exercise', 'clean_teeth', 'pack_lunch']
graph['make_morning_exercise'] = ['take_shower']
graph['take_shower'] = ['dress_up']
graph['dress_up'] = []
graph['clean_teeth'] = ['have_a_breakfast']
graph['have_a_breakfast'] = []
graph['pack_lunch'] = []

def make_task_list(graph):
    queue = deque()
    queue += graph['wake_up']
    searched = []
    i = 0

    print(f"{i}. wake_up")

    while queue:
        print(">>> queue = ", queue)
        i += 1
        task = queue.popleft()
        print(f"{i}. {task}")

        if not task in searched:
            queue += graph[task]
            searched.append(task)


make_task_list(graph)