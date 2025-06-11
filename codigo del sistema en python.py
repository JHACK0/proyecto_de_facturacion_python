import tkinter as tk
from tkinter import messagebox

class SistemaFacturacionSupermercado:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Busqueda De Productos")
        self.root.geometry("900x600")

        
        self.productos = {
        
            "Arroz Doble Carolina 1kg": 5000,
            "Aceite de Cocina Girasol 1L": 8000,
            "Leche Alquería Entera 1L": 3000,
            "Huevos de Gallina Campesina x12": 7000,
            "Atún en Lata Van Camp's 200g": 5000,
            "Azúcar Blanca Incauca 1kg": 4000,
            "Café Liofilizado Sello Rojo 100g": 6000,
            "Harina de Trigo Harinera del Valle 1kg": 3500,
            "Pan de Molde Bimbo 680g": 4500,
            "Galletas Saltín Noel 150g": 2500,
            "Cerveza Aguila 355ml": 2000,
            "Coca-Cola 2.5L": 5000,
            "Jugo de Naranja Natural 1L": 4000,
            "Agua Mineral Manantial 500ml": 1500,
            "Café Juan Valdez 250g": 12000,
            "Vino Tinto Santa Helena 750ml": 25000,
            "Gaseosa Colombiana Postobón 300ml": 1200,
            "Energizante Red Bull 250ml": 5000,
            "Té Lipton Limón 25 bolsas": 3500,
            "Jugo Hit Guayaba 200ml": 1000,
            "Detergente en Polvo Ariel 2kg": 12000,
            "Cloro Blanqueador Azul 1L": 2500,
            "Papel Higiénico Familia x4": 5000,
            "Limpiavidrios Windex 500ml": 3000,
            "Desodorante Ambiente Glade 360ml": 7000,
            "Jabón de Barra Protex 125g": 1500,
            "Esponja Scotch-Brite": 1000,
            "Cepillo de Dientes Colgate": 2000,
            "Shampoo Sedal 400ml": 8000,
            "Desinfectante Lysol 500ml": 6000,
            "Papel Toalla Elite x2": 6000,
            "Desodorante Axe 150ml": 9000,
            "Cepillo de Dientes Oral-B": 3500,
            "Crema Dental Colgate Triple Acción 90g": 5000,
            "Gel Antibacterial Dettol 250ml": 4000,
            "Toallas Húmedas Pampers x80": 7000,
            "Pañales Huggies Active Sec x20": 25000,
            "Acondicionador Sedal 350ml": 8500,
            "Crema Hidratante Nivea 200ml": 10000,
            "Cuchillas de Afeitar Gillette x5": 15000,
            "Smartphone Samsung Galaxy A52": 1800000,
            "Televisor LG 55'' 4K": 3500000,
            "Auriculares Inalámbricos Apple AirPods": 800000,
            "Impresora Multifuncional HP Deskjet": 300000,
            "Disco Duro Externo Seagate 1TB": 400000,
            "Mouse Logitech Inalámbrico": 80000,
            "Teclado Gamer Razer": 250000,
            "Cámara de Seguridad Xiaomi": 150000,
            "Batería Portátil Anker 20000mAh": 150000,
            "Altavoz Bluetooth JBL Charge 4": 400000,   
            "Nevera Mabe 300L": 1500000,
            "Lavadora Samsung 15kg": 2000000,
            "Estufa Haceb 4 Puestos": 800000,
            "Microondas Panasonic 30L": 500000,
            "Licuadora Oster 10 Velocidades": 150000,
            "Aspiradora Samsung Powerbot": 700000,
            "Plancha de Vapor Black+Decker": 80000,
            "Licuadora de Mano KitchenAid": 250000,
            "Batidora de Pedestal Hamilton Beach": 300000,
            "Cafetera Philips Senseo": 180000,          
            "Camiseta Polo Ralph Lauren": 120000,
            "Zapatos Adidas Superstar": 350000,
            "Vestido de Fiesta Zara": 250000,
            "Pantalón Jeans Levi's": 200000,
            "Camisa Tommy Hilfiger": 180000,
            "Bolso Coach de Cuero": 600000,
            "Corbata Hugo Boss": 150000,
            "Bufanda Burberry": 300000,
            "Calcetines Nike": 25000,
            "Gorra New Era": 80000,
            "Mochila Totto": 120000,
            "Reloj Casio Digital": 90000,
            "Lámpara de Escritorio LED": 60000,
            "Libro El Alquimista de Paulo Coelho": 35000,
            "Gafas de Sol Ray-Ban Aviator": 250000,
            "Planta Ornamental": 25000,
            "Caja de Herramientas 100 piezas": 80000,
            "Mapa Mundial Decorativo": 40000,
            "Silla de Oficina Ergonómica": 180000,
            "Cable HDMI 2m": 150000
            "TV Samsung 50'' 4K": 2500000,
            "Laptop HP Core i5": 3000000,
            "iPhone 12 Pro 256GB": 5000000,
            "Audífonos Sony WH-1000XM4": 1500000,
            "Consola PS5": 4000000,
            "Refrigerador LG 400L": 1700000,
            "Lavadora Haceb 10kg": 2200000,
            "Estufa Whirlpool 6 Puestos": 900000,
            "Licuadora Oster 12 Velocidades": 180000,
            "Plancha de Vapor Philips": 100000,
            # Ropa y Calzado
            "Camiseta Adidas Originals": 90000,
            "Zapatos Timberland": 400000,
            "Vestido de Noche Pronovias": 350000,
            "Pantalón Dockers": 150000,
            "Camisa Lacoste": 200000,
            "Mochila Adidas Classic": 100000,
            "Reloj Swatch": 180000,
            "Bufanda Louis Vuitton": 500000,
            "Zapatillas Puma": 130000,
            "Corbata Calvin Klein": 90000,
            # Electrónicos
            "TV LG 65'' 8K": 6000000,
            "Macbook Pro 13''": 7000000,
            "Samsung Galaxy S21 Ultra": 6000000,
            "AirPods Pro": 1000000,
            "Xbox Series X": 4500000,
            "Congelador Mabe 200L": 1200000,
            "Lavaplatos LG": 3000000,
            "Licuadora Ninja 1000W": 200000,
            "Batidora KitchenAid 6 Velocidades": 250000,
            "Plancha Black+Decker Digital": 120000,
            # Hogar y Decoración
            "Sofá de Cuero": 2500000,
            "Mesa de Comedor de Vidrio": 1500000,
            "Silla Ergonómica para Escritorio": 350000,
            "Cuadro Abstracto": 800000,
            "Lámpara de Pie Moderna": 400000,
            "Alfombra Persa": 700000,
            "Cortinas Blackout": 200000,
            "Cojines Decorativos": 50000,
            "Mueble de TV": 600000,
            "Vajilla de Porcelana": 300000,
        }

     
        self.carrito = {}
        self.total = 0.0

        self.color_fondo = "#f2f2f2"
        self.color_boton = "#4CAF50"
        self.color_boton_hover = "#45a049"

        self.frame_buscar = tk.Frame(root, bg=self.color_fondo)
        self.frame_buscar.pack(pady=20)

        self.lbl_bienvenida = tk.Label(self.frame_buscar, text="Bienvenido al Sistema de busqueda de productos", font=("Arial", 24), bg=self.color_fondo, fg=self.color_texto)
        self.lbl_bienvenida.pack(pady=10)

        self.entry_buscar = tk.Entry(self.frame_buscar, width=50, font=("Arial", 14))
        self.entry_buscar.pack(side=tk.LEFT, padx=10)

        self.btn_buscar = tk.Button(self.frame_buscar, text="Buscar", command=self.buscar_producto, bg=self.color_boton, fg="white", activebackground=self.color_boton_hover, font=("Arial", 14))
        self.btn_buscar.pack(side=tk.LEFT, padx=10)

        self.frame_productos = tk.Frame(root, bg=self.color_fondo)
        self.frame_productos.pack(pady=20, padx=10, fill=tk.BOTH, expand=True)

        self.lbl_productos = tk.Label(self.frame_productos, text="Productos", font=("Arial", 18, "bold"), bg=self.color_fondo, fg=self.color_texto)
        self.lbl_productos.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.scrollbar_productos = tk.Scrollbar(self.frame_productos)
        self.scrollbar_productos.grid(row=1, column=1, sticky="ns")

        self.listbox_productos = tk.Listbox(self.frame_productos, width=60, height=20, font=("Arial", 12), yscrollcommand=self.scrollbar_productos.set)
        self.listbox_productos.grid(row=1, column=0, padx=10, sticky="nsew")
        self.scrollbar_productos.config(command=self.listbox_productos.yview)

        self.frame_total = tk.Frame(root, bg=self.color_fondo)
        self.frame_total.pack(pady=20)

        self.lbl_total = tk.Label(self.frame_total, text="Total: $0.00", font=("Arial", 18), bg=self.color_fondo, fg=self.color_texto)
        self.lbl_total.pack(padx=10)

        self.btn_agregar = tk.Button(self.frame_total, text="Agregar al Carrito", command=self.agregar_al_carrito, bg=self.color_boton, fg="white", activebackground=self.color_boton_hover, font=("Arial", 14))
        self.btn_agregar.pack(side=tk.LEFT, padx=10)

        self.btn_finalizar = tk.Button(self.frame_total, text="Finalizar Compra", command=self.finalizar_compra, bg=self.color_boton, fg="white", activebackground=self.color_boton_hover, font=("Arial", 14))
        self.btn_finalizar.pack(side=tk.RIGHT, padx=10)

        # Carrito de compras
        self.frame_carrito = tk.Frame(root, bg=self.color_marco)
        self.frame_carrito.pack(pady=20, padx=10, fill=tk.BOTH, expand=True)

        self.lbl_carrito = tk.Label(self.frame_carrito, text="Carrito de Compras", font=("Arial", 18, "bold"), bg=self.color_marco, fg=self.color_texto)
        self.lbl_carrito.pack(pady=10)

        self.texto_carrito = tk.Text(self.frame_carrito, width=60, height=10, font=("Arial", 12))
        self.texto_carrito.pack(pady=10)

        self.lbl_total_compra = tk.Label(self.frame_carrito, text="Total de la Compra: $0.00", font=("Arial", 14), bg=self.color_marco, fg=self.color_texto)
        self.lbl_total_compra.pack(pady=10)

        self.btn_agregar_nuevo = tk.Button(self.frame_carrito, text="Agregar Nuevo Producto", command=self.agregar_nuevo_producto, bg=self.color_boton, fg="white", activebackground=self.color_boton_hover, font=("Arial", 14))
        self.btn_agregar_nuevo.pack(pady=10)

        # Llenar la lista de productos
        self.actualizar_lista_productos()

    def buscar_producto(self):
        self.listbox_productos.delete(0, tk.END)
        texto_busqueda = self.entry_buscar.get().lower()
        for producto, precio in self.productos.items():
            if texto_busqueda in producto.lower():
                self.listbox_productos.insert(tk.END, f"{producto} - ${precio:.2f}")

    def agregar_al_carrito(self):
        seleccion = self.listbox_productos.curselection()
        if seleccion:
            producto_seleccionado = self.listbox_productos.get(seleccion)
            producto, precio = producto_seleccionado.split(" - ")
            precio = float(precio.replace("$", ""))
            if producto in self.carrito:
                self.carrito[producto] += precio
            else:
                self.carrito[producto] = precio
            self.actualizar_carrito()

    def actualizar_carrito(self):
        self.texto_carrito.delete(1.0, tk.END)
        self.total = sum(self.carrito.values())
        for producto, precio in self.carrito.items():
            self.texto_carrito.insert(tk.END, f"{producto} - ${precio:.2f}\n")
        self.lbl_total_compra.config(text=f"Total de la Compra: ${self.total:.2f}")
        self.lbl_total.config(text=f"Total: ${self.total:.2f}")

    def finalizar_compra(self):
        messagebox.showinfo("Compra Finalizada", "¡Gracias por su compra!")
        self.carrito = {}
        self.total = 0.0
        self.texto_carrito.delete(1.0, tk.END)
        self.lbl_total_compra.config(text="Total de la Compra: $0.00")
        self.lbl_total.config(text="Total: $0.00")

    def actualizar_lista_productos(self):
        self.listbox_productos.delete(0, tk.END)
        for producto, precio in self.productos.items():
            self.listbox_productos.insert(tk.END, f"{producto} - ${precio:.2f}")

    def agregar_nuevo_producto(self):
        ventana_agregar = tk.Toplevel(self.root)
        ventana_agregar.title("Agregar Nuevo Producto")

        frame_agregar = tk.Frame(ventana_agregar, bg=self.color_fondo)
        frame_agregar.pack(padx=20, pady=10)

        lbl_nombre = tk.Label(frame_agregar, text="Nombre del Producto:", font=("Arial", 14), bg=self.color_fondo, fg=self.color_texto)
        lbl_nombre.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        entry_nombre = tk.Entry(frame_agregar, width=30, font=("Arial", 12))
        entry_nombre.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        lbl_precio = tk.Label(frame_agregar, text="Precio:", font=("Arial", 14), bg=self.color_fondo, fg=self.color_texto)
        lbl_precio.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        entry_precio = tk.Entry(frame_agregar, width=15, font=("Arial", 12))
        entry_precio.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        btn_agregar = tk.Button(frame_agregar, text="Agregar", command=lambda: self.agregar_producto_nuevo(entry_nombre.get(), entry_precio.get(), ventana_agregar), bg=self.color_boton, fg="white", activebackground=self.color_boton_hover, font=("Arial", 14))
        btn_agregar.grid(row=2, columnspan=2, pady=20)

    def agregar_producto_nuevo(self, nombre, precio, ventana):
        try:
            precio = float(precio)
            if nombre and precio > 0:
                self.productos[nombre] = precio
                self.actualizar_lista_productos()
                messagebox.showinfo("Producto Agregado", f"Se ha agregado '{nombre}' correctamente.")
                ventana.destroy()
            else:
                messagebox.showerror("Error", "Ingrese un nombre de producto válido y un precio mayor que cero.")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un precio válido (número).")

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaFacturacionSupermercado(root)
    root.mainloop()
