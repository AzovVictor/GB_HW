seconds = int(input("Введите количество секунд:"))
hour = seconds // 3600
minutes = (seconds // 60) % 60
sec = seconds % 60
print(f"{hour}:{minutes}:{sec}")
