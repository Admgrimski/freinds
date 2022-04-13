-- TJ - Friends Datbase Setup for Profolio Page
-- Run cat friends_database_setup.sql | docker exec -i pg_container psql
-- to create the database in use classes virutal enviroment

-- kill other connections
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'friendsdb' AND pid <> pg_backend_pid();
-- (re)create the database
DROP DATABASE IF EXISTS friendsdb;
CREATE DATABASE friendsdb;
-- connect via psql
\c friendsdb

-- database configuration
SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET default_tablespace = '';
SET default_with_oids = false;

---
--- CREATE tables
---

CREATE TABLE friends (
    id SERIAL,
    username
    password
    email
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    display_name TEXT NOT NULL,
    active BOOLEAN NOT NULL,
    PRIMARY KEY (id)
);
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(16), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    first_name = db.Column(db.String(50), unique=False, nullable=True, default='first name')
    last_name = db.Column(db.String(50), unique=False, nullable=True, default='last name')
    friend_image = db.Column(db.String(20), nullable=False, default='default.jpg')
    display_name = db.Column(db.String(30), unique=True, nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=True)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship('Posts', backref='friend', lazy=True)
 