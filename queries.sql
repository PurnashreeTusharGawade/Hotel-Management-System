USE hotel_management;
CREATE TABLE signup (
    name varchar(50),
    email varchar(50) primary key,
    secq varchar(50),
    seca varchar(50),
    password varchar(50)
);
SELECT * from details;
DESC guest;

CREATE TABLE guest (
    guest_id INT PRIMARY KEY,
    guest_name VARCHAR(30) NOT NULL,
    phone BIGINT NOT NULL,
    email varchar(30) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    nationality VARCHAR(20) NOT NULL,
    address VARCHAR(40) NOT NULL
);
SELECT * FROM guest;
DESC guest;

CREATE TABLE room (
	roomno INT PRIMARY KEY,
    floor INT NOT NULL,
    roomType varchar(20) NOT NULL,
    price int NOT NULL,
    capacity int NOT NULL
);
DESC room;
SELECT * FROM room;

CREATE TABLE reservation (
    reservation_id INT PRIMARY KEY,
    guest_id INT NOT NULL,
    roomType VARCHAR(20) NOT NULL,
    roomno INT NOT NULL,
    check_in DATE NOT NULL,
    check_out DATE NOT NULL,
    no_of_days INT,
    FOREIGN KEY (guest_id) REFERENCES guest(guest_id) ON DELETE CASCADE,
    FOREIGN KEY (roomno) REFERENCES room(roomno) ON DELETE CASCADE
);

DELIMITER //
CREATE TRIGGER calculate_days_insert BEFORE INSERT ON reservation
FOR EACH ROW
BEGIN
    SET NEW.no_of_days = DATEDIFF(NEW.check_out, NEW.check_in);
END;
//
CREATE TRIGGER calculate_days_update BEFORE UPDATE ON reservation
FOR EACH ROW
BEGIN
    SET NEW.no_of_days = DATEDIFF(NEW.check_out, NEW.check_in);
END;
//
DELIMITER ;

DESC reservation;
SELECT * FROM reservation;

CREATE TABLE restaurant (
	order_id int primary key,
    guest_id int not null,
    meal_category varchar(30) not null,
    amount int not null,
    foreign key (guest_id) references guest(guest_id) on delete cascade
);
DESC restaurant;
SELECT * FROM restaurant;


CREATE TABLE invoice (
    reservation_id INT PRIMARY KEY,
    guest_id INT,
    roomno INT,
    check_in DATE,
    check_out DATE,
    foodbill INT,
    roombill INT,
    total INT,
    FOREIGN KEY(reservation_id) references reservation(reservation_id) ON DELETE CASCADE,
    FOREIGN KEY (guest_id) REFERENCES guest(guest_id) ON DELETE CASCADE,
    FOREIGN KEY (roomno) REFERENCES room(roomno) ON DELETE CASCADE
);

DELIMITER //
CREATE TRIGGER calculate_total_bill BEFORE INSERT ON invoice
FOR EACH ROW
BEGIN
    SET NEW.total = NEW.foodbill + NEW.roombill;
END;
//
DELIMITER ;

DESC invoice;
SELECT * FROM invoice;



CREATE VIEW details AS(
	SELECT I.reservation_id,I.guest_id,C.guest_name,I.total 
    FROM invoice I, guest C
    WHERE I.guest_id=C.guest_id
);

select * from details;

