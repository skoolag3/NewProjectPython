create DATABASE if not exists agendamento_ACME CHARACTER SET utf8mb4
COLLATE utf8mb4_general_ci;
USE agendamento_ACME;

create table if not exists ambientes (
    id int auto_increment primary key,
    nome varchar(50) not null,
    descricao varchar(100),
    capacidade int not null default  1,
    ativo TINYINT(1) not null default 1,
    criado_em DATETIME notnull default current_timestamp,
    atualizado_em DATETIME not null default current_timestamp on update current_timestamp
);

create table usuarios (
    id int auto_increment primary key,
    nome varchar(100) not null,
    email varchar(100) not null,
    telefone varchar(16),
    ativo TINYINT(1) not null default 1,
    criado_em DATETIME not null default current_timestamp,
    atualizado_em DATETIME not null default current_timestamp on update current_timestamp
);

create table agendamentos (
    id int auto_increment primary key,
    ambiente_id int not null,
    usuario_id int not null,
    datainicio datetime not null,
    datafinal datetime not null,
    titulo varchar(50) not null,
    descricao varchar(255),
    status enum('ativo', 'cancelado') not null default 'ativo',
    ativo TINYINT(1) not null default 1,
    criado_em DATETIME not null default current_timestamp,
    atualizado_em DATETIME not null default current_timestamp on update current_timestamp,
    CONSTRAINT fk_agendamento_ambiente FOREIGN KEY (ambiente_id) REFERENCES ambientes(id) ON DELETE RESTRICT on UPDATE CASCADE,
    CONSTRAINT fk_agendamento_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE RESTRICT on update CASCADE,
    CONSTRAINT CHK_datas check (datafinal >= datainicio)
);

create index idx_agendamento_conflito on agendamentos (ambiente_id, datainicio, datafinal, status);