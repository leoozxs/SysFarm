CREATE TABLE saida (
    id INT AUTO_INCREMENT PRIMARY KEY,
    lote_id INT NOT NULL,
    qtd_saida INT NOT NULL,
    tipo_saida ENUM('Venda', 'Avaria', 'Perda', 'Roubo') NOT NULL,
    usuario_id INT NOT NULL,
    data_saida DATETIME NOT NULL,
    FOREIGN KEY (lote_id) REFERENCES lote(id),
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);