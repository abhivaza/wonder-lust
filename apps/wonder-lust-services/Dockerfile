FROM node:20.15.1 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install --only=development --silent
COPY . .
RUN npx nx reset
RUN npx nx build wonder-lust-services --prod
FROM node
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install -g pm2@latest
RUN npm install --only=production --silent
RUN npm install express
COPY --from=builder /app/dist/apps/wonder-lust-services ./build
ENTRYPOINT ["pm2-runtime","build/main.js"]