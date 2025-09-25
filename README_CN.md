<<<<<<< HEAD
# Dify on MySQL
=======
![cover-v5-optimized](./images/GitHub_README_if.png)

<div align="center">
  <a href="https://cloud.dify.ai">Dify 云服务</a> ·
  <a href="https://docs.dify.ai/getting-started/install-self-hosted">自托管</a> ·
  <a href="https://docs.dify.ai">文档</a> ·
  <a href="https://dify.ai/pricing">Dify 产品形态总览</a>
</div>

<p align="center">
    <a href="https://dify.ai" target="_blank">
        <img alt="Static Badge" src="https://img.shields.io/badge/Product-F04438"></a>
    <a href="https://dify.ai/pricing" target="_blank">
        <img alt="Static Badge" src="https://img.shields.io/badge/free-pricing?logo=free&color=%20%23155EEF&label=pricing&labelColor=%20%23528bff"></a>
    <a href="https://discord.gg/FngNHpbcY7" target="_blank">
        <img src="https://img.shields.io/discord/1082486657678311454?logo=discord&labelColor=%20%235462eb&logoColor=%20%23f5f5f5&color=%20%235462eb"
            alt="chat on Discord"></a>
    <a href="https://reddit.com/r/difyai" target="_blank">  
        <img src="https://img.shields.io/reddit/subreddit-subscribers/difyai?style=plastic&logo=reddit&label=r%2Fdifyai&labelColor=white"
            alt="join Reddit"></a>
    <a href="https://twitter.com/intent/follow?screen_name=dify_ai" target="_blank">
        <img src="https://img.shields.io/twitter/follow/dify_ai?logo=X&color=%20%23f5f5f5"
            alt="follow on X(Twitter)"></a>
    <a href="https://www.linkedin.com/company/langgenius/" target="_blank">
        <img src="https://custom-icon-badges.demolab.com/badge/LinkedIn-0A66C2?logo=linkedin-white&logoColor=fff"
            alt="follow on LinkedIn"></a>
    <a href="https://hub.docker.com/u/langgenius" target="_blank">
        <img alt="Docker Pulls" src="https://img.shields.io/docker/pulls/langgenius/dify-web?labelColor=%20%23FDB062&color=%20%23f79009"></a>
    <a href="https://github.com/langgenius/dify/graphs/commit-activity" target="_blank">
        <img alt="Commits last month" src="https://img.shields.io/github/commit-activity/m/langgenius/dify?labelColor=%20%2332b583&color=%20%2312b76a"></a>
    <a href="https://github.com/langgenius/dify/" target="_blank">
        <img alt="Issues closed" src="https://img.shields.io/github/issues-search?query=repo%3Alanggenius%2Fdify%20is%3Aclosed&label=issues%20closed&labelColor=%20%237d89b0&color=%20%235d6b98"></a>
    <a href="https://github.com/langgenius/dify/discussions/" target="_blank">
        <img alt="Discussion posts" src="https://img.shields.io/github/discussions/langgenius/dify?labelColor=%20%239b8afb&color=%20%237a5af8"></a>
</p>

<div align="center">
  <a href="./README.md"><img alt="README in English" src="https://img.shields.io/badge/English-d9d9d9"></a>
  <a href="./README_CN.md"><img alt="简体中文版自述文件" src="https://img.shields.io/badge/简体中文-d9d9d9"></a>
  <a href="./README_JA.md"><img alt="日本語のREADME" src="https://img.shields.io/badge/日本語-d9d9d9"></a>
  <a href="./README_ES.md"><img alt="README en Español" src="https://img.shields.io/badge/Español-d9d9d9"></a>
  <a href="./README_FR.md"><img alt="README en Français" src="https://img.shields.io/badge/Français-d9d9d9"></a>
  <a href="./README_KL.md"><img alt="README tlhIngan Hol" src="https://img.shields.io/badge/Klingon-d9d9d9"></a>
  <a href="./README_KR.md"><img alt="README in Korean" src="https://img.shields.io/badge/한국어-d9d9d9"></a>
  <a href="./README_AR.md"><img alt="README بالعربية" src="https://img.shields.io/badge/العربية-d9d9d9"></a>
  <a href="./README_TR.md"><img alt="Türkçe README" src="https://img.shields.io/badge/Türkçe-d9d9d9"></a>
  <a href="./README_VI.md"><img alt="README Tiếng Việt" src="https://img.shields.io/badge/Ti%E1%BA%BFng%20Vi%E1%BB%87t-d9d9d9"></a>
  <a href="./README_BN.md"><img alt="README in বাংলা" src="https://img.shields.io/badge/বাংলা-d9d9d9"></a>
</div>

# 

<div align="center">
  <a href="https://trendshift.io/repositories/2152" target="_blank"><img src="https://trendshift.io/api/badge/repositories/2152" alt="langgenius%2Fdify | 趋势转变" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</div>

Dify 是一个开源的 LLM 应用开发平台。其直观的界面结合了 AI 工作流、RAG 管道、Agent、模型管理、可观测性功能等，让您可以快速从原型到生产。以下是其核心功能列表：
</br> </br>

**1. 工作流**:
在画布上构建和测试功能强大的 AI 工作流程，利用以下所有功能以及更多功能。

**2. 全面的模型支持**:
与数百种专有/开源 LLMs 以及数十种推理提供商和自托管解决方案无缝集成，涵盖 GPT、Mistral、Llama3 以及任何与 OpenAI API 兼容的模型。完整的支持模型提供商列表可在[此处](https://docs.dify.ai/getting-started/readme/model-providers)找到。

![providers-v5](https://github.com/langgenius/dify/assets/13230914/5a17bdbe-097a-4100-8363-40255b70f6e3)

**3. Prompt IDE**:
用于制作提示、比较模型性能以及向基于聊天的应用程序添加其他功能（如文本转语音）的直观界面。

**4. RAG Pipeline**:
广泛的 RAG 功能，涵盖从文档摄入到检索的所有内容，支持从 PDF、PPT 和其他常见文档格式中提取文本的开箱即用的支持。

**5. Agent 智能体**:
您可以基于 LLM 函数调用或 ReAct 定义 Agent，并为 Agent 添加预构建或自定义工具。Dify 为 AI Agent 提供了 50 多种内置工具，如谷歌搜索、DALL·E、Stable Diffusion 和 WolframAlpha 等。

**6. LLMOps**:
随时间监视和分析应用程序日志和性能。您可以根据生产数据和标注持续改进提示、数据集和模型。

**7. 后端即服务**:
所有 Dify 的功能都带有相应的 API，因此您可以轻松地将 Dify 集成到自己的业务逻辑中。

## 使用 Dify

- **云 </br>**
  我们提供[ Dify 云服务](https://dify.ai)，任何人都可以零设置尝试。它提供了自部署版本的所有功能，并在沙盒计划中包含 200 次免费的 GPT-4 调用。

- **自托管 Dify 社区版</br>**
  使用这个[入门指南](#%E5%BF%AB%E9%80%9F%E5%90%AF%E5%8A%A8)快速在您的环境中运行 Dify。
  使用我们的[文档](https://docs.dify.ai)进行进一步的参考和更深入的说明。

- **面向企业/组织的 Dify</br>**
  我们提供额外的面向企业的功能。[给我们发送电子邮件](mailto:business@dify.ai?subject=%5BGitHub%5DBusiness%20License%20Inquiry)讨论企业需求。 </br>

  > 对于使用 AWS 的初创公司和中小型企业，请查看 [AWS Marketplace 上的 Dify 高级版](https://aws.amazon.com/marketplace/pp/prodview-t22mebxzwjhu6)，并使用一键部署到您自己的 AWS VPC。它是一个价格实惠的 AMI 产品，提供了使用自定义徽标和品牌创建应用程序的选项。

## 保持领先

在 GitHub 上给 Dify Star，并立即收到新版本的通知。

![star-us](https://github.com/langgenius/dify/assets/13230914/b823edc1-6388-4e25-ad45-2f6b187adbb4)
>>>>>>> v1.9.0

[English](README.md) | 简体中文

## 项目背景

自2024年10月起，我们开始与 Dify 团队展开合作。考虑到 MySQL 是全球应用最广泛的关系型数据库之一，许多用户强烈希望 Dify 能够支持 MySQL。同时，由于 OceanBase 与 MySQL 具有高度兼容性，我们向 Dify 项目提交了支持 MySQL pull request。但由于 Dify 团队当时正专注于内部开发里程碑的工作，暂时无法处理这项贡献。

此外，通过与众多 Dify 用户的深入交流，我们发现市场对多项企业级功能存在强烈需求。幸运的是，OceanBase 能够提供这些能力。因此，我们持续自主维护并增强该分支功能，以满足这些企业级需求。

## 欢迎贡献

欢迎任何建议，并感谢所有的贡献。

## 核心优势

这个分支提供以下企业级特性：

### 高可用性

在生产环境中，系统必须提供 7x24 小时不间断服务。数据库作为整个系统的核心组件，其任何故障都可能严重影响服务可用性。

<<<<<<< HEAD
OceanBase 通过 Paxos 共识协议保障高可用性。在生产环境中以集群模式部署时，即使单台服务器甚至多台服务器发生故障，只要集群中多数派仍然运行，OceanBase 仍能始终保持服务状态，确保无任何数据丢失（RPO = 0），并实现故障恢复时间在8秒以内（RTO < 8）。

### 可扩展性

随着运行时间的累积，数据库中存储的数据量持续增长。在传统数据库系统中，一旦数据量超过单台机器的容量限制，扩展就变得极具挑战性。

OceanBase 作为一款流行的分布式数据库，通过向集群添加新的节点来提供无限扩展能力。系统实现了数据和负载的自动重新平衡，整个过程对应用程序完全透明。
=======
#### 使用 Helm Chart 或 Kubernetes 资源清单（YAML）部署

使用 [Helm Chart](https://helm.sh/) 版本或者 Kubernetes 资源清单（YAML），可以在 Kubernetes 上部署 Dify。

- [Helm Chart by @LeoQuote](https://github.com/douban/charts/tree/master/charts/dify)

- [Helm Chart by @BorisPolonsky](https://github.com/BorisPolonsky/dify-helm)

- [Helm Chart by @magicsong](https://github.com/magicsong/ai-charts)

- [YAML 文件 by @Winson-030](https://github.com/Winson-030/dify-kubernetes)

- [YAML file by @wyy-holding](https://github.com/wyy-holding/dify-k8s)

- [🚀 NEW! YAML 文件 (支持 Dify v1.6.0) by @Zhoneym](https://github.com/Zhoneym/DifyAI-Kubernetes)

#### 使用 Terraform 部署
>>>>>>> v1.9.0

### AI 增强

<<<<<<< HEAD
鉴于 OceanBase 也是一款流行的向量数据库，它提供了强大的混合查询能力。这使得在单个查询中可以同时处理多种数据类型，包括向量数据、标量数据（关系表中的传统结构化数据）、GIS 和全文索引。

这种混合查询能力不仅可以帮助提升 AI 查询性能(将过去的多次查询融合为单次查询, 并利用优化器选择最优执行路径)，更为关键的是，通过混合查询可以提升查询的准确度（召回率），特别是在检索增强生成（RAG）系统中发挥更大的价值。
=======
##### Azure Global

- [Azure Terraform by @nikawang](https://github.com/nikawang/dify-azure-terraform)

##### Google Cloud

- [Google Cloud Terraform by @sotazum](https://github.com/DeNA/dify-google-cloud-terraform)
>>>>>>> v1.9.0

### 降低成本

通过用 OceanBase 替换当前 Dify 使用的所有数据库（包括 PostgreSQL、Weaviate 和 Redis），用户可以实现更高效的资源利用，并显著降低硬件成本。

<<<<<<< HEAD
此外，这种整合简化了数据库运维操作，从运维三套系统减少到只运维一套系统，从而大幅简化了维护工作并降低了操作复杂性。
=======
##### AWS

- [AWS CDK by @KevinZhao (EKS based)](https://github.com/aws-samples/solution-for-deploying-dify-on-aws)
- [AWS CDK by @tmokmss (ECS based)](https://github.com/aws-samples/dify-self-hosted-on-aws)

#### 使用 阿里云计算巢 部署

使用 [阿里云计算巢](https://computenest.console.aliyun.com/service/instance/create/default?type=user&ServiceName=Dify%E7%A4%BE%E5%8C%BA%E7%89%88) 将 Dify 一键部署到 阿里云

#### 使用 阿里云数据管理DMS 部署

使用 [阿里云数据管理DMS](https://help.aliyun.com/zh/dms/dify-in-invitational-preview) 将 Dify 一键部署到 阿里云

#### 使用 Azure Devops Pipeline 部署到AKS

使用[Azure Devops Pipeline Helm Chart by @LeoZhang](https://github.com/Ruiruiz30/Dify-helm-chart-AKS) 将 Dify 一键部署到 AKS
>>>>>>> v1.9.0

### 多租户支持

由于 OceanBase 原生支持多租户，Dify 用户现在可以通过 OceanBase 的多租户功能在应用层面实现多租户，而不会影响 Dify 现有的多租户规则。

<<<<<<< HEAD
## 安装社区版

### 系统要求

在安装 Dify 之前，请确保您的机器满足以下最低系统要求：

- CPU >= 2 核
- 内存 >= 8 GiB

### 快速启动
=======
## Contributing

对于那些想要贡献代码的人，请参阅我们的[贡献指南](https://github.com/langgenius/dify/blob/main/CONTRIBUTING_CN.md)。
同时，请考虑通过社交媒体、活动和会议来支持 Dify 的分享。

> 我们正在寻找贡献者来帮助将 Dify 翻译成除了中文和英文之外的其他语言。如果您有兴趣帮助，请参阅我们的[i18n README](https://github.com/langgenius/dify/blob/main/web/i18n-config/README.md)获取更多信息，并在我们的[Discord 社区服务器](https://discord.gg/8Tpq4AcN9c)的`global-users`频道中留言。
>>>>>>> v1.9.0

启动 Dify 服务器的最简单方法是运行我们的 [docker-compose.yaml](docker/docker-compose.yaml) 文件。

在运行安装命令之前，请确保您的机器上已安装 [Docker](https://docs.docker.com/get-docker/) 和 [Docker Compose](https://docs.docker.com/compose/install/)。

启动服务的操作如下：

```bash
cd docker
bash setup-mysql-env.sh
docker compose up -d
```

<<<<<<< HEAD
说明：
- `setup-mysql-env.sh` 是一个设置参数的辅助脚本，它会根据用户输入设置数据库连接信息，并配置 OceanBase 作为向量存储。
- Dify 1.x 开始引入了插件系统，安装插件的过程会根据插件配置执行类似 `python install -r requirements.txt` 的命令。为了加快安装速度，脚本中设置了 `PIP_MIRROR_URL` 为清华大学 Tuna 镜像源。
- 对于中国大陆用户，可以参考 https://github.com/dongyubin/DockerHub 设置 Docker 镜像加速，以获得更好的镜像加载速度。
=======
- [GitHub Discussion](https://github.com/langgenius/dify/discussions). 👉：分享您的应用程序并与社区交流。
- [GitHub Issues](https://github.com/langgenius/dify/issues)。👉：使用 Dify.AI 时遇到的错误和问题，请参阅[贡献指南](CONTRIBUTING.md)。
- [电子邮件支持](mailto:hello@dify.ai?subject=%5BGitHub%5DQuestions%20About%20Dify)。👉：关于使用 Dify.AI 的问题。
- [Discord](https://discord.gg/FngNHpbcY7)。👉：分享您的应用程序并与社区交流。
- [X(Twitter)](https://twitter.com/dify_ai)。👉：分享您的应用程序并与社区交流。
- [商业许可](mailto:business@dify.ai?subject=%5BGitHub%5DBusiness%20License%20Inquiry)。👉：有关商业用途许可 Dify.AI 的商业咨询。
>>>>>>> v1.9.0

运行后，可以在浏览器中访问 [http://localhost/install](http://localhost/install) 进入 Dify 控制台并开始初始化安装操作。

更多关于 Dify 使用的信息请参考 [https://dify.ai](https://dify.ai)。

## 许可证

本仓库遵循 [Dify Open Source License](LICENSE) 开源协议，该许可证本质上是 Apache 2.0，但有一些额外的限制。