CREATE TABLE fornecedor_medicamento (
    fornecedor_id INT NOT NULL,
    medicamento_id INT NOT NULL,
    PRIMARY KEY (fornecedor_id, medicamento_id),
    FOREIGN KEY (fornecedor_id) REFERENCES fornecedor(id),
    FOREIGN KEY (medicamento_id) REFERENCES medicamento(id)
);