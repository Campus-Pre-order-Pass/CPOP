---
id: server-mermaid
title: 流程圖
sidebar_label: 後端流程圖
sidebar_position: 1
---

```mermaid
graph TD;

subgraph Shop應用
    Shop模型 --> MenuItem模型
    Shop模型 --> Order模型
    Shop視圖 --> 顯示菜單項目視圖
    Shop視圖 --> 創建訂單視圖
end

subgraph MenuItem應用
    MenuItem模型 --> MenuItem視圖
end


```

```mermaid
graph TD;

subgraph Customer應用
    Customer模型 --> Customer視圖
end

subgraph Order應用
    Order模型 --> Order視圖
    Order視圖 --> 處理支付視圖
    Order視圖 --> 通知顧客視圖
end

subgraph Camera應用
    Camera模型 --> Camera控制器
end

subgraph Bot應用
    Bot模型 --> Bot控制器
end
```

# 交易系統後端應用介紹

## Shop 應用

Shop 應用包含了以下模型和視圖：

- **Shop 模型：** 商店資訊，與菜單項目模型和訂單模型有關聯。
- **MenuItem 模型：** 菜單項目資訊。
- **Order 模型：** 訂單資訊。

Shop 應用的視圖包括：

- **顯示菜單項目視圖：** 用於顯示商店的菜單項目。
- **創建訂單視圖：** 用於創建新的訂單。

## MenuItem 應用

MenuItem 應用包含了以下模型和視圖：

- **MenuItem 模型：** 菜單項目資訊。

MenuItem 應用的視圖包括：

- **MenuItem 視圖：** 用於顯示和處理菜單項目。

## Customer 應用

Customer 應用包含了以下模型和視圖：

- **Customer 模型：** 顧客資訊。

Customer 應用的視圖包括：

- **Customer 視圖：** 用於顯示和管理顧客資訊。

## Order 應用

Order 應用包含了以下模型和視圖：

- **Order 模型：** 訂單資訊。

Order 應用的視圖包括：

- **Order 視圖：** 用於顯示和管理訂單。
- **處理支付視圖：** 用於處理訂單支付。
- **通知顧客視圖：** 用於通知顧客訂單狀態。

## Camera 應用

Camera 應用包含了以下模型和控制器：

- **Camera 模型：** 相機資訊。
- **Camera 控制器：** 用於控制相機。

## Bot 應用

Bot 應用包含了以下模型和控制器：

- **Bot 模型：** 機器人資訊。
- **Bot 控制器：** 用於控制機器人。

這些應用之間建立了相應的模型和視圖，形成了一個完整的後端應用系統。
