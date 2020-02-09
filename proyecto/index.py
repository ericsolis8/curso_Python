from tkinter import ttk
from tkinter import *

import sqlite3


class Product:

    db_name = 'database.db'

    def __init__(self, window):
        self.wind = window
        self.wind.title('Tienda Online')

        # crear frame
        frame = LabelFrame(self.wind, text='Registrar un producto')
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        # Input Nombre
        Label(frame, text='Nombre: ').grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column=1)

        # Input Precio
        Label(frame, text='Precio: ').grid(row=2, column=0)
        self.price = Entry(frame)
        self.price.grid(row=2, column=1)

        ttk.Button(frame, text='Guardar', command=self.add_product).grid(
            row=3, columnspan=2, sticky=W + E)

        # mensaje de guardado
        self.message = Label(text='', fg='red')
        self.message.grid(row=3, column=0, columnspan=2, sticky=W + E)

        # table
        self.tree = ttk.Treeview(height=10, column=2)
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='Nombre', anchor=CENTER)
        self.tree.heading('#1', text='Precio', anchor=CENTER)

        ttk.Button(text='Borrar').grid(row=5, column=0, sticky=W+E)
        ttk.Button(text='Salir').grid(row=5, column=1, sticky=W+E)
        self.get_products()

    def run_query(self, query, parameters={}):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
            return result
    # limpiando la tabla
    def get_products(self):

        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
    # consulta para obtener los datos en la consola
        query = 'SELECT * FROM product ORDER BY name DESC'
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert('', 0, text=row[1], value=row[2])

    def validation(self):
        return len(self.name.get()) != 0 and len(self.price.get()) != 0

    def add_product(self):
        if self.validation():
            query = 'INSERT INTO product VALUES(NULL, ?, ?)'
            parameters = (self.name.get(), self.price.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Product {} se ha agregado!'.format(
            self.name.get())
            self.name.delete(0, END)
            self.price.delete(0, END)
        else:
            self.message['text'] = 'Por favor llena los campos'
        # ver los cambios en la tabla
        self.get_products()

    def delete_product(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text']
        except IndexError as e:
            self.message['text'] = 'Selecciona un producto'
            return
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM product WHERE name = ?'
        self.run_query(query, {name})
        self.message['text'] = 'Producto {} ha sido borrado'.format(name)
        self.get_products()


if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
