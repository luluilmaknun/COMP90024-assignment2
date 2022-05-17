# syntax=docker/dockerfile:1

FROM node:14.17.0

ENV NODE_ENV=production

WORKDIR /app

COPY ["package.json", "package-lock.json*", "./"]

RUN npm install --dev
RUN npm install -g serve

COPY . .

EXPOSE 3000
RUN npm build

#CMD ["sleep", "3600"]
#CMD ["npm", "install", "--save-dev"]
#CMD ["npm", "install" "-g" "@angular/cli"]
#CMD ["ng", "serve"]

#CMD ["npm", "start"]
CMD ["serve", "-l","3000","-s","build"]

