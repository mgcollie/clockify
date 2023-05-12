# Use the standard Nginx image from Docker Hub
FROM nginx:1.13.5

RUN mkdir -p /var/lib/nginx/cache && chmod -R 777 /var/lib/nginx/cache

# Copy the configuration file from  the current directory and paste
# it inside the container to use it as Nginx's default config.
COPY nginx.conf /etc/nginx/nginx.conf
COPY proxy-settings.conf /etc/nginx/proxy-settings.conf

EXPOSE 8000

# Start Nginx when the container has provisioned.
CMD ["nginx", "-g", "daemon off;"]