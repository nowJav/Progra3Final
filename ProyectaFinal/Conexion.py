import pyodbc

class Connect:
    def __init__(self):
        server = 'proyectofin.database.windows.net' 
        database = 'RFID' 
        username = 'Administrador1' 
        password = 'base1122.'

        self.cnn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

    def __str__(self):
        datos = self.consulta()
        aux = ""
        for row in datos:
            aux = aux + str(row)+"\n"
        return aux

    def consulta(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM data_rfid")
        datos = cur.fetchall()
        cur.close()
        return datos
    
    def buscar(self,cod_rfid):
        cur = self.cnn.cursor()
        sql = "SELECT * FROM data_rfid WHERE id ={}".format(cod_rfid)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()
        return datos
    
    def insertar(self,cod_rfid,name,tipo,estatus,date):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO data_rfid (cod_rfid, name, tipo, estatus,date)
        VALUES ('{}','{}','{}','{}','{}')'''.format(cod_rfid,name,tipo,estatus,date)
        cur.execute(sql)
        #n = cur.rowcount
        self.cnn.commit()
        cur.close()
        #return n
    
    def eliminar(self,id):
        cur = self.cnn.cursor()
        sql = '''DELETE FROM data_rfid WHERE id ='{}' '''.format(id)
        cur.execute(sql)
        #n = cur.rowcount()
        self.cnn.commit()
        cur.close()
        #return n
    
    def modificar(self,id,cod_rfid,name,tipo,estatus):
        cur = self.cnn.cursor()
        sql = '''UPDATE data_rfid SET cod_rfid = '{}', name='{}',tipo='{}',estatus='{}'
        WHERE id = '{}' '''.format(cod_rfid,name,tipo,estatus,id)
        cur.execute(sql)
        #n = cur.rowcount()
        self.cnn.commit()
        cur.close()
        #return n