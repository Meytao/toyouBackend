# ToyouBackend后端

## 项目结构

```text
toyouBackend/
├── main.py               ← FastAPI 应用入口
├── test_main.http        ← IDEA/PyCharm HTTP Client 测试文件
│
├── .env.dev              ← 开发环境变量
├── .env.prod             ← 生产环境变量
├── .gitignore            ← Git 忽略规则
│
├── .venv/                ← Python 虚拟环境
├── .idea/                ← PyCharm 配置
├── __pycache__/          ← Python 编译产物
│
├── app/                  ← 业务代码主体
│   ├── api/              接口路由层
│   ├── config/           配置层
│   ├── dao/              数据访问对象
│   ├── models/           ORM 模型层
│   ├── schemas/          Pydantic 数据契约
│   ├── services/         业务逻辑层
│   └── utils/            工具与基础设施
```

# 子模块职责

```text
   api  →  services  →  dao  →  models  →  MySQL
   ↓          ↓          ↓
schemas    utils       utils

```

| 目录             | 职责                                            |
|----------------|-----------------------------------------------|
| `app/api`      | 路由层：定义 URL、接收请求、调用 service、返回响应               |
| `app/services` | 业务逻辑层：处理“业务规则”，比如权限校验、流程编排、跨表操作               |
| `app/dao`      | 数据访问层：封装对 ORM 的 CRUD，只跟数据库打交道，不掺业务            |
| `app/models`   | ORM 模型：每个 `.py` 对应数据库一张表的结构                   |
| `app/schemas`  | Pydantic 校验/序列化模型：请求体 / 响应体 / 内部 DTO 的字段定义与验证 |
| `app/utils`    | 横切关注点工具：与具体业务无关的“通用件”                         |
| `app/config`   | 应用配置层：读取环境变量、构造数据库引擎 / Session                |