import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const app = express();
const clientGet = promisify(client.get).bind(client);
const clientSet = promisify(client.set).bind(client);

const listProducts = [
  { Id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { Id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { Id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { Id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
]
const getItemById = (id) => {
  for (const list of listProducts) {
    if (list['Id'] === id) return list;
  }
}

const reserveStockById = async (itemId, stock) => {
  await clientSet(itemId, stock);
}

const getCurrentReservedStockById = async (itemId) => {
  await clientGet(itemId);

}
app.get('/list_products', (req, res) => res.send(JSON.stringify(listProducts)));
app.get('/list_products/:itemId', async (req, res) => {
  const id = Number(req.params.itemId);
  const item = getItemById(id);
  if (item) {
    item.currentQuantity = await getCurrentReservedStockById(id);
    res.send(JSON.stringify(item));
  }
  res.status(404).send(JSON.stringify({"status":"Product not found"}));
});

app.get('/reserve_product/:itemId', async (req, res) => {
    const id = Number(req.params.itemId);
    const item = getItemById(id);
    if (!item) {
        res.status(403).send(JSON.stringify({"status":"Product not found"}));
    }
    const stock = await getCurrentReservedStockById(id);
    console.log(stock);
    if (stock === 0) {
      res.status(403).send(JSON.stringify({"status":"Not enough stock available","itemId":`${id}`}));
    }
    console.log(stock);
    async () => await reserveStockById(id, stock);
    res.send(JSON.stringify({"status":"Reservation confirmed","itemId":`${id}`}));
});
app.listen(1245);
