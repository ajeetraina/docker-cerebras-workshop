# Docker DevDuck Multi-Agent System Workshop - Docker Labspace

A comprehensive Docker labspace for building and deploying sophisticated multi-agent systems using Docker, Google Agent Development Kit (ADK), and Cerebras AI.

## What You'll Learn

This interactive labspace teaches you how to build a multi-agent system for Node.js programming assistance featuring:

- **DevDuck**: Coordinator agent that routes requests intelligently
- **Local Agent**: Node.js development expert for code generation  
- **Cerebras Agent**: Advanced AI for complex problem-solving
- **Docker Compose**: Orchestration platform for seamless coordination

## Workshop Structure

The labspace is structured as an interactive learning experience with:

- **Introduction & Prerequisites**: Environment setup and requirements
- **System Overview**: Understanding the multi-agent architecture  
- **Hands-On Exercises**: Practical programming scenarios
- **Advanced Features**: Token streaming and model configuration
- **Best Practices**: Production deployment and optimization

## Running This Labspace

To run this labspace, you'll need Docker installed on your system.

### Quick Start

```bash
export CONTENT_REPO_URL=$(git remote get-url origin)
docker compose -f oci://dockersamples/labspace up -y
```

Then open your browser to [http://localhost:3030](http://localhost:3030)

### Development Mode

If you're developing this labspace content:

```bash
CONTENT_PATH=$PWD docker compose -f oci://dockersamples/labspace-content-dev up
```

## Learning Outcomes

After completing this workshop, you will be able to:

- Deploy multi-agent systems using Docker Compose
- Integrate local and cloud AI models effectively  
- Build FastAPI web interfaces for agent interaction
- Understand inter-agent communication patterns
- Apply best practices for AI agent orchestration

## Labspace Structure

- `labspace.yaml` - Defines the labspace configuration
- `docs/` - Contains the tutorial markdown files with hands-on exercises
- Source files - Multi-agent system implementation examples

## Repository Structure

```
├── labspace.yaml           # Labspace configuration
├── docs/                   # Tutorial content
│   ├── index.md           # Introduction
│   ├── prerequisites.md   # Setup requirements  
│   ├── overview.md        # System architecture
│   ├── getting-started.md # Initial setup
│   ├── deployment.md      # Docker deployment
│   ├── basic-interaction.md # Basic usage
│   ├── local-agent.md     # Local agent tasks
│   ├── cerebras-analysis.md # AI analysis
│   ├── agent-routing.md   # Routing patterns
│   ├── advanced-features.md # Advanced topics
│   ├── troubleshooting.md # Common issues
│   ├── best-practices.md  # Production tips
│   └── next-steps.md      # Further learning
├── Dockerfile             # Multi-agent system container
└── README.md              # This file
```

## Prerequisites

- Docker and Docker Compose installed
- Basic knowledge of containers and APIs
- Understanding of Python/FastAPI (helpful but not required)
- Cerebras API key (provided in tutorial)

## Contributing

This labspace is part of the Docker Samples collection. Contributions and improvements are welcome!

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
