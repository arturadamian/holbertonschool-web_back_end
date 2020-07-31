import kue from 'kue';
import redis from 'redis';
import { promisify } from 'util';
import express from 'express';

const client = redis.createClient();
const queue = kue.createQueue();
const app = express();
const clientGet = promisify(client.get).bind(client);
const clientSet = promisify(client.set).bind(client);

const reserveSeat = async (number) =>  await clientSet('available_seats', number);
const getCurrentAvailableSeats = async () => await clientGet('available_seats');

let reservationEnabled = true;

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({numberOfAvailableSeats});
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) res.json({ "status": "Reservation are blocked" });
  const job = queue.create('reserve_seat', {}).save((err) => {
    if (err) res.json({ status: 'Reservation failed' });
    res.json({ status: 'Reservation in process' });
  });
  job.on('failed', (err) => console.log(`Seat reservation job ${job.id} failed: ${err}`));
  job.on('complete', () => console.log(`Seat reservation job ${newJob.id} completed`));
});

app.get('/process', (req, res) => {
    queue.process('reserve_seat', async (job, done) => {
      let availableSeats = await getCurrentAvailableSeats();
      if (availableSeats < 1) {
        done(Error('Not enough seats available'));
      } else {
        await reserveSeat(Number(availableSeats) - 1);
      };
      if ((Number(availableSeats) - 1) < 1) reservationEnabled = false;
      done();
    });
    res.json({ status: 'Queue processing' });
});

app.listen(1245, () => {
  reserveSeat(50);
  reservationEnabled = true;
});