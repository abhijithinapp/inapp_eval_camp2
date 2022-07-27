use camp2
create table stops(stop_id INT PRIMARY KEY,
stop VARCHAR(50))
INSERT INTO stops VALUES 
('0','Trivandrum'),
('1','Alappy'),
('2','Ernakulam'),
('3','Kozhikkode');
SELECT * FROM stops

CREATE TABLE trains(train_id INT PRIMARY KEY IDENTITY,
train_name VARCHAR(50),
start_id INT NOT NULL FOREIGN KEY REFERENCES stops(stop_id),
end_id INT NOT NULL FOREIGN KEY REFERENCES stops(stop_id),
birth_filled INT NOT NULL,
wait_list_filled INT NOT NULL);

INSERT INTO trains(train_name, start_id,end_id, birth_filled,wait_list_filled) VALUES
('TVM_ALP','0','1','0','0'),
('TVM_ERN','0','2','0','0'),
('TVM_KZM','0','3','0','0');

SELECT * FROM trains