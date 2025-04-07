FROM nginx:alpine

# Copy the custom Nginx configuration file into the container
COPY ./gateway/nginx-kube.conf /etc/nginx/nginx.conf

# Expose port 80 for the Nginx server
EXPOSE 80