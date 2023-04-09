FROM node:19-alpine as build

WORKDIR /web
COPY . /web/


ARG VITE_API_ROOT
RUN echo "VITE_API_ROOT=${VITE_API_ROOT}" > .env.production

RUN npm ci;
RUN npm run build;

FROM nginx

COPY --from=build /web/dist /usr/share/nginx/html
COPY default.conf /etc/nginx/conf.d

EXPOSE 80


