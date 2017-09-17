CREATE USER 'matcha'@'localhost' IDENTIFIED BY 'matcha';

GRANT ALL PRIVILEGES ON *.* TO 'matcha'@'localhost';

FLUSH PRIVILEGES;

USE matcha;

CREATE TABLE locations (
		id INT NOT NULL AUTO_INCREMENT,
		longitude INT NOT NULL,
		latitude INT NOT NULL,
		name VARCHAR(64) NOT NULL,
		PRIMARY KEY (id)
);

CREATE TABLE users (
	id INT NOT NULL AUTO_INCREMENT,
	f_name VARCHAR(64),
	l_name VARCHAR(64),
	email VARCHAR(64) NOT NULL,
	age SMALLINT,
	gender CHAR(1),
	blurb VARCHAR(3000),
	location_id INT,
	age_range_min SMALLINT DEFAULT 18,
	age_range_max SMALLINT DEFAULT 117,
	sexual_preference CHAR(1) DEFAULT 'B',
	active INT DEFAULT 0,
	dt_joined DATETIME DEFAULT NOW(),
	PRIMARY KEY (id),
	FOREIGN KEY (location_id) REFERENCES locations(id)
);

CREATE TABLE shadow (
	id INT NOT NULL AUTO_INCREMENT,
	user_id INT NOT NULL,
	passwd CHAR(64),
	salt CHAR(32),
	PRIMARY KEY (id),
	FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE sessions (
	id INT NOT NULL AUTO_INCREMENT,
	user_id INT NOT NULL,
	hash CHAR(64) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE images (
	id INT NOT NULL AUTO_INCREMENT,
	profile_pic INT DEFAULT 0,
	user_id INT NOT NULL,
	filepath VARCHAR(96) NOT NULL,
	creation_dt DATETIME  NOT NULL DEFAULT NOW(),
	PRIMARY KEY (id),
	FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE likes (
	id INT NOT NULL AUTO_INCREMENT,
	user_id INT NOT NULL,
	liked_user_id INT NOT NULL,
	like_type CHAR(1) NOT NULL DEFAULT 'L',
	is_match INT NOT NULL DEFAULT 0,
	liked_dt DATETIME NOT NULL DEFAULT NOW(),
	PRIMARY KEY (id),
	UNIQUE(user_id, liked_user_id),
	FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
	FOREIGN KEY (liked_user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE messages (
	id INT NOT NULL AUTO_INCREMENT,
	sender_id INT NOT NULL,
	receiver_id INT NOT NULL,
	content VARCHAR(500),
	read INT NOT NULL DEFAULT 0,
	sent_dt DATETIME NOT NULL DEFAULT NOW(),
	PRIMARY KEY (id),
	FOREIGN KEY (sender_id) REFERENCES users(id) ON DELETE CASCADE,
	FOREIGN KEY (receiver_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE email_verification (
	id INT NOT NULL AUTO_INCREMENT,
	user_id INT NOT NULL,
	token VARCHAR(64),
	PRIMARY KEY (id),
	FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE interests (
		id INT NOT NULL AUTO_INCREMENT,
		label VARCHAR(64) NOT NULL,
		PRIMARY KEY (id)
);

CREATE TABLE user_interests (
		id INT NOT NULL AUTO_INCREMENT,
		user_id INT NOT NULL,
		interest_id INT NOT NULL,
		UNIQUE(user_id, interest_id),
		FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
		FOREIGN KEY (interest_id) REFERENCES interests(id) ON DELETE CASCADE
);
