-- Plant Intelligence Device Database Schema

-- Users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Plants table
CREATE TABLE plants (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    name VARCHAR(255) NOT NULL,
    species VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Sensor data table
CREATE TABLE sensor_data (
    id SERIAL PRIMARY KEY,
    plant_id INTEGER NOT NULL,
    temperature FLOAT,
    humidity FLOAT,
    soil_moisture FLOAT,
    light_level FLOAT,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (plant_id) REFERENCES plants(id)
);

-- Care recommendations table
CREATE TABLE care_recommendations (
    id SERIAL PRIMARY KEY,
    plant_id INTEGER NOT NULL,
    recommendation TEXT,
    priority VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (plant_id) REFERENCES plants(id)
);
