# Docker Cerebras Multi-Agent Workshop

A comprehensive workshop for building and deploying sophisticated multi-agent systems using Docker, Google Agent Development Kit (ADK), and Cerebras AI.

## 🚀 Quick Start

This workshop teaches you how to build a multi-agent system for Node.js programming assistance featuring:

- **DevDuck**: Coordinator agent that routes requests intelligently
- **Local Agent**: Node.js development expert for code generation
- **Cerebras Agent**: Advanced AI for complex problem-solving
- **Docker Compose**: Orchestration platform for seamless coordination

## 📚 Workshop Content

The workshop is structured as an interactive learning experience with:

- **Getting Started**: Environment setup and prerequisites
- **System Overview**: Understanding the multi-agent architecture
- **Hands-On Exercises**: Practical programming scenarios
- **Advanced Features**: Token streaming and model configuration
- **Best Practices**: Production deployment and optimization

## 🐳 Run as a Docker container

Clone the repo and follow the instructions to run this workshop inside a Docker container

```
docker build -t devduck .
docker run -p 8003:8000 devduck 
```


## 🛠️ Local Development

To run this workshop site locally:

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start development server
mkdocs serve

# Build for production
mkdocs build
```

## 🌐 Deployment

### GitHub Pages (Automatic)

1. Push your repository to GitHub
2. Go to Settings → Pages
3. Select "GitHub Actions" as source
4. The site will build and deploy automatically

### Manual Deployment

```bash
# Build the site
mkdocs build

# Deploy to GitHub Pages
mkdocs gh-deploy
```

## 📖 Workshop Structure

The workshop follows a progressive learning approach:

1. **Introduction & Prerequisites** - Setup and requirements
2. **System Architecture** - Understanding the multi-agent design
3. **Deployment** - Docker Compose orchestration
4. **Agent Interaction** - Hands-on exercises with each agent
5. **Advanced Topics** - Configuration and optimization

## 🎯 Learning Objectives

After completing this workshop, you will be able to:

- Deploy multi-agent systems using Docker Compose
- Integrate local and cloud AI models effectively
- Build FastAPI web interfaces for agent interaction
- Understand inter-agent communication patterns
- Apply best practices for AI agent orchestration



