from database import execute_sql

class UsuarioModel:
    @staticmethod
    def buscarTodos():
        return execute_sql("select * from usuarios order by nome", fetchall=True)
    
    @staticmethod
    def buscarUmUsuario(id: int):
        return execute_sql("select * from usuarios where id = %s", (id,), fetchone=True)
    
    @staticmethod
    def inserir(nome: str, email: str, telefone: str):
        return execute_sql("insert into usuarios (nome, email, telefone) values (%s, %s, %s)",
                          (nome, email, telefone), commit=True)
    
    @staticmethod
    def atualizar(id: int, nome: str, email: str, telefone: str, ativo: int):
        return execute_sql("update usuarios set nome = %s, email = %s, telefone = %s, ativo = %s where id = %s",
                            (nome, email, telefone, ativo, id), commit=True)
    
    @staticmethod
    def excluir(id: int):
        return execute_sql("delete from usuarios where id = %s", (id,), commit=True)