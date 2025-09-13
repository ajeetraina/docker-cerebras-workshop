# Troubleshooting

Common issues and their solutions.

## Common Issues

### Cannot Access Web Interface

- **Solution**: Ensure all containers are running with `docker compose ps`
- **Check**: Verify port 8000 is not in use by other applications

### Cerebras Agent Not Responding

- **Solution**: Verify your Cerebras API key in the `.env` file
- **Check**: Ensure internet connectivity for Cerebras API calls

### Cannot Switch Between Agents

- **Solution**: Try the reset command: `go back to devduck`
- **Check**: Wait for current agent response to complete before switching

### GPU-Related Errors

- **Solution**: Verify GPU drivers are installed and Docker has GPU access
- **Alternative**: Use Docker Offload if no GPU is available

## Health Checks

Monitor system health:

```bash
# Check container status
docker compose ps

# View logs 
docker compose logs 

# Check resource usage
docker stats
```

!!! note "Coming Soon"
    More troubleshooting scenarios will be added to this section.
