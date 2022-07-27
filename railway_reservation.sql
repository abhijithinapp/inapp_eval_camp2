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
end_id INT NOT NULL FOREIGN KEY REFERENCES stops(stop_id),
birth_filled INT NOT NULL,
wait_list_filled INT NOT NULL);

INSERT INTO trains(train_name, end_id, birth_filled,wait_list_filled) VALUES
('TVM_ALP','1','0','0'),
('TVM_ERN','2','0','0'),
('TVM_KZM','3','0','0');

SELECT * FROM trains


CREATE TABLE passengerdetails(passenger_id INT PRIMARY KEY IDENTITY,
passenger_name VARCHAR(50) NOT NULL, 
stop_id INT FOREIGN KEY REFERENCES stops(stop_id),
train_id INT NOT NULL FOREIGN KEY REFERENCES trains(train_id))

SELECT * FROM passengerdetails

CREATE TABLE waitlist(passenger_id INT PRIMARY KEY IDENTITY,
passenger_name VARCHAR(50) NOT NULL,
stop_id INT FOREIGN KEY REFERENCES stops(stop_id),
train_id INT NOT NULL FOREIGN KEY REFERENCES trains(train_id));

SELECT * FROM waitlist

drop table passengerdetails
drop table waitlist
drop table trains
