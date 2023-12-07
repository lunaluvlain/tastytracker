# from tkinter import *
# from tkinter import messagebox
   
# class TastyTracker:
#     def __init__(self, master):
#         self.master = master
#         master.title("tasy tracker")
#         master.geometry("1920x1080")
#         master.configure(bg= "pink")
        
#         self.greet_button = Button(master, text="Masuk", bg="white", command=self.masuk, font="Halvetica 16 bold")
#         self.greet_button.configure(width=10, height=2)
#         self.greet_button.place(x= 700, y=400)
#         self.close_button = Button(master, text="Keluar", bg="white", fg="#8530d1", command=master.destroy, font="Halvetica 16 bold")
#         self.close_button.configure(width=10, height=2)
#         self.close_button.place(x=700, y=500)

#     def masuk(self):
#         self.master.withdraw()  
#         page1 = Toplevel(self.master)
#         page1.title("Welcome to Tasty Tracker")
#         page1.configure(bg="pink")
#         Label(page1, text="Welcome to tasty tracker", font="courier 18 bold", fg="red", bg="pink").pack()
#         page1.geometry("1920x1080")
#         page1.deiconify()

#         add_recipe_button = Button(page1, text="Tambah Resep", bg="white", command=self.tambah_resep, font="Helvetica 16 bold")
#         add_recipe_button.configure(width=15, height=2)
#         add_recipe_button.pack(pady=20)

#         page1.geometry("1920x1080")
#         page1.deiconify()

#     def tambah_resep(self):
#         # Fungsi ini akan menampilkan form untuk menambah resep
#         form = Toplevel(self.master)
#         form.title("Tambah Resep Baru")
#         form.geometry("500x300")
#         form.configure(bg="pink")

#         # Label dan Entry untuk nama resep
#         Label(form, text="Nama Resep:", font="Helvetica 12 bold", bg="pink").pack()
#         name_entry = Entry(form, font="Helvetica 12")
#         name_entry.pack()

#         # Label dan Entry untuk bahan resep
#         Label(form, text="Bahan (pisahkan dengan koma):", font="Helvetica 12 bold", bg="pink").pack()
#         ingredients_entry = Entry(form, font="Helvetica 12")
#         ingredients_entry.pack()

#         # Button untuk menambah resep
#         add_button = Button(form, text="Tambah Resep", bg="white", command=lambda: self.simpan_resep(name_entry.get(), ingredients_entry.get()), font="Helvetica 12 bold")
#         add_button.pack(pady=20)

#     def simpan_resep(self, nama_resep, bahan_resep):
#         # Fungsi ini akan menyimpan resep ke dalam database atau melakukan tindakan sesuai kebutuhan
#         messagebox.showinfo("Info", f"Resep {nama_resep} berhasil ditambahkan!")
    
# root = Tk()
# app = TastyTracker(master=root)
# root.mainloop()

from tkinter import *
from tkinter import messagebox

class TastyTracker:
    def __init__(self, master):
        self.master = master
        master.title("Tasty Tracker")
        master.geometry("1920x1080")
        master.configure(bg="pink")

        self.greet_button = Button(master, text="Masuk", bg="white", command=self.masuk, font="Helvetica 16 bold")
        self.greet_button.configure(width=10, height=2)
        self.greet_button.place(x=700, y=400)
        self.close_button = Button(master, text="Keluar", bg="white", fg="#8530d1", command=master.destroy, font="Helvetica 16 bold")
        self.close_button.configure(width=10, height=2)
        self.close_button.place(x=700, y=500)

        self.label = Label(master, text="TASTY TRACKER", font="Forte 60 bold", bg= "pink")
        self.label.configure(width=15, height=5)
        self.label.place(x=345,y=100)

        # Database sederhana untuk menyimpan resep
        self.recipes = []

    def masuk(self):
        self.master.withdraw()
        page1 = Toplevel(self.master)
        page1.title("Welcome to Tasty Tracker")
        page1.configure(bg="pink")
        Label(page1, text="Welcome to Tasty Tracker", font="courier 18 bold", fg="red", bg="pink").pack()

        # Entry untuk pencarian berdasarkan nama bahan
        search_label = Label(page1, text="Cari Resep berdasarkan Nama Bahan:", font="Helvetica 12 bold", bg="pink")
        search_label.pack(pady=10)
        self.search_entry = Entry(page1, font="Helvetica 12")
        self.search_entry.pack(pady=5)

        # Button untuk memulai pencarian
        search_button = Button(page1, text="Cari", bg="white", command=self.cari_resep, font="Helvetica 12 bold")
        search_button.pack(pady=10)

        # Button untuk membuka form tambah resep
        add_recipe_button = Button(page1, text="Tambah Resep", bg="white", command=self.tambah_resep, font="Helvetica 16 bold")
        add_recipe_button.configure(width=15, height=2)
        add_recipe_button.pack(pady=20)

        # LabelFrame untuk menampilkan resep-resep
        recipe_label_frame = LabelFrame(page1, text="Resep-resep", font="Helvetica 12 bold", bg="pink")
        recipe_label_frame.pack(padx=20, pady=20, expand=True, fill="both")

        # Listbox untuk menampilkan resep-resep
        self.recipe_listbox = Listbox(recipe_label_frame, font="Helvetica 12", selectmode=SINGLE)
        self.recipe_listbox.pack(expand=True, fill="both")

        # Scrollbar untuk Listbox
        scrollbar = Scrollbar(recipe_label_frame)
        scrollbar.pack(side=RIGHT, fill="y")
        self.recipe_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.recipe_listbox.yview)

        # Binding untuk mengaktifkan event ketika item di Listbox diklik
        self.recipe_listbox.bind("<Double-Button-1>", self.tampilkan_detail_resep)

        page1.geometry("1920x1080")
        page1.deiconify()

    def tambah_resep(self):
        # Fungsi ini akan menampilkan form untuk menambah resep
        form = Toplevel(self.master)
        form.title("Tambah Resep Baru")
        form.geometry("500x400")
        form.configure(bg="pink")

        # Label dan Entry untuk nama resep
        Label(form, text="Nama Resep:", font="Helvetica 12 bold", bg="pink").pack()
        name_entry = Entry(form, font="Helvetica 12")
        name_entry.pack()

        # Label dan Entry untuk bahan resep
        Label(form, text="Bahan (pisahkan dengan koma):", font="Helvetica 12 bold", bg="pink").pack()
        ingredients_entry = Entry(form, font="Helvetica 12")
        ingredients_entry.pack()

        # Label dan Entry untuk langkah-langkah resep
        Label(form, text="Langkah-langkah:", font="Helvetica 12 bold", bg="pink").pack()
        steps_entry = Entry(form, font="Helvetica 12")
        steps_entry.pack()

        # Button untuk menambah resep
        add_button = Button(form, text="Tambah Resep", bg="white", command=lambda: self.simpan_resep(name_entry.get(), ingredients_entry.get(), steps_entry.get()), font="Helvetica 12 bold")
        add_button.pack(pady=20)

    def simpan_resep(self, nama_resep, bahan_resep, langkah_resep):
        # Fungsi ini akan menyimpan resep ke dalam database atau melakukan tindakan sesuai kebutuhan
        self.recipes.append({"name": nama_resep, "ingredients": bahan_resep, "steps": langkah_resep})
        self.update_recipe_listbox(nama_resep)

    def update_recipe_listbox(self, nama_resep):
        # Fungsi ini akan menambahkan nama resep ke dalam Listbox
        self.recipe_listbox.insert(END, nama_resep)

    def tampilkan_detail_resep(self, event):
        # Fungsi ini akan menampilkan laman baru dengan detail resep
        selected_index = self.recipe_listbox.curselection()
        if selected_index:
            selected_recipe = self.recipes[selected_index[0]]
            detail_laman = Toplevel(self.master)
            detail_laman.title(selected_recipe["name"])
            detail_laman.geometry("500x400")

            # Menampilkan informasi resep di laman baru
            Label(detail_laman, text=f"Nama Resep: {selected_recipe['name']}", font="Helvetica 14 bold").pack(pady=10)
            Label(detail_laman, text=f"Bahan: {selected_recipe['ingredients']}", font="Helvetica 12").pack(pady=5)
            Label(detail_laman, text=f"Langkah-langkah: {selected_recipe['steps']}", font="Helvetica 12").pack(pady=5)

    def cari_resep(self):
        # Fungsi ini akan mencari resep berdasarkan nama bahan
        keyword = self.search_entry.get().lower()
        matching_recipes = [recipe["name"] for recipe in self.recipes if keyword in recipe["ingredients"].lower()]
        
        # Membersihkan Listbox sebelum menampilkan hasil pencarian baru
        self.recipe_listbox.delete(0, END)
        
        # Menampilkan hasil pencarian di Listbox
        for recipe in matching_recipes:
            self.recipe_listbox.insert(END, recipe)

if __name__ == "__main__":
    root = Tk()
    app = TastyTracker(master=root)
    root.mainloop()
