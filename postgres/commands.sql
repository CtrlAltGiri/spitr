CREATE TABLE users (
  username VARCHAR(50) PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  displayname VARCHAR(50) NOT NULL,
  phone VARCHAR(20)
);