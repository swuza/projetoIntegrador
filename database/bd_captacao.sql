CREATE DATABASE Captacao;

USE Captacao;

CREATE TABLE funcionarios (
    id_funcionario INT PRIMARY KEY, 
    nome VARCHAR(255) NOT NULL,        
    cpf VARCHAR(11) NOT NULL,         
    data_nascimento DATE NOT NULL,     
    empresa VARCHAR(255) NOT NULL,    
    cnpj VARCHAR(14) NOT NULL          
);

CREATE TABLE uso_convenio (
    id_uso INT PRIMARY KEY,            
    id_funcionario INT NOT NULL,      
    nome_convenio VARCHAR(255) NOT NULL,  
    tipo_convenio VARCHAR(50) NOT NULL,   
    data_uso DATE NOT NULL,           
    tipo_atendimento VARCHAR(255) NOT NULL,  
    FOREIGN KEY (id_funcionario) REFERENCES funcionarios(id_funcionario) 
);

CREATE TABLE transacao_log (
    id INT PRIMARY KEY,
    arquivo VARCHAR(255) NOT NULL,
    responsavel VARCHAR(255) NOT NULL,
    data_hora DATETIME NOT NULL,
    status VARCHAR(50) NOT NULL,
);