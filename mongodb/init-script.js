var conn = new Mongo();

var db = conn.getDB('db');

db.createCollection('templates');