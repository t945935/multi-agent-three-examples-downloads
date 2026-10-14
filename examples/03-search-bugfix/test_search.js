"use strict";

const assert = require("node:assert/strict");
const { searchItems } = require("./search.js");

const items = [
  { title: "Python 入門" },
  { title: "台南旅行" },
];

assert.deepEqual(searchItems("python", items), [{ title: "Python 入門" }]);
assert.deepEqual(searchItems("   ", items), []);
assert.deepEqual(searchItems("", items), []);
assert.deepEqual(searchItems("不存在", items), []);
assert.deepEqual(searchItems(null, items), []);

console.log("5 個搜尋情境全部通過");
