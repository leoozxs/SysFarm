CREATE TABLE lote (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_lote VARCHAR(50) NOT NULL,
    medicamento_id INT NOT NULL,
    fornecedor_id INT NOT NULL,
    validade DATE NOT NULL,
    FOREIGN KEY (medicamento_id) REFERENCES medicamento(id),
    FOREIGN KEY (fornecedor_id) REFERENCES fornecedor(id)
);