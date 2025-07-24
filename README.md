# Anthropic 提示工程交互式教程 - 中文汉化版

欢迎来到 Anthropic 提示工程交互式教程的中文汉化版本！

## 📖 项目简介

本项目是 **Anthropic 官方提示工程交互式教程** 的中文汉化版本，专门为中国用户优化。我不仅将原版英文教程翻译成中文，还对大模型调用接口进行了适配：

### 🔧 主要改进

1. **接口标准化**: 将原版教程中的 Anthropic Claude API 调用接口修改为 **OpenAI 规范**，使其与更多大模型平台兼容
2. **中文本地化**: 完整翻译所有教程内容、示例和说明文档
3. **提示词案例优化**：对于某些提示词案例进行了优化，以保证更好的学习演示效果
4. **平台兼容性**: 支持阿里云、腾讯云、硅基流动等主流大模型服务平台
5. **模型灵活性**: 支持多种大模型，包括 Qwen、ChatGLM、Baichuan 等

## 🎯 课程目标

完成本课程后，您将能够：

- **掌握优秀提示词的基本结构**
- **识别常见失败模式**并学习解决它们的"80/20"技巧
- **理解大模型的优势和局限性**
- **从零开始为常见用例构建强大的提示词**

## 📚 课程结构与内容

本课程专为让您有充分机会练习编写和调试提示词而设计。课程分为 9 个章节，每章都配有相应的练习，以及一个包含更高级方法的附录。建议按章节顺序学习。

每个课程都有底部的"示例练习区"，您可以自由实验课程中的示例，亲眼看到改变提示词如何改变模型的响应。同时提供答案参考。

### 📋 目录结构

#### 初级篇
- **第1章**: 基础提示结构
- **第2章**: 清晰和直接
- **第3章**: 分配角色（角色提示）

#### 中级篇
- **第4章**: 分离数据和指令
- **第5章**: 格式化输出和为模型代言
- **第6章**: 预知（逐步思考）
- **第7章**: 使用示例（少样本提示）

#### 高级篇
- **第8章**: 避免幻觉
- **第9章**: 从零开始构建复杂提示词
  - 聊天机器人复杂提示词
  - 法律服务复杂提示词
  - 练习：金融服务复杂提示词
  - 练习：编程复杂提示词

#### 附录篇
- **附录A**: 提示词链接
- **附录B**: 工具使用
- **附录C**: 搜索和检索

## 🚀 快速开始

### 环境要求

- Python 3.7+
- Jupyter Notebook 或 JupyterLab
- 大模型 API 密钥

### 安装步骤

1. **克隆代码库**
   ```bash
   git clone git@github.com:zaihanLit/prompt-chn-interactive-tutorial.git
   cd prompt-chn-interactive-tutorial
   ```

2. **安装依赖**
   ```bash
   pip install openai pickleshare jupyter
   ```

3. **配置 API 密钥**
   
   在 `courses/00_教程使用指南.ipynb` 中设置您的 API 配置：
   ```python
   API_KEY = "your_api_key_here"
   MODEL_NAME = "Qwen/Qwen2.5-14B-Instruct"  # 或其他支持的模型
   BASE_URL = "https://api.siliconflow.cn/v1/"  # 或其他平台地址
   ```

4. **开始学习**
   
   按顺序打开并运行 `courses/` 目录下的 Jupyter Notebook 文件：
   - `00_教程使用指南.ipynb` - 首先阅读
   - `01_基础提示结构.ipynb` - 开始学习
   - 继续按编号顺序学习其他章节

## 🔑 支持的模型平台

本教程已适配以下大模型平台：

- **硅基流动** (SiliconFlow)
- **阿里云** (Alibaba Cloud)
- **腾讯云** (Tencent Cloud)
- **百度智能云** (Baidu Cloud)
- **其他兼容 OpenAI API 规范的平台**

### 推荐模型

- Qwen/Qwen2.5-14B-Instruct （经测试该模型能取得较好的示例效果）
- 其他兼容的大语言模型

## 💡 使用技巧

- **温度设置**: 本课程使用 temperature=0，产生更确定性的结果
- **快捷键**: 使用 `Shift + Enter` 执行单元格并移动到下一个
- **顺序学习**: 建议按章节编号顺序学习，确保基础概念掌握后再进入高级内容
- **实践练习**: 每个章节都包含练习区域，建议完成所有练习以巩固学习效果

## 🔧 技术实现

### API 调用示例

```python
from openai import OpenAI

client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)

def get_completion(prompt: str):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        max_tokens=2000,
        temperature=0.0,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
```

## 📝 原版说明

本教程基于 Anthropic 官方教程，原版使用 Claude 3 Haiku 模型。Anthropic 还有 Claude 3 Sonnet 和 Claude 3 Opus 两个更智能的模型，其中 Opus 是最智能的。

原版教程也存在于 Google Sheets 中，使用 Anthropic 的 Claude for Sheets 扩展。我们推荐使用这个 Jupyter Notebook 版本，因为它更适合编程学习和实验。

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request 来改进这个中文教程！

- 报告翻译错误或改进建议
- 添加新的示例和练习
- 优化代码实现
- 更新文档内容

## 📄 许可证

本项目基于原版 Anthropic 教程，遵循相应的开源许可证。

## 🙏 致谢

- 感谢 Anthropic 团队创建了优秀的原版教程


---

**准备好开始了吗？请前往 `courses/01_基础提示结构.ipynb` 开始您的提示工程学习之旅！** 