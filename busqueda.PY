from pydantic import BaseModel
import Conexion


class Proveedores(BaseModel):
    Nit: int
    Nombre: str
    Producto: str
    Cantidad: int
    

    def __str__(self):
        datos=self.consulta_Proveedor()        
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
        
    def consulta_Proveedor(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM Proveedor")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def buscar_Proveedor(self, Nit):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM compras WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos
    
    def inserta_Proveedor(self,Nit, Nombre, Producto, Cantidad):
        cur = self.cnn.cursor()
        sql='''INSERT INTO Proveedor(Nit, Nombre, Producto, Cantidad) 
        VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(Nit, Nombre, Producto, Cantidad)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def elimina_Proveedor(self,Nit):
        cur = self.cnn.cursor()
        sql='''DELETE FROM Proveedor WHERE Nit = {}'''.format(Nit)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modifica_Proveedor(self,Nit, Nombre, Producto, Cantidad):
        cur = self.cnn.cursor()
        sql='''UPDATE Proveedor SET Nit='{}', Nombre='{}', Producto='{}', Cantidad='{}',
        Precio='{}', ValorTotal='{}', where Id = {}'''.format(Nit, Nombre, Producto, Cantidad)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n 
