CREATE TYPE TaskStatus AS ENUM ('TODO', 'IN_PROGRESS', 'DONE');

CREATE TABLE Task (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    status TaskStatus NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

