# TaskFlow API

基于 FastAPI + SQLAlchemy 构建的带 JWT 鉴权、数据隔离与自动化测试的 RESTful API 服务。

## 🛠 技术栈
- **Web 框架**: FastAPI
- **ORM**: SQLAlchemy 2.0
- **数据库**: SQLite
- **鉴权**: PyJWT + Passlib (bcrypt)
- **测试**: Pytest + HTTPX
- **部署**: Docker

## ✨ 核心功能
- 用户注册与登录，密码使用 bcrypt 哈希加密存储。
- 基于 JWT 的身份验证与接口保护。
- 任务的完整 CRUD（创建、查询、更新、删除）。
- **数据隔离**：用户只能操作自己的任务，防止水平越权。
- 覆盖核心逻辑的单元测试。

## 🚀 快速开始

1. 安装依赖：
   ```bash
   pip install -r requirements.txt