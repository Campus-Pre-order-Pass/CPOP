import React from "react";

// 定义英文到中文的映射
const typeMapping: { [key: string]: string } = {
  staples: "主食",
  bento: "便當",
  beverages: "飲料",
  other: "其他",
};

// 创建翻译函数
function translateTypeToChinese(englishType: string): string {
  return typeMapping[englishType] || englishType;
}

export default translateTypeToChinese;
