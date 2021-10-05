FROM node:current-alpine as dependencies
COPY package.json ./
RUN npm i

FROM node:current-alpine as builder
COPY . .
COPY --from=dependencies node_modules ./node_modules
RUN npm run build

FROM node:current-alpine as runner
ENV NODE_ENV production
COPY --from=builder public ./public
COPY --from=builder .next ./.next
COPY --from=builder node_modules ./node_modules
COPY --from=builder package.json ./package.json

EXPOSE 8080
CMD ["npm", "run", "start"]
