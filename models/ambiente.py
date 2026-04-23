from database import execute_sql

class AmbienteModel:
    def buscarTodos(self):
        return execute_sql("SELECT * FROM ambientes order by nome", fetchall=True)
    
    def buscarUmAmbiente(self, id: int):
        return execute_sql("SELECT * FROM ambientes where id = %s", (id,), fetchone=True)
    
    def inserir(self, nome: str, descricao: str, capacidade: int):
        return execute_sql("INSERT INTO ambientes (nome, descricao, capacidade) VALUES (%s, %s, %s)",
                            (nome, descricao, capacidade), commit=True)
    
    def atualizar(self, id: int, nome: str, descricao: str, capacidade: int, ativo: int):
        return execute_sql("UPDATE ambientes SET nome = %s, descricao = %s, capacidade = %s, ativo = %s WHERE id = %s",
                            (nome, descricao, capacidade, ativo, id), commit=True)
    
    def excluir(self, id: int):
        return execute_sql("DELETE FROM ambientes WHERE id = %s", (id,), commit=True)