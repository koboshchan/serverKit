# serverKit

Instant minecraft server startup with Docker Compose, using itzg's Minecraft server image for easy updates and management. The server is configured to run Folia, a high-performance Minecraft server software, with custom settings defined in a patch.json file. The setup also includes support for Velocity proxy secrets and custom commands configuration.

## Running the Server

1. Write your velocity secret to `forwarding.secret` in the root of this repository.
2. Run `docker compose up -d` to start the server in detached mode.
3. Stop the server with `docker compose down`.
4. Edit server plugins, configs, and world data in the `data` directory.
5. Restart the server to apply changes with `docker compose up -d`.
6. thats it.