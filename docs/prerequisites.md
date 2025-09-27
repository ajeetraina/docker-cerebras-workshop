# Prerequisites

Before starting this workshop, ensure you have the following requirements met. This will ensure a smooth learning experience and prevent setup issues during the workshop.

!!! warning "Important"
    Please complete all prerequisite setup before beginning the hands-on exercises. Missing requirements may prevent proper system functionality.

## System Requirements

### Docker Installation

**Required Docker Versions**

- **Docker Desktop** 4.43.0+ or **Docker Engine** (latest stable)
- For Linux with Docker Engine: **Docker Compose** 2.38.1 or later

!!! info "Download Links"
    - [Docker Desktop](https://www.docker.com/products/docker-desktop/)
    - [Docker Engine](https://docs.docker.com/engine/)

### Hardware Requirements

**GPU Support (Recommended)**

- A laptop or workstation with a GPU (e.g., MacBook, NVIDIA GPU)
- Required for running local AI models efficiently

!!! tip "Alternative"
    If you don't have a GPU, you can use [Docker Offload](https://www.docker.com/products/docker-offload/) for cloud-based model execution.

### Platform-Specific Setup

=== "Linux / Windows"
    For Docker Engine on Linux or Docker Desktop on Windows:

    - Ensure GPU support is enabled
    - Install necessary GPU drivers
    - Verify [Docker Model Runner requirements](https://docs.docker.com/ai/model-runner/)

=== "macOS"
    Docker Desktop on macOS with Apple Silicon:

    - Built-in GPU acceleration support
    - Optimized for M1/M2/M3 chips
    - No additional driver setup required

### Enable Docker Model Runner

Ensure that you've enabled Docker Model Runner using Docker Dashboard > Settings > AI > Model Runner. Download the following models beforehand.

```
docker model pull hf.co/menlo/jan-nano-gguf:q4_k_m
docker model pull hf.co/menlo/lucy-gguf:q8_0
```

!!! tip "Why we choose these models"
    These models implement a tiered intelligence architecture designed for optimal performance and resource efficiency.

    Jan-Nano is specifically designed and optimized to work seamlessly with Model Context Protocol (MCP) servers, enabling efficient   integration with various research tools and data sources JanJan. This is perfect for a coordinator that needs to route requests to different agents and tools. Routing & Orchestration Focus: The model excels at routing tasks, with MCP-agent providing router implementations including EmbeddingRouter for classification and Intent Classifier patterns that identify the most relevant categories for routing

    Lucy is an ideal choice for your Local Agent because its 1.7B parameter size strikes the perfect balance between capability and efficiency for local execution on consumer hardware. Built on the same Qwen3 architecture as Jan-Nano, Lucy ensures seamless compatibility within your agent ecosystem while being specifically optimized for conversational development tasks and code generation. Its compact size means lightning-fast response times for the quick Node.js queries, code explanations, and general development tasks that form the bulk of day-to-day programming work, while consuming minimal system resources. This allows Lucy to handle the high-frequency, low-complexity requests efficiently, leaving Jan-Nano free to focus on coordination decisions and Cerebras to tackle the truly complex computational challenges. The q8_0 quantization maintains excellent quality while ensuring Lucy can run smoothly locally, making it the perfect "first responder" agent that can instantly provide code snippets, explain concepts, and handle routine development questions without the latency or cost of cloud API calls.

## API Requirements

### 🧠 Cerebras API Access

You'll need a Cerebras API key to access advanced AI capabilities:

1. Visit [https://cloud.cerebras.ai/](https://cloud.cerebras.ai/)
2. Create an account or sign in
3. Navigate to API settings
4. Generate a new API key
5. Save the key securely (you'll need it during setup)

!!! warning "Security Note"
    Keep your API key secure and never commit it to version control. We'll show you how to use environment variables safely.

## Knowledge Prerequisites

### ✅ Required Knowledge

- **Basic Docker understanding**: Containers, images, and basic commands
- **Command line familiarity**: Running terminal/cmd commands
- **Web browser usage**: Accessing web interfaces and APIs

### 💡 Helpful (But Not Required)

- **Node.js development**: Understanding JavaScript/Node.js concepts
- **REST APIs**: Familiarity with API concepts and usage
- **AI/ML basics**: Understanding of machine learning concepts
- **FastAPI/Python**: Knowledge of web framework concepts

## Pre-Workshop Checklist

- [ ] Docker Desktop/Engine installed and running
- [ ] Docker Compose available (version 2.38.1+)
- [ ] GPU drivers installed (if using local GPU)
- [ ] Cerebras API key obtained and ready
- [ ] Internet connection available for API calls
- [ ] Text editor or IDE available for configuration

## Quick Verification Commands

Run these commands to verify your setup:

```bash
# Check Docker version
docker --version

# Check Docker Compose version
docker compose version

# Test Docker functionality
docker run hello-world

# Check available system resources
docker system df
```

!!! success "All Set?"
    If you've completed all the prerequisites, you're ready to dive into the workshop overview and understand the system architecture!
