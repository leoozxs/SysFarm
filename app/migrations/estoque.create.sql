CREATE TABLE estoque (
    id INT AUTO_INCREMENT PRIMARY KEY,
    lote_id INT NOT NULL UNIQUE,
    medicamento_id INT NOT NULL,
    data_entrada DATE NOT NULL,
    validade DATE NOT NULL,
    qtd_atual INT NOT NULL DEFAULT 0,
    status VARCHAR(20) NOT NULL,
    FOREIGN KEY (lote_id) REFERENCES lote(id),
    FOREIGN KEY (medicamento_id) REFERENCES medicamento(id)
);