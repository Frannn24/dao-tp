""" 
    def registrar_extraviados(self, prestamo_id):
            try:
                with self.conn:
                    self.cursor.execute("SELECT id_prestamo, id_libro FROM prestamo WHERE id_prestamo = ?", (prestamo_id))
                    prestamo_info = self.cursor.fetchone()
                    
                    if not prestamo_info:
                        mensaje_error = "El ID de préstamo no existe en la base de datos. Por favor, ingrese un ID de préstamo válido."
                        messagebox.showerror("Error", mensaje_error)
                        return
                    
                    with self.conn:
                        self.cursor.execute("SELECT fecha_devolucion FROM prestamo WHERE id_prestamo = ?", (prestamo_id))
                        fecha_devolucion = self.cursor.fetchone()
                        fecha_mes = fecha_devolucion + timedelta(days=30)
                    
                    if datetime.now < (fecha_mes):
                        mensaje_error = "La fecha actual no es mayor a los 30 dias pactados."
                        messagebox.showerror("Error", mensaje_error)
                        return
                with self.conn:
                    self.cursor.execute("UPDATE libros SET estado = 'Extraviado' WHERE codigo = ?", (prestamo_info[1],))
                mensaje_exito = f"Libro ID: {prestamo_info[1]} registrado como extraviado con exito."
                messagebox.showinfo("Éxito", mensaje_exito)
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Error al registrar el extravio del prestamo: {prestamo_id}")                
"""