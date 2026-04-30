from database import execute_sql

class AgendamentoModel:
    @staticmethod
    def buscarTodos():
        return execute_sql("select * from agendamentos order by data_hora", fetchall=True)
    
    @staticmethod
    def buscarUmAgendamento(id: int):
        return execute_sql("select * from agendamentos where id = %s", (id,), fetchone=True)
    
    @staticmethod
    def inserir(id_usuario: int, id_ambiente: int, data_hora: str, duracao: int):
        return execute_sql("insert into agendamentos (id_usuario, id_ambiente, data_hora, duracao) values (%s, %s, %s, %s)",
                          (id_usuario, id_ambiente, data_hora, duracao), commit=True)
    
    @staticmethod
    def atualizar(id: int, id_usuario: int, id_ambiente: int, data_hora: str, duracao: int):
        return execute_sql("update agendamentos set id_usuario = %s, id_ambiente = %s, data_hora = %s, duracao = %s where id = %s",
                            (id_usuario, id_ambiente, data_hora, duracao, id), commit=True)
    
    @staticmethod
    def excluir(id: int):
        return execute_sql("delete from agendamentos where id = %s", (id,), commit=True)