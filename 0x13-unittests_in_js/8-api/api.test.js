const chai = require('chai');
const chaiHttp = require('chai-http');

chai.use(chaiHttp);

describe('express app GET / req', () => {
  it('/ correct status, result', () => {
    chai.request('http://localhost:7865')
      .get('/')
      .end((err, res) => {
        if (err) throw err;
        chai.expect(res.statusCode).to.eql(200);
        chai.expect(res.text).to.eql('Welcome to the payment system');
      })
  })
})