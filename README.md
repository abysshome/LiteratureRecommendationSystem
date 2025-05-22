# 科技文献推荐系统 (Literature Recommendation System)

## 项目介绍

科技文献推荐系统是一个基于Django开发的Web应用，旨在为用户提供个性化的科技文献推荐服务。系统利用向量嵌入技术和相似度计算，根据用户的兴趣和历史行为，推荐相关的科技文献，提高用户获取专业知识的效率。

## 功能特点

- **个性化推荐**：基于用户向量和文章向量的相似度，为用户提供个性化的文献推荐
- **用户管理**：完整的用户注册、登录、权限管理功能
- **文献检索**：支持按关键词、作者、标题等多维度检索文献
- **数据可视化**：提供文献阅读统计、热门文献排行等数据可视化功能
- **响应式界面**：适配多种设备，提供良好的用户体验

## 技术架构

### 后端技术

- **Web框架**：Django 4.2.9
- **数据库**：MySQL
- **向量检索**：FAISS (Facebook AI Similarity Search)
- **深度学习**：PyTorch

### 前端技术

- **页面渲染**：Django模板系统
- **UI组件**：Bootstrap
- **交互效果**：JavaScript/jQuery
- **数据可视化**：Highcharts

## 系统架构

系统主要由以下几个模块组成：

1. **用户管理模块**：负责用户的注册、登录、权限控制等功能
2. **文献数据模块**：管理文献的元数据，包括标题、摘要、关键词、作者等信息
3. **推荐引擎模块**：基于向量嵌入的推荐算法，计算用户与文献的相似度
4. **搜索模块**：提供多维度的文献检索功能
5. **数据可视化模块**：展示用户行为和文献统计数据

## 安装部署

### 环境要求

- Python 3.8+
- MySQL 5.7+
- 推荐使用虚拟环境

### 安装步骤

1. **克隆代码库**

   ```bash
   git clone https://github.com/yourusername/LiteratureRecommendationSystem.git
   cd LiteratureRecommendationSystem
   ```

2. **创建并激活虚拟环境**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # 或
   venv\Scripts\activate  # Windows
   ```

3. **安装依赖**

   ```bash
   pip install -r requirements.txt
   ```

4. **配置数据库**

   在 `system/settings.py` 中配置数据库连接信息：

   ```python
   DATABASES = {
       "default": {
           "ENGINE": "django.db.backends.mysql",
           "NAME": '文献推荐系统',  # 数据库名称
           "USER": "root",
           "PASSWORD": "your_password",
           "HOST": "127.0.0.1",
           "PORT": 3306,
       }
   }
   ```

5. **创建数据库**

   ```sql
   create database 文献推荐系统 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
   ```

6. **迁移数据库**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **创建超级用户**

   ```bash
   python manage.py createsuperuser
   ```

8. **启动服务**

   ```bash
   python manage.py runserver
   ```

   访问 http://127.0.0.1:8000 即可使用系统

## 推荐引擎配置

推荐引擎基于用户和文章的向量嵌入，需要配置以下文件：

- `deploy/article_embeddings_200.pt`：文章向量嵌入文件
- `deploy/user_embeddings_200.pt`：用户向量嵌入文件
- `deploy/articles.csv`：文章元数据文件

## 使用说明

### 管理员功能

1. 访问 `/admin` 进入管理后台
2. 可以管理用户、文献数据、系统设置等

### 用户功能

1. 注册/登录：新用户需要先注册账号
2. 个人中心：查看个人信息、阅读历史等
3. 文献推荐：系统会根据用户兴趣自动推荐相关文献
4. 文献搜索：可以按关键词、作者等搜索文献
5. 数据统计：查看个人阅读统计和系统热门文献

## 开发指南

### 项目结构

- `app01/`：主应用目录
  - `models.py`：数据模型定义
  - `views/`：视图函数
  - `templates/`：HTML模板
  - `static/`：静态资源
  - `utils/`：工具函数
- `deploy/`：推荐引擎部署相关文件
- `system/`：项目配置文件

### 推荐算法

系统使用基于向量嵌入的推荐算法，主要流程如下：

1. 为每篇文章和每个用户生成特征向量
2. 使用FAISS计算用户向量与文章向量的相似度
3. 返回相似度最高的文章作为推荐结果

## 贡献指南

欢迎贡献代码或提出建议，请遵循以下步骤：

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 许可证

本项目采用 MIT 许可证 - 详情请参阅 [LICENSE](LICENSE) 文件

## 联系方式

如有任何问题或建议，请联系项目维护者：

- 邮箱：your.email@example.com
- GitHub Issues：[提交问题](https://github.com/yourusername/LiteratureRecommendationSystem/issues)
