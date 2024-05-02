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

```
Task3

1.
INSERT INTO member (name, username, password) VALUES ('test', 'test', 'test');

INSERT INTO member (name, username, password, follower_count)
VALUES 
    ('Ross', 'Ro5555', 'ro5555',100),
    ('Bob', 'Bo6666', 'bo6666',211),
    ('Angus', 'Angus88330', 'angus88330',985),
    ('Lily', 'Lily7777', 'lily7777',347);
```
```
2.
SELECT * FROM member;
```
![Week5_3_2](https://github.com/Ro5555chenn/wehelpbootcamp5th/assets/156869378/6a576d58-4e32-42e9-ac24-5d6432750deb)






