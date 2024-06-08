# Feedback Commons

**反馈通用工具库**

## 目录
- [简介](#简介)
- [安装](#安装)
- [使用](#使用)
  - [API 客户端](#api-客户端)
  - [数据清洗工具](#数据清洗工具)
  - [文件解析工具](#文件解析工具)
  - [模型定义](#模型定义)
  - [异步任务](#异步任务)
- [贡献](#贡献)
- [许可证](#许可证)

## 简介

Feedback Commons 是一个通用工具库，旨在支持企业级 AI 驱动的智能反馈系统的开发。该库包含多种实用工具，如 API 客户端、数据清洗、文件解析、模型定义和异步任务处理。

## 目录

```bash
feedback-commons/
|-- .github/
├── docs/
│   ├── API.md
│   ├── DATA.md
│   └── README.md
├── src/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── openai_client.py
│   │   └── ...
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── data_cleaning.py
│   │   ├── file_parser.py
│   │   └── ...
│   ├── models/
│   │   ├── __init__.py
│   │   ├── feedback.py
│   │   └── ...
│   └── tasks/
│       ├── __init__.py
│       ├── async_tasks.py
│       └── ...
├── tests/
│   ├── test_api.py
│   ├── test_utils.py
│   └── ...
├── requirements.txt
└── setup.py
```

## 安装

```bash
pip install -r requirements.txt
python setup.py install
```

## 使用

### API 客户端

该模块提供与 OpenAI API 的集成，方便调用大语言模型进行数据处理。

#### 示例代码

```python
from feedback_commons.api.openai_client import OpenAIClient

client = OpenAIClient(api_key='your_api_key')
response = client.get_response(prompt="Summarize the following feedback...")
print(response)
```

### 数据清洗工具

提供数据清洗和预处理功能，包括格式转换、缺失值处理等。

#### 示例代码

```python
from feedback_commons.utils.data_cleaning import clean_data

data = {"field1": "value1", "field2": None}
cleaned_data = clean_data(data)
print(cleaned_data)
```

### 文件解析工具

支持多种文件格式的解析，如 Excel、JSON、YAML 等。

#### 示例代码

```python
from feedback_commons.utils.file_parser import parse_excel

data = parse_excel('path/to/file.xlsx')
print(data)
```

### 模型定义

定义反馈系统的数据模型，包括用户、问题、反馈、标签等。

#### 示例代码

```python
from feedback_commons.models.feedback import Feedback

feedback = Feedback(user_id=1, question_id=1, feedback_text="Great product!", score=4.5)
print(feedback)
```

### 异步任务

使用 Celery 实现异步任务处理，提高数据处理性能。

#### 示例代码

```python
from feedback_commons.tasks.async_tasks import process_feedback

task = process_feedback.delay(feedback_data)
print(task.id)
```

## 贡献

欢迎对 Feedback Commons 做出贡献！请阅读 [贡献指南](docs/CONTRIBUTING.md) 了解详细信息。

## 许可证

Feedback Commons 使用 MIT 许可证。详情请参阅 [LICENSE](LICENSE) 文件。
```

### 工具模块概述

1. **API 客户端**：
   - `openai_client.py`：封装与 OpenAI API 的交互，简化调用过程。

2. **数据清洗工具**：
   - `data_cleaning.py`：提供数据清洗函数，如处理缺失值、数据标准化等。

3. **文件解析工具**：
   - `file_parser.py`：支持 Excel、JSON、YAML 等文件格式的解析和转换。

4. **模型定义**：
   - `feedback.py`：定义反馈系统的数据模型，如用户、问题、反馈、标签等。

5. **异步任务**：
   - `async_tasks.py`：使用 Celery 实现异步任务处理，包括数据评分和分类等任务。
