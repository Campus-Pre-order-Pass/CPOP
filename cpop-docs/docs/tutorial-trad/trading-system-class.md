---
id: trading-system
title: 交易系統
sidebar_label: 交易系統
sidebar_position: 1
---

`/CPOP/server/order/core`

## 進入點

- **`TradingSystem` 類別：** 在交易系統中，TradingSystem 扮演著協調和管理各個模塊的角色，它是整個交易系統的進入點。TradingSystem 的主要職責包括初始化各個模塊、設定事件訂閱關係、載入配置文件、運行回測等。

```python

class TradingSystem(ABC):
    @abstractmethod
    def __init__(self):
        """
        抽象方法 - 初始化方法，負責建立交易系統的基本結構。
        """
        pass

    @abstractmethod
    def initialize(self):
        """
        抽象方法 - 初始化整個交易系統，包括各個模塊的建立和相關配置。
        """
        pass

    @abstractmethod
    def subscribe_events(self):
        """
        抽象方法 - 設定事件訂閱，建立模塊之間的通信機制。
        """
        pass

    @abstractmethod
    def load_configuration(self, config_file_path):
        """
        抽象方法 - 載入配置文件，確保交易系統參數和設定的正確性。

        :param config_file_path: 配置文件的路徑。
        """
        pass

    @abstractmethod
    def run_backtest(self, start_date, end_date):
        """
        抽象方法 - 運行回測，模擬交易策略在歷史數據上的表現。

        :param start_date: 回測起始日期。
        :param end_date: 回測結束日期。
        """
        pass
```

## 1. 交易策略模塊（Strategy Module）

- **`Strategy` 類別：** 定義交易策略的基本結構，包括信號生成和交易執行邏輯。
- **具體策略類別：** 擴展 `Strategy` 類別以實現不同的交易策略，例如均線策略、動能策略等。

## 2. 風險管理模塊（Risk Management Module）

- **`RiskManager` 類別：** 管理交易風險的模塊，包括止損、止盈等風險控制。
- **風險參數：** 定義風險控制的參數，例如最大風險金額、最大損失百分比等。

```python

class RiskManager(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def manage_risk(self, trade):
        pass

```

## 3. 執行模塊（Execution Module）

- **`ExecutionSystem` 類別：** 處理實際的交易執行，包括發送訂單到市場、監控執行狀態等。
- **交易訂單類別：** 定義交易訂單的屬性，例如股票代碼、數量、價格等。

```python

class ExecutionSystem(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def execute_order(self, order):
        pass
```

## 4. 數據模塊（Data Module）

- **`DataManager` 類別：** 獲取、處理和存儲市場數據的模塊。
- **數據源接口：** 定義獲取數據的接口，可以是歷史數據、實時數據等。

```python

class DataManager(ABC):
    @abstractmethod
    def __init__(self, mock_path:str):
        pass

    @abstractmethod
    def fetch_market_data(self):
        pass

    @abstractmethod
    def fetch_test_send_data(self):
        pass

    @abstractmethod
    def fetch_test_result_data(self):
        pass
```

## 5. 回測模塊（Backtesting Module）

- **`Backtester` 類別：** 提供回測框架，模擬過去交易策略的表現。
- **績效評估：** 計算回測結果的指標，例如收益率、最大回撤等。

## 6. 事件管理模塊（Event Management Module）

- **事件驅動：** 使用事件驅動的方式來協調不同模塊之間的通信，例如市場數據更新、訂單執行等。

## 7. 帳戶模塊（Account Module）

- **`Account` 類別：** 管理帳戶的狀態，包括餘額、持倉、交易歷史等。
- **帳戶狀態更新：** 當有新的交易或者執行事件發生時，更新帳戶狀態。

```python

class Account(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def update_account_status(self, trade):
        pass
```

## 8. 日誌和監控模塊（Logging and Monitoring Module）

- **`Logger` 類別：** 記錄系統運行日誌，方便排查問題和分析。
- **監控：** 監控系統運行狀態，檢測潛在的錯誤或問題。

## 9. 配置模塊（Configuration Module）

- **配置文件：** 使用配置文件來管理策略、風險控制和系統參數的設置。
  ConditionsModule

## 10. 配置模塊（Conditions Module）

- **`ConditionsModule` 類別：** 當配置相關錯誤發生時引發的錯誤類別。
- **衍生類別：**`TradeError`,`ConfigurationModule`

## 11. 錯誤配置

- **`ConfigurationError` 類別：** 當配置相關錯誤發生時引發的錯誤類別。
- **衍生類別：**`TradeError`,`ConfigurationModule`
