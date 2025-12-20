import tkinter as tk
import csv
from tkinter import filedialog,messagebox
import mysql.connector
conn=mysql.connector.connect(
    user='root',
    password='Deepu6421!@#',
    host='localhost',
    database='tkinter_db',
    autocommit=False
)
print(conn.is_connected())
cursor = conn.cursor()

def file_open():
    file=filedialog.askopenfilename(filetypes=[('csv file','*.csv')])

    with open(file,'r') as f:
        reader=csv.reader(f)
        print(next(reader))
        for row in reader:
            cursor.execute(
                '''INSERT INTO students(NAME,CLASS,GRADE)
                   VALUES (%s,%s,%s)
                ''',
                row
            )
        conn.commit()
        messagebox.showinfo('Info','data saved to db')



def fill_text_box():

    text_box.configure(state='normal')
    text_box.delete('1.0',tk.END)
    cursor.execute('select* from students')
    for row in cursor.fetchall():
    #    print(row)
       text_box.insert(tk.END,f'ID:{row[0]},Name:{row[1]},Class:{row[2]},Grade:{row[3]}\n')

    text_box.configure(state="disabled")
def add_record():
    name=name_entry.get()
    class_=class_entry.get()
    grade=Grade_entry.get()



    cursor.execute(
                '''INSERT INTO students(NAME,CLASS,GRADE)
                   VALUES (%s,%s,%s)
                ''',
                (name,class_,grade)
    )
    conn.commit()
    messagebox.showinfo('Info','record added')
    fill_text_box()
def Update_record():
    id = int(id_entry.get())
    name=name_entry.get()
    class_=class_entry.get()
    grade=Grade_entry.get()
    cursor.execute(
        '''update students set name=%s,class=%s,grade=%s where id=%s''',
                (name,class_,grade,id)
    )
    conn.commit()
    messagebox.showinfo('Info','record upated')
    fill_text_box()

    

def delete_record():
    id = int(id_entry.get())
    if id:
        cursor.execute('''delete from students where id=%s''',(id,))
        conn.commit()
        messagebox.showinfo("Info","deleted")
        fill_text_box()
    else:
        messagebox.showwarning("warning",'id requird')
    
root = tk.Tk()
root.geometry('500x500')

tk.Button(root,text='UPLOAD CSV',command=file_open).pack(pady=10)

text_box=tk.Text(root,height=10,width=50)
text_box.pack(pady=20)

action_frame=tk.Frame(root)
action_frame.pack()

tk.Label(action_frame,text='ID').grid(row=0,column=0)
id_entry=tk.Entry(action_frame,width=4)
id_entry.grid(row=0,column=1)

tk.Label(action_frame,text='Name').grid(row=0,column=2)
name_entry=tk.Entry(action_frame)
name_entry.grid(row=0,column=3)

tk.Label(action_frame,text='Class').grid(row=0,column=4)
class_entry=tk.Entry(action_frame,width=2)
class_entry.grid(row=0,column=5)

tk.Label(action_frame,text='Grade').grid(row=0,column=6)
Grade_entry=tk.Entry(action_frame,width=2)
Grade_entry.grid(row=0,column=7)


tk.Button(action_frame,text='Add',command=add_record).grid(row=1,column=0,padx=10)

tk.Button(action_frame,text='Update',command=Update_record).grid(row=1,column=1,padx=10)
tk.Button(action_frame,text='Delete',command=delete_record).grid(row=1,column=2,padx=10)


fill_text_box()
root.mainloop()





