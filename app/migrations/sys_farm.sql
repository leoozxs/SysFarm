CREATE DATABASE IF NOT EXISTS sys_farm;
USE sys_farm;

CREATE TABLE IF NOT EXISTS MEDICAMENTO (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nome VARCHAR(150),
    tipo ENUM(
        'Comprimido', 'Cápsula', 'Drágea', 'Pastilha', 'Goma medicamentosa',
        'Pó', 'Granulado', 'Sachê', 'Xarope', 'Solução oral', 'Suspensão oral',
        'Gotas', 'Spray', 'Aerossol', 'Inalável', 'Creme', 'Pomada', 'Gel',
        'Loção', 'Espuma', 'Adesivo transdérmico', 'Supositório', 'Óvulo vaginal',
        'Colírio', 'Pomada oftálmica', 'Gotas otológicas', 'Spray nasal',
        'Injetável', 'Implante', 'Outros'
    ) NOT NULL,
    categoria ENUM(
        'Analgésico', 'Antibiótico', 'Anti-inflamatório', 'Antialérgico', 'Antitérmico',
        'Antifúngico', 'Antiviral', 'Antidepressivo', 'Ansiolítico', 'Antisséptico',
        'Anticoagulante', 'Anti-hipertensivo', 'Antidiabético', 'Anticoncepcional',
        'Antiácido', 'Antiemético', 'Laxante', 'Antidiarreico', 'Expectorante',
        'Descongestionante', 'Corticoide', 'Relaxante muscular', 'Vitaminas', 'Outros'
    ) NOT NULL,
    dosagem VARCHAR(30) NOT NULL,
    ativo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE fornecedor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cnpj VARCHAR(18) NOT NULL UNIQUE,
    ativo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    cargo VARCHAR(50) NOT NULL,
    data_entrada DATE NOT NULL,
    ativo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE lote (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_lote VARCHAR(50) NOT NULL,
    medicamento_id INT NOT NULL,
    fornecedor_id INT NOT NULL,
    validade DATE NOT NULL,
    FOREIGN KEY (medicamento_id) REFERENCES medicamento(id),
    FOREIGN KEY (fornecedor_id) REFERENCES fornecedor(id)
);

CREATE TABLE fornecedor_medicamento (
    fornecedor_id INT NOT NULL,
    medicamento_id INT NOT NULL,
    PRIMARY KEY (fornecedor_id, medicamento_id),
    FOREIGN KEY (fornecedor_id) REFERENCES fornecedor(id),
    FOREIGN KEY (medicamento_id) REFERENCES medicamento(id)
);

CREATE TABLE estoque (
    id INT AUTO_INCREMENT PRIMARY KEY,
    lote_id INT NOT NULL UNIQUE,
    medicamento_id INT NOT NULL,
	fornecedor_id INT NOT NULL,
    data_entrada DATE NOT NULL,
    validade DATE NOT NULL,
    qtd_atual INT NOT NULL DEFAULT 0,
    status VARCHAR(20) NOT NULL,
    FOREIGN KEY (lote_id) REFERENCES lote(id),
    FOREIGN KEY (medicamento_id) REFERENCES medicamento(id),
    FOREIGN KEY (fornecedor_id) REFERENCES fornecedor(id)
);

CREATE TABLE saida (
    id INT AUTO_INCREMENT PRIMARY KEY,
    lote_id INT NOT NULL,
    qtd_saida INT NOT NULL,
    tipo_saida ENUM('Venda', 'Avaria', 'Perda', 'Roubo') NOT NULL,
    usuario_id INT NOT NULL,
    data_saida DATE NOT NULL,
    FOREIGN KEY (lote_id) REFERENCES lote(id),
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);

CREATE TABLE entrada (
    id INT AUTO_INCREMENT PRIMARY KEY,
    lote_id INT NOT NULL,
    qtd_entrada INT NOT NULL,
    data_entrada DATE NOT NULL,
    usuario_id INT NOT NULL,
    FOREIGN KEY (lote_id) REFERENCES lote(id),
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);
-- =========================================
-- Dados de teste - Estoque de Farmácia
-- =========================================

INSERT INTO fornecedor (id, nome, cnpj, ativo) VALUES
(1, 'Farmasul Distribuidora', '11.111.111/0001-11', TRUE),
(2, 'MedPlus Comércio', '22.222.222/0001-22', TRUE),
(3, 'BioFarma Ltda', '33.333.333/0001-33', TRUE),
(4, 'Distribuidora Saúde Total', '44.444.444/0001-44', TRUE),
(5, 'Comercial Vitalmed', '55.555.555/0001-55', TRUE);

select * from entrada;

INSERT INTO usuario (id, nome, cpf, senha, cargo, data_entrada, ativo) VALUES
(1, 'João Silva', '11122233344', '123456', 'Farmacêutico', '2025-01-10', TRUE),
(2, 'Maria Souza', '22233344455', 'abcdef', 'Balconista', '2025-02-15', TRUE),
(3, 'Pedro Lima', '33344455566', 'senha123', 'Gerente', '2024-11-01', TRUE),
(4, 'Ana Costa', '44455566677', 'qwerty', 'Balconista', '2025-06-20', TRUE),
(5, 'Leonardo Valença', '05717919050', '123456', 'Chef da porra toda', '2025-01-10', TRUE),
(6, 'Diego dos Santos', '80031448925', '123456', 'Chefinho da porrinha todinha', '2025-01-10', TRUE);

INSERT INTO medicamento (id, nome, tipo, categoria, dosagem, ativo) VALUES
(1, 'Dipirona', 'Comprimido', 'Analgésico', '10mg', TRUE),
(2, 'Amoxicilina', 'Cápsula', 'Antibiótico', '50mg', TRUE),
(3, 'Ibuprofeno', 'Comprimido', 'Anti-inflamatório', '20mg', TRUE),
(4, 'Loratadina', 'Comprimido', 'Antialérgico', '5mg', TRUE),
(5, 'Paracetamol', 'Comprimido', 'Antitérmico', '30mg', TRUE),
(6, 'Cefalexina', 'Cápsula', 'Antibiótico', '50mg', TRUE);

INSERT INTO fornecedor_medicamento (fornecedor_id, medicamento_id) VALUES
(1, 1), (1, 2), (2, 3), (2, 4), (3, 5), (3, 6), (4, 1), (5, 2);

INSERT INTO lote (id, numero_lote, medicamento_id, fornecedor_id, validade) VALUES
(1, 'LT-0001', 1, 1, '2027-05-10'),
(2, 'LT-0002', 2, 2, '2026-12-01'),
(3, 'LT-0003', 3, 3, '2027-02-15'),
(4, 'LT-0004', 4, 4, '2026-11-20'),
(5, 'LT-0005', 5, 5, '2027-08-30'),
(6, 'LT-0006', 1, 4, '2027-01-05'),
(7, 'LT-0007', 6, 2, '2026-10-10'),
(8, 'LT-0008', 2, 1, '2027-03-25');

INSERT INTO entrada (id, lote_id, qtd_entrada, data_entrada, usuario_id) VALUES
(1, 1, 100, '2026-06-01', 1),
(2, 2, 200, '2026-06-02', 2),
(3, 3, 150, '2026-06-03', 1),
(4, 4, 80,  '2026-06-04', 3),
(5, 5, 120, '2026-06-05', 4),
(6, 6, 90,  '2026-07-01', 1),
(7, 7, 60,  '2026-07-02', 2),
(8, 8, 130, '2026-07-03', 3);

INSERT INTO saida (id, lote_id, qtd_saida, tipo_saida, usuario_id, data_saida) VALUES
(1, 1, 20, 'Venda',  2, '2026-06-10'),
(2, 1, 5,  'Avaria', 1, '2026-06-15'),
(3, 2, 50, 'Venda',  3, '2026-06-12'),
(4, 3, 30, 'Venda',  4, '2026-06-20'),
(5, 4, 10, 'Perda',  1, '2026-06-25'),
(6, 5, 40, 'Venda',  2, '2026-07-05'),
(7, 6, 15, 'Roubo',  3, '2026-07-10'),
(8, 7, 20, 'Venda',  4, '2026-07-12');


INSERT INTO estoque (lote_id, medicamento_id, fornecedor_id, data_entrada, validade, qtd_atual, status) VALUES
(1, 1, 1, '2026-06-01', '2027-05-10', 75,  'Disponível'),
(2, 2, 2, '2026-06-02', '2026-12-01', 150, 'Disponível'),
(3, 3, 3, '2026-06-03', '2027-02-15', 120, 'Disponível'),
(4, 4, 4, '2026-06-04', '2026-11-20', 70,  'Disponível'),
(5, 5, 5, '2026-06-05', '2027-08-30', 80,  'Disponível'),
(6, 1, 4, '2026-07-01', '2027-01-05', 75,  'Disponível'),
(7, 6, 2, '2026-07-02', '2026-10-10', 40,  'Baixo'),
(8, 2, 1, '2026-07-03', '2027-03-25', 130, 'Disponível');
