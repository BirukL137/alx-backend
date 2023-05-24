import redis from 'redis';

const client = redis.createClient();
const promisify = require('util').promisify;

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, (reject, resolve) => {
    redis.print("Reply: OK ", resolve);
  });
};

const displaySchoolValue = async (schoolName) => {
  const value = await (promisify(client.get).bind(client))(schoolName);
  console.log(value);
  };
  
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
