FROM php:8-apache

# Set working directory
WORKDIR /var/www/html

# Copy the files into the container
COPY . .

# Set permissions to ensure Apache can read the files
RUN chown -R www-data:www-data /var/www

# Expose port 80
EXPOSE 80