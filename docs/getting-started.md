# Getting Started

Now that you understand the system architecture, let's get your hands dirty! This section will guide you through the complete setup process, from cloning the repository to accessing your first multi-agent system.

!!! info "Estimated Time"
    15-20 minutes for complete setup

## Step 1: Repository Setup

First, let's clone the repository and navigate to the project directory:

```bash
# Clone the Docker Cerebras demo repository
git clone https://github.com/dockersamples/docker-cerebras-demo.git

# Navigate to the project directory
cd docker-cerebras-demo

# List the contents to familiarize yourself
ls -la
```

### 📁 Repository Structure

You should see files similar to:

```
.
├── LICENSE.md
├── README.md
├── agents
│   ├── Dockerfile
│   ├── devduck
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   └── sub_agents
│   │       ├── __init__.py
│   │       ├── cerebras
│   │       │   ├── __init__.py
│   │       │   ├── agent.py
│   │       │   └── tools.py
│   │       └── localagent
│   │           ├── __init__.py
│   │           └── agent.py
│   ├── main.py
│   └── requirements.txt
├── compose.yml
├── mcp-gateway-catalog.yaml
├── pyproject.toml
└── uv.lock
```

## Step 2: Environment Configuration

Configure your environment variables by creating a `.env` file from the provided template:

```bash
# Copy the environment template
cp .env.sample .env

# Open the .env file in your preferred editor
# For example, using nano:
nano .env

# Or using VS Code:
code .env
```

### Required Environment Variables

Edit your `.env` file to include your Cerebras API credentials:

```env
# Cerebras API Configuration
CEREBRAS_API_KEY=your_actual_api_key_here
CEREBRAS_BASE_URL=https://api.cerebras.ai/v1
CEREBRAS_CHAT_MODEL=llama-4-scout-17b-16e-instruct
```

!!! warning "API Key Setup"
    Replace `your_actual_api_key_here` with your actual Cerebras API key obtained from [https://cloud.cerebras.ai/](https://cloud.cerebras.ai/)

## Step 3: System Deployment

Now let's deploy the complete multi-agent system using Docker Compose:

### Initial Deployment

```bash
# Deploy all services
docker compose up

# Or run in detached mode (background)
docker compose up -d
```

!!! note "First Run Notes"
    - The first deployment may take several minutes as Docker downloads required images
    - Local models will be downloaded and cached automatically
    - You'll see startup logs for all three agents

### Development Deployment

If you make changes to the code and need to rebuild:

```bash
# Rebuild and deploy with code changes
docker compose up --build

# Force recreation of containers
docker compose up --build --force-recreate
```

## Step 4: Verify Deployment

### Check Service Status

```bash
# Check if all services are running
docker compose ps

# View logs for all services
docker compose logs
```

### ✅ Expected Output

A successful deployment should show all services as "Up":

```
NAME                                   IMAGE                                COMMAND                  SERVICE         CREATED         STATUS         PORTS
docker-cerebras-demo-devduck-agent-1   docker-cerebras-demo-devduck-agent   "sh -c 'uvicorn main…"   devduck-agent   3 minutes ago   Up 3 minutes   0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp
docker-cerebras-demo-mcp-gateway-1     docker/mcp-gateway:latest            "/docker-mcp gateway…"   mcp-gateway     3 minutes ago   Up 3 minutes
```

### Network and Resource Check

```bash
# Check resource usage
docker stats

# Verify network connectivity
docker network ls

# Check available disk space
docker system df
```

## Step 5: Access the Application

Once all services are running successfully, you can access the web interface:

!!! success "Web Interface Access"
    **Primary URL**: [http://0.0.0.0:8000](http://0.0.0.0:8000/dev-ui/?app=devduck)
    
    **Alternative URL**: [http://localhost:8000](http://localhost:8000)

### First Access Verification

1. Open your web browser
2. Navigate to `http://0.0.0.0:8000/dev-ui/?app=devduck`
3. You should see the multi-agent interface
4. Try typing a simple message like "Hello"
5. Verify that DevDuck responds appropriately

## Quick Health Check

Let's perform a quick system health check to ensure everything is working:

### 🏥 System Health Checklist

- [ ] All Docker containers are running
- [ ] Web interface loads at http://0.0.0.0:8000
- [ ] DevDuck agent responds to simple messages
- [ ] No error messages in container logs
- [ ] System resources are not maxed out

## Troubleshooting Common Issues

### ⚠️ Port Already in Use

If port 8000 is already in use:

```bash
# Find what's using port 8000
lsof -i :8000

# Or modify docker-compose.yml to use a different port
# Change "8000:8000" to "8001:8000" in the ports section
```


### 🤖 Model Too Big

In case you encounter the following error message stating:

```
{"error": "litellm.InternalServerError: InternalServerError: OpenAIException - unable to load runner: model too big"}
```

It's recommended to use lightweight model like Llama 3.2 based on your system configuration.


### 🚫 Cerebras API Issues

If Cerebras agent fails to start:

- Verify your API key is correct in the .env file
- Check internet connectivity
- Ensure your Cerebras account has API access

!!! success "Congratulations!"
    You've successfully deployed your multi-agent system. In the next section, we'll start with hands-on exercises to explore the capabilities of each agent.
