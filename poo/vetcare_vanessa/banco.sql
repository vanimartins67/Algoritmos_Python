CREATE DATABASE IF NOT EXISTS vetcare;
USE vetcare;

CREATE TABLE IF NOT EXISTS person (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(200) NOT NULL,
  telefone VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS tutor (
  id INT PRIMARY KEY,
  endereco VARCHAR(255),
  FOREIGN KEY (id) REFERENCES person(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS veterinario (
  id INT PRIMARY KEY,
  crmv VARCHAR(50),
  FOREIGN KEY (id) REFERENCES person(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS animal (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  especie VARCHAR(50),
  raca VARCHAR(50),
  idade INT,
  tutor_id INT,
  FOREIGN KEY (tutor_id) REFERENCES tutor(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS consulta (
  id INT AUTO_INCREMENT PRIMARY KEY,
  animal_id INT,
  vet_id INT,
  data_consulta VARCHAR(20),
  hora_consulta VARCHAR(10),
  FOREIGN KEY (animal_id) REFERENCES animal(id),
  FOREIGN KEY (vet_id) REFERENCES veterinario(id)
);

CREATE TABLE IF NOT EXISTS prescricao (
  id INT AUTO_INCREMENT PRIMARY KEY,
  consulta_id INT,
  texto TEXT,
  FOREIGN KEY (consulta_id) REFERENCES consulta(id)
);

CREATE TABLE IF NOT EXISTS consulta (
  id INT AUTO_INCREMENT PRIMARY KEY,
  animal_id INT,
  vet_id INT,
  data_consulta VARCHAR(20),
  hora_consulta VARCHAR(10),
  FOREIGN KEY (animal_id) REFERENCES animal(id),
  FOREIGN KEY (vet_id) REFERENCES veterinario(id)
);

CREATE TABLE IF NOT EXISTS prescricao (
  id INT AUTO_INCREMENT PRIMARY KEY,
  consulta_id INT,
  texto TEXT,
  FOREIGN KEY (consulta_id) REFERENCES consulta(id)
);