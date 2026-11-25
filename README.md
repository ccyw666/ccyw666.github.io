
# Python 
程序设计实验博客合集

> 课程实验记录：从基础语法容器、文本分词词云，到 FastAPI 接口、数据看板与字符界面绘制，配套可运行源码、测试用例与复盘博客。

## 技术栈

Python 3.10+ · pandas · jieba · wordcloud · matplotlib · plotly · Streamlit · FastAPI · pytest

## 实验目录

| 序号 | 实验主题 | 关键技术 | 工程目录 | 博客 |
| --- | --- | --- | --- | --- |
| 1 | Vibe Coding：Excel 报表脚本 + FastAPI 记账接口 | requests/pandas、FastAPI、pydantic、pytest | `vibe_lab1/` | `vibe_lab1/blog.md` |
| 2 | 数据看板的设计与实现 | Streamlit、Pandas、Plotly、筛选联动 | `dashboard_lab2/` | `dashboard_lab2/blog.md` |
| 3 | Python 列表、元组、集合 | 切片删除、可哈希判定、集合运算、保序去重 | `lab3_containers/` | `lab3_containers/blog.md` |
| 4 | 本地文档智能审查与摘要 Agent | jieba 分词、停用词/自定义词典、词云生成 | `doc_agent_lab4/` | `doc_agent_lab4/blog.md` |
| 5 | 十五五规划报告热词频率统计 | jieba 词频统计、政策术语词典、词云可视化 | `fyp_keywords/` | `fyp_keywords/blog.md` |
| 6 | 字符田字格绘制 | Unicode 框线字符、字符串拼接、二维布局 | `grid_draw/` | `grid_draw/blog.md` |

## 各实验概览

### 1. Vibe Coding 实操：报表脚本 + 记账接口
- **考题一**：读取脏数据销售表，清洗去重后按销售员/地区/总额统计，输出含四个工作表的 `report.xlsx`；
- **考题二**：FastAPI 记账服务，支持新增流水、多条件筛选分页、区间汇总，参数非法返回 4xx 结构化错误；
- 交付：需求澄清清单、源码、测试用例、AI 协作过程记录、复盘。

### 2. 数据看板设计与实现
- 电商销售场景，四大模块：KPI 概览卡片、地区柱状图 + 品类环形图、月度趋势折线图、明细表格；
- 侧边栏地区/品类/月份筛选，所有图表与明细表联动更新；
- 数据清洗：去空值、剔异常、去重，输出 CSV 报告。

### 3. 列表、元组、集合
- 切片删除索引逻辑与遍历删除漏删 bug 分析；
- 元组/列表/frozenset/普通 set 可哈希判定；
- 集合交并差对称差运算、无序去重与保序去重对比；
- 选课编号综合统计（交集、对称差、差集、转元组）与嵌套列表去重。

### 4. 本地文档智能审查与摘要 Agent
- 批量读取本地文档，文本清洗 → 自定义词典 → jieba 精确分词 → 过滤停用词 → 词频统计；
- 输出 Top50 词云 PNG 与关键词汇总 CSV；
- 含目录/文件缺失、编码错误、空数据等异常兜底。

### 5. 十五五规划热词频率统计
- 基于规划建议原文，统计高频政策术语，输出 Top50 热词排行与词云；
- 自定义政策词典保证「新质生产力」「高质量发展」「关键核心技术」等成词；
- 高频词解读：发展质量、科技自立、绿色低碳、改革与安全四条主线。

### 6. 字符田字格绘制
- 用 Unicode 框线字符在控制台拼出田字格外框与内部十字；
- 支持四格填字符、内容居中、超长截断；
- 扩展为多行多列田字格矩阵。

## 环境准备

```bash
# 通用基础库（按各实验 requirements.txt 安装）
pip install pandas jieba wordcloud matplotlib numpy pillow
pip install streamlit plotly fastapi uvicorn pytest
```

## 运行方式

每个工程目录下独立运行，以实验 1 为例：

```bash
cd vibe_lab1
python excel_report.py sales_raw.xlsx report.xlsx   # 报表脚本
uvicorn accounting_api:app --reload                  # 记账接口
python -m pytest test_lab1.py -v                     # 测试
```

数据看板：

```bash
cd dashboard_lab2
streamlit run app.py
```

分词/词云类实验：

```bash
cd doc_agent_lab4 && python doc_agent.py
cd fyp_keywords && python keyword_counter.py
```

## 测试说明

每个工程均附带 `test_*.py`，使用 pytest 覆盖正常路径与边界/异常用例：

```bash
python -m pytest test_*.py -v
```

## 目录结构总览

```
.
├── vibe_lab1/          # 实验1 报表脚本 + FastAPI 记账接口
├── dashboard_lab2/      # 实验2 Streamlit 数据看板
├── lab3_containers/    # 实验3 列表/元组/集合
├── doc_agent_lab4/     # 实验4 文档审查摘要 Agent
├── fyp_keywords/       # 实验5 规划热词频率统计
└── grid_draw/          # 实验6 字符田字格绘制
```

## 小结

这套实验覆盖了 Python 基础语法（容器、字符串）、数据处理（pandas 清洗统计）、文本分析（jieba 分词词云）、Web 服务（FastAPI）、可视化（Plotly/Streamlit）和测试验证（pytest）。每个工程遵循「需求澄清 → 分步实现 → 运行验证 → 复盘总结」的流程，博客文稿记录了思路、踩坑与改进方向。
```

直接复制上面代码块里的内容，粘贴到仓库根目录 `README.md` 即可。需要我再出一版带徽章（Python、pytest、Streamlit 图标）的 GitHub 风格版本吗？

