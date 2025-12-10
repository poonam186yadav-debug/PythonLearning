marks={
    "math":10,
    "science":15,
    "english":12,
    "history":16,
    "computer":20,
}

print(marks["computer"],type(marks))
print(marks.keys())
print(marks.values())
print(marks.items())
marks.update({"math":18,"hindi":14})
print(marks)
