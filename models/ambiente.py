from database import execute_sql

class AmbienteModel:
    def buscarTodos(self):
        return execute_sql("SELECT * FROM ambientes order by nome", fetchall=True)
    
    def buscarUmAmbiente(self, id):
        return execute_sql("SELECT * FROM ambientes where id = %s", (id,), fetchone=True)