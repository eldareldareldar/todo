import customtkinter as ctk
import psycopg2
from tkinter import *

ctk.set_appearance_mode("dark")

# Подключаемся к базе данных PostgreSQL
# db_params = {
#     'dbname': 'your_db_name',
#     'user': 'your_db_user',
#     'password': 'your_db_password',
#     'host': 'your_db_host'
# }

# Создаем подключение к базе данных
# conn = psycopg2.connect(**db_params)
# cursor = conn.cursor()

# Создаем таблицу для хранения задач, если она не существует
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS tasks (
#         id SERIAL PRIMARY KEY,
#         task_text TEXT
#     )
# ''')
# conn.commit()

app = ctk.CTk()
app.title('ToDo List')
app.geometry("750x450")


#Создаем таск
def add_task():
    task = task_entry.get()
    if task:
        tasks_list.insert(0, task)
        task_entry.delete(0, END)
        save_task_to_db(task)
    else:
        pass   


#Удаляем таск
def remove_task():
    selected = tasks_list.curselection()
    if selected:
        selected_task = tasks_list.get(selected[0])
        tasks_list.delete(selected[0])
        delete_task_from_db(selected_task)
    else:
        pass 


#Сохраняем, удаляем и загружаем таски в БД
# def save_task_to_db(task):
#     cursor.execute("INSERT INTO tasks (task_text) VALUES (%s)", (task,))
#     conn.commit()

# def delete_task_from_db(task):
#     cursor.execute("DELETE FROM tasks WHERE task_text = %s", (task,))
#     conn.commit()

# def load_tasks_from_db():
#     cursor.execute("SELECT task_text FROM tasks")
#     tasks = cursor.fetchall()
#     for task in tasks:
#         tasks_list.insert(END, task[0])


#Озаглавливаем
title_label = ctk.CTkLabel(app, text="Daily Tasks", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(40, 20))


#Создаем окна ввода и вывода
scrollable_frame = ctk.CTkScrollableFrame(app, width=500, height=200)
scrollable_frame.pack()

task_entry = ctk.CTkEntry(scrollable_frame)
task_entry.pack(fill="x")

tasks_list = Listbox(app, width=49, height=8, font=ctk.CTkFont)
tasks_list.place(x=123, y=135)


#Создаем кнопки
add_button = ctk.CTkButton(app, text="Add", width=500, command=add_task)
add_button.pack(pady=20)

delete_button = ctk.CTkButton(app, text="Delete", width=500, command=remove_task)
delete_button.pack(pady=20)


# load_tasks_from_db()  # Загружаем задачи из базы данных при запуске приложения

app.mainloop()

# Закрываем подключение к базе данных при выходе из приложения
# conn.close()


