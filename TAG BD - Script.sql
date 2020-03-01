
CREATE TABLE tbl_categoria (
                id_categoria INT AUTO_INCREMENT NOT NULL,
                nome_categoria VARCHAR NOT NULL,
                desc_categoria VARCHAR,
                Parent_id_categoria INT NOT NULL,
                PRIMARY KEY (id_categoria)
);


CREATE TABLE tbl_pessoa (
                id_pessoa INT AUTO_INCREMENT NOT NULL,
                nome_pessoa VARCHAR NOT NULL,
                nomeSocial_pessoa VARCHAR,
                dtNasc_pessoa DATE NOT NULL,
                PRIMARY KEY (id_pessoa)
);


CREATE TABLE tbl_tarefa (
                id_tarefa INT AUTO_INCREMENT NOT NULL,
                nome_tarefa VARCHAR NOT NULL,
                desc_tarefa VARCHAR NOT NULL,
                id_pessoa INT NOT NULL,
                id_categoria INT NOT NULL,
                PRIMARY KEY (id_tarefa)
);


CREATE TABLE tbl_tarefaEstado (
                id_tarefa INT NOT NULL,
                id_pessoa INT NOT NULL,
                desc_tarefaEstado VARCHAR NOT NULL,
                datetime_tarefaEstado VARCHAR NOT NULL,
                id_categoria INT NOT NULL,
                PRIMARY KEY (id_tarefa, id_pessoa)
);


CREATE TABLE tbl_cpf (
                id_cpf INT AUTO_INCREMENT NOT NULL,
                numero_cpf VARCHAR NOT NULL,
                id_pessoa INT NOT NULL,
                PRIMARY KEY (id_cpf)
);


CREATE UNIQUE INDEX tbl_cpf_idx
 ON tbl_cpf
 ( numero_cpf );

CREATE TABLE tbl_dre (
                id_dre INT AUTO_INCREMENT NOT NULL,
                numero_dre VARCHAR NOT NULL,
                id_pessoa INT NOT NULL,
                PRIMARY KEY (id_dre)
);


CREATE UNIQUE INDEX tbl_dre_idx
 ON tbl_dre
 ( numero_dre );

CREATE TABLE tbl_telefone (
                id_telefone INT AUTO_INCREMENT NOT NULL,
                numero_telefone VARCHAR NOT NULL,
                id_pessoa INT NOT NULL,
                PRIMARY KEY (id_telefone)
);


CREATE UNIQUE INDEX tbl_telefone_idx
 ON tbl_telefone
 ( numero_telefone );

CREATE TABLE tbl_email (
                id_email VARCHAR AUTO_INCREMENT NOT NULL,
                address_email VARCHAR NOT NULL,
                id_pessoa INT NOT NULL,
                PRIMARY KEY (id_email)
);


CREATE UNIQUE INDEX tbl_email_idx
 ON tbl_email
 ( address_email );

ALTER TABLE tbl_categoria ADD CONSTRAINT tbl_categoria_tbl_categoria_fk
FOREIGN KEY (Parent_id_categoria)
REFERENCES tbl_categoria (id_categoria)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE tbl_tarefa ADD CONSTRAINT tbl_categoria_tbl_tarefa_fk
FOREIGN KEY (id_categoria)
REFERENCES tbl_categoria (id_categoria)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE tbl_tarefaEstado ADD CONSTRAINT tbl_categoria_tbl_tarefaestado_fk
FOREIGN KEY (id_categoria)
REFERENCES tbl_categoria (id_categoria)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE tbl_email ADD CONSTRAINT tbl_pessoa_tbl_email_fk
FOREIGN KEY (id_pessoa)
REFERENCES tbl_pessoa (id_pessoa)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE tbl_telefone ADD CONSTRAINT tbl_pessoa_tbl_telefone_fk
FOREIGN KEY (id_pessoa)
REFERENCES tbl_pessoa (id_pessoa)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE tbl_dre ADD CONSTRAINT tbl_pessoa_tbl_dre_fk
FOREIGN KEY (id_pessoa)
REFERENCES tbl_pessoa (id_pessoa)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE tbl_cpf ADD CONSTRAINT tbl_pessoa_tbl_cpf_fk
FOREIGN KEY (id_pessoa)
REFERENCES tbl_pessoa (id_pessoa)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE tbl_tarefa ADD CONSTRAINT tbl_pessoa_tbl_tarefa_fk
FOREIGN KEY (id_pessoa)
REFERENCES tbl_pessoa (id_pessoa)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE tbl_tarefaEstado ADD CONSTRAINT tbl_pessoa_tbl_tarefaestado_fk
FOREIGN KEY (id_pessoa)
REFERENCES tbl_pessoa (id_pessoa)
ON DELETE NO ACTION
ON UPDATE NO ACTION;

ALTER TABLE tbl_tarefaEstado ADD CONSTRAINT tbl_tarefa_tbl_tarefaestado_fk
FOREIGN KEY (id_tarefa)
REFERENCES tbl_tarefa (id_tarefa)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
