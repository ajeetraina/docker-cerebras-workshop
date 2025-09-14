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


## Enable Docker Model Runner

Ensure that you've enabled Docker Model Runner using Docker Dashboard > Settings > AI > Model Runner.
Download the following models beforehand.

```
docker model pull unsloth/qwen3-gguf:4B-UD-Q4_K_XL
docker model pull hf.co/unsloth/qwen3-30b-a3b-instruct-2507-gguf:q5_k_m
```

!!! tip "Why we chose these models"
      These models implement a tiered intelligence architecture designed for optimal performance and resource efficiency. 
       
       The smaller Qwen3-4B model serves as a fast coordinator that handles routing decisions and simple tasks, while the larger 30B model tackles complex reasoning and code generation when needed. 
       This approach ensures users get immediate responses for basic interactions while still having access to powerful AI capabilities for demanding tasks. 
       The technical optimizations make these models particularly suitable for containerized deployments. 
       
     Unsloth framework provides 2-5x speed improvements over standard implementations, while GGUF quantization reduces model sizes significantly (Q4 cuts size by ~75%) without major quality loss. The 4B model uses Q4_K_XL quantization for fast inference with extended context support, while the 30B variant uses Q5_K_M for better quality preservation on complex tasks.

       This strategic model selection delivers the best of both worlds: lightning-fast coordination for user experience and heavyweight reasoning for quality outputs. Rather than running one large model constantly (expensive and slow) or one small model always (fast but limited), this tiered approach optimizes both cost and capability, making it ideal for production AI applications where both responsiveness and intelligence matter.


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
