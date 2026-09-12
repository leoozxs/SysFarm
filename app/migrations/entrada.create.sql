CREATE TABLE entrada (
    id INT AUTO_INCREMENT PRIMARY KEY,
    lote_id INT NOT NULL,
    qtd_entrada INT NOT NULL,
    data_entrada DATE NOT NULL,
    usuario_id INT NOT NULL,
    FOREIGN KEY (lote_id) REFERENCES lote(id),
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);