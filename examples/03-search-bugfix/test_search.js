"use strict";

const assert = require("node:assert/strict");

// 可指定模組路徑；預設驗證修復版本。
const modulePath = process.argv[2] || "./search.js";
const { searchItems } = require(modulePath);

const items = [
  { title: "Python 入門" },
  { title: "台南旅行" },
];

// [回歸檢查] 空白輸入必須回傳空陣列，不可拋出例外。
assert.doesNotThrow(
  () => assert.deepEqual(searchItems("   ", items), []),
  "whitespace query failed: expected [] without throwing",
);

assert.deepEqual(searchItems("python", items), [{ title: "Python 入門" }]);
assert.deepEqual(searchItems("   ", items), []);
assert.deepEqual(searchItems("", items), []);
assert.deepEqual(searchItems("不存在", items), []);
assert.deepEqual(searchItems(null, items), []);

console.log("5 個搜尋情境全部通過");
