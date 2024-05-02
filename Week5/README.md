```
Task2

CREATE TABLE member (
    id BIGINT AUTO_INCREMENT PRIMARY KEY COMMENT 'unique_id',
    name VARCHAR(255) NOT NULL COMMENT 'Name',
    username VARCHAR(255) NOT NULL COMMENT 'Username',
    password VARCHAR(255) NOT NULL COMMENT 'Password',
    follower_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Follower Count',
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Signup Time'
);

```
![Week5_2](https://github.com/Ro5555chenn/wehelpbootcamp5th/assets/156869378/7638618b-80d0-420f-b3fa-8ef84f1a05aa)
