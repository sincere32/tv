CREATE USER tv WITH PASSWORD 'tvtvtvtv';
CREATE DATABASE tv WITH OWNER tv;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO tv;
