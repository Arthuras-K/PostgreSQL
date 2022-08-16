CREATE TABLE IF NOT exists employee (
  id SERIAL PRIMARY KEY,
  department VARCHAR(60),
  boss_id INTEGER NOT NULL REFERENCES employee(id) 
);