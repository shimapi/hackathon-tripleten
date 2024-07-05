const { createProxyMiddleware } = require('http-proxy-middleware');
const path = require('path');
const express = require('express');
const fs = require('fs');

module.exports = function (app) {
  app.use(
    '/json',
    (req, res, next) => {
      const filePath = path.join(__dirname, '..', 'notebook', 'json', req.path);
      fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
          res.status(404).send('File not found');
        } else {
          res.json(JSON.parse(data));
        }
      });
    }
  );
};
