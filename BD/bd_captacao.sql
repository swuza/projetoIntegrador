CREATE DATABASE Captacao;

USE Captacao;

CREATE TABLE Funcionarios (
    ID_Funcionario INT PRIMARY KEY, 
    Nome VARCHAR(255) NOT NULL,        
    CPF VARCHAR(11) NOT NULL,         
    Data_Nascimento DATE NOT NULL,     
    Empresa VARCHAR(255) NOT NULL,    
    CNPJ VARCHAR(14) NOT NULL          
);

CREATE TABLE Uso_Convenio (
    ID_Uso INT PRIMARY KEY,            
    ID_Funcionario INT NOT NULL,      
    Nome_Convenio VARCHAR(255) NOT NULL,  
    Tipo_Convenio VARCHAR(50) NOT NULL,   
    Data_Uso DATE NOT NULL,           
    Tipo_Atendimento VARCHAR(255) NOT NULL,  
    FOREIGN KEY (ID_Funcionario) REFERENCES Funcionarios(ID_Funcionario) 
);
