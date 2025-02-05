# Utilise une image de base Node.js pour la construction
FROM node:18-bookworm AS builder
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
RUN npm run build

FROM node:18-bookworm
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY package.json ./
RUN npm install 
EXPOSE 4173
CMD ["npm", "run", "serve"]
