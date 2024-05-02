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
```
3.
SELECT * FROM member ORDER BY time DESC;
```
![Week5_3_3](https://github.com/Ro5555chenn/wehelpbootcamp5th/assets/156869378/b9cca0e1-b3de-4f27-9a91-12ebe276a21b)
```
4.
SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
```
![Week5_3_4](https://github.com/Ro5555chenn/wehelpbootcamp5th/assets/156869378/da7f15d2-620d-4a07-9d82-8ff0755d6d8a)
```
5. 
SELECT * FROM member WHERE username = 'test';
```
![Week5_3_5](https://github.com/Ro5555chenn/wehelpbootcamp5th/assets/156869378/3b35efd0-48dd-4549-98bc-1d5524b493b0)
```
6. 
SELECT * FROM member WHERE name LIKE '%es%';
```
![Week5_3_6](https://github.com/Ro5555chenn/wehelpbootcamp5th/assets/156869378/096a81d9-9585-48ab-9d03-b28a4bf0f391)
```
7. 
SELECT * FROM member WHERE username = 'test' AND password = 'test';
```
![Week5_3_7](https://github.com/Ro5555chenn/wehelpbootcamp5th/assets/156869378/f9794225-cf00-4f27-a98b-59905e3a35d8)
```
8. 
UPDATE member SET name = 'test2' WHERE username = 'test';
```
![Week5_3_8](https://github.com/Ro5555chenn/wehelpbootcamp5th/assets/156869378/d725751d-ea2a-4aae-a333-4de2281037b8)
```
Task4

1. 
SELECT COUNT(*) FROM member;
```
![Week5_4_1](https://github.com/Ro5555chenn/wehelpbootcamp5th/assets/156869378/0e94c9cc-d5b2-4f1b-b63f-041c5ec4e30e)
```
2. 
SELECT SUM(follower_count)  FROM member;
```
![Week5_4_2](https://github.com/Ro5555chenn/wehelpbootcamp5th/assets/156869378/3779ae76-8190-4315-8223-10ac88315983)
```
3. 
SELECT AVG(follower_count)  FROM member;
```
![Week5_4_3](https://github.com/Ro5555chenn/wehelpbootcamp5th/assets/156869378/dea8a192-33cd-4100-a25b-a7d943475023)
``` 
4. 
SELECT AVG(follower_count) 
FROM (
    SELECT follower_count
    FROM member
    ORDER BY follower_count DESC
    LIMIT 2
) AS top_2_followers;
```
![Week5_4_4](https://github.com/Ro5555chenn/wehelpbootcamp5th/assets/156869378/3e7e17f0-1afa-4f4f-839b-f5394e410e11)
```
Task5

1. 
CREATE TABLE message(
    id BIGINT AUTO_INCREMENT PRIMARY KEY  COMMENT ‘Unique ID',
    member_id BIGINT NOT NULL COMMENT ‘Member ID for Message Sender',
    content VARCHAR(255) NOT NULL COMMENT ‘Content',
    like_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT ‘Like Count',
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT ‘Publish Time',
    FOREIGN KEY (member_id) REFERENCES member(id) ON DELETE CASCADE
);

INSERT INTO message (member_id, content, like_count)
VALUES
(2, 'Hello from Ross!', 3),
(3, 'Bob checking in!', 5),
(4, 'It’s Angus. How’s everyone doing?', 4),
(5, 'Lily here, love this place!', 6),
(1, 'Test user saying hello!', 2);
```
![Week5_5_1](https://github.com/Ro5555chenn/wehelpbootcamp5th/assets/156869378/84936b67-2399-4d7a-9de3-527d6da9e364)
```
2.
SELECT message.id, message.content, member.name
FROM message
INNER JOIN member ON message.member_id = member.id;
```
![Week5_5_2](https://github.com/Ro5555chenn/wehelpbootcamp5th/assets/156869378/532b11ab-72e5-42b6-a535-114338c831f8)
```
3.
SELECT message.id, message.content, member.name
FROM message
INNER JOIN member ON message.member_id = member.id
WHERE member.username = 'test';
```
![Week5_5_3](https://github.com/Ro5555chenn/wehelpbootcamp5th/assets/156869378/7780794e-378b-4cd5-b50d-9e1489c78fb3)
```
4.
SELECT AVG(message.like_count)
FROM message
INNER JOIN member ON message.member_id = member.id
WHERE member.username = 'test';
```
![Week5_5_4](https://github.com/Ro5555chenn/wehelpbootcamp5th/assets/156869378/7980ddc5-ebcb-4adf-addb-6b320403ac22)
```
5. 
SELECT member.username, AVG(message.like_count) 
FROM message
INNER JOIN member ON message.member_id = member.id
GROUP BY member.username;
```
![Week5_5_5](https://github.com/Ro5555chenn/wehelpbootcamp5th/assets/156869378/d41e26cf-8145-406b-80d3-e05a6296674c)

















