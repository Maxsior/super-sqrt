import tkinter

class ValidEntry(tkinter.Spinbox):
    """Entry wich controls input characters"""
    def __init__(self, master, value="", **kw):
        tkinter.Spinbox.__init__(*(self, master), **kw)
        self.__value = value
        self.variable = tkinter.StringVar()
        self.variable.set(value)
        self.variable.trace("w", self.__callback)
        self.config(textvariable=self.variable)

    def __callback(self, *dummy):
        value = self.variable.get()
        newvalue = self.validate(value)
        if newvalue is None:
            self.variable.set(self.__value)
        elif newvalue != value:
            self.__value = newvalue
            self.variable.set(newvalue)
        else:
            self.__value = value

    def validate(self, value):
        minv, maxv = self.cget("from"), self.cget("to")
        if value and minv <= float(value) <= maxv:
            return value

    def get(self):
        return float(self.variable.get())


class Application(tkinter.Frame):
    query = ''

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        entry = ValidEntry(master)
        entry.pack()
        self.pack()
        self.init_elements()

    def init_elements(self):
        self.label_input = tkinter.Label(self)
        self.label_input["text"] = "Введите выражение:"
        self.label_input.pack()

        self.input = tkinter.Entry(self)
        self.input.pack()

        self.label_output = tkinter.Label(self)
        self.label_output["text"] = "Результат:"
        self.label_output.pack()

        self.output = tkinter.Label(self)
        self.output.pack()

    def add_to_query(self, symbol):
        pass


root = tkinter.Tk()
app = Application(master=root)
app.pack()
root.title('МЕНЯТЬ НАЗВАНИЕ В ЗАВИСИМОСТИ ОТ ЯЗЫКА???')
root.geometry('1000x500')
app.mainloop()