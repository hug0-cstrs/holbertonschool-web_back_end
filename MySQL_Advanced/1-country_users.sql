-- Create a table users with the following requirements:
-- id: INT NOT NULL AUTO_INCREMENT PRIMARY KEY - a unique ID for each user
-- email: VARCHAR(255) NOT NULL UNIQUE - the email of the user
-- name: VARCHAR(255) - the name of the user
-- country: ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US' - the country of the user, default is US
CREATE TABLE IF NOT EXISTS users (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255),
  country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
)
