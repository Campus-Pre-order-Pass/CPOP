# CPOP 高科美食通

CPOP 高科美食通是一個使用多種技術堆疊的專案，旨在提供高效且現代的美食通訊平台。

## 技術堆疊

- **Django**: 用於構建強大的後端服務，處理數據庫、業務邏輯等。
- **Redis**: 作為快取和消息代理，提升應用性能和可擴展性。
- **Docker**: 用於容器化應用程式，確保在不同環境中的一致性運行。
- **React**: 前端框架，用於構建交互式用戶界面。
- **Next.js**: React 框架的擴展，提供更好的服務端渲染和路由管理。

## 專案結構

### 1. `server` 資料夾

這個資料夾包含後端 Django 應用程式的源代碼。主要功能包括處理數據庫、業務邏輯和與前端的通信。

### 2. `redis` 資料夾

這個資料夾包含與 Redis 相關的配置文件和代碼。Redis 用作快取和消息代理，提升應用性能和可擴展性。

### 3. `Supplier-front` 資料夾

這個資料夾是管理頁面的前端應用程式。使用 React 和 Next.js 架構，提供現代化的用戶界面和良好的用戶體驗。

## 如何運行

### 透過 makefile

1. 啟動所有前端後端伺服器與建制

   ```bash
   make all
   ```

2. 啟動 server

   ```bash
   make runser
   ```

3. 啟動 docker gui 管理啟動

   ```bash
   make gui
   ```

### 後端 (Django + Redis)

1. 進入 `server` 目錄：

   ```bash
   cd server
   ```

2. 使用 Docker 構建後端映像：

   ```bash
   docker build -t cpop-server-image .
   ```

3. 運行 Docker 容器：

   ```bash
   docker run -p 8000:8000 cpop-server-image
   ```

### 前端 (React + Next.js)

1. 進入 `Supplier-front` 目錄：

   ```bash
   cd Supplier-front
   ```

2. 安裝相依套件：

   ```bash
   npm install
   ```

3. 啟動開發服務器：

   ```bash
   npm run dev
   ```

現在，你可以通過訪問 [http://localhost:8000](http://localhost:8000) 來查看你的應用程式。

### nwgsi

[https://github.com/twtrubiks/docker-django-nginx-uwsgi-postgres-tutorial]

請確保安裝了 Docker、Node.js 和相關套件，並按照上述步驟進行設置和運行。
