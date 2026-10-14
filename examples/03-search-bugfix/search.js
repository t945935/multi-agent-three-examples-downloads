"use strict";

/**
 * 搜尋資料；空字串與只有空白時回傳空結果，不拋出例外。
 * 實際網站可在呼叫端將結果渲染到頁面。
 */
function searchItems(query, items) {
  const keyword = typeof query === "string" ? query.trim().toLowerCase() : "";
  if (keyword === "") return [];

  return items.filter((item) =>
    String(item.title).toLowerCase().includes(keyword),
  );
}

if (typeof module !== "undefined") {
  module.exports = { searchItems };
}
