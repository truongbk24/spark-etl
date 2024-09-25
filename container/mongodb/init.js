// Replace 'mydatabase' with your database name
db = db.getSiblingDB('crm');

// Create a collection named 'mycollection'
db.createCollection('customer');
db.createCollection('transaction');