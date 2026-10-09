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
