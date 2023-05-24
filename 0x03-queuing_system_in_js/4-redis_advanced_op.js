import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

client.hset('HolbertonSchools', 'Portland', 50, (err, res) => {
  if (err) {
    console.error(err);
  } else {
    redis.print('Reply: 1');
  }
});

client.hset('HolbertonSchools', 'Seattle', 80, (err, res) => {
  if (err) {
    console.error(err);
  } else {
    redis.print('Reply: 1');
  }
});

client.hset('HolbertonSchools', 'New York', 20, (err, res) => {
  if (err) {
    console.error(err);
  } else {
    redis.print('Reply: 1');
  }
});

client.hset('HolbertonSchools', 'Bogota', 20, (err, res) => {
  if (err) {
    console.error(err);
  } else {
    redis.print('Reply: 1');
  }
});

client.hset('HolbertonSchools', 'Cali', 40, (err, res) => {
  if (err) {
    console.error(err);
  } else {
    redis.print('Reply: 1');
  }
});

client.hset('HolbertonSchools', 'Paris', 2, (err, res) => {
  if (err) {
    console.error(err);
  } else {
    redis.print('Reply: 1');
  }
});

client.hgetall('HolbertonSchools', (err, res) => {
  if (err) {
    console.error(err);
  } else {
    console.log(res);
  }
});
