FROM node:20.15.1 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npx nx reset
RUN npx nx build wonder-lust-ui --prod
FROM nginx
WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
COPY --from=builder /app/dist/apps/wonder-lust-ui ./
RUN sed -i '10i \\ttry_files $uri $uri/ /index.html;' /etc/nginx/conf.d/default.conf
ENTRYPOINT ["nginx", "-g", "daemon off;"]