# syntax=docker/dockerfile:1

FROM node:14.15.1

ENV NODE_ENV=production

WORKDIR /app

COPY ["package.json", "package-lock.json*", "./"]

RUN npm install --dev

COPY . .

EXPOSE 4200

#CMD ["sleep", "3600"]
#CMD ["npm", "install", "--save-dev"]
#CMD ["npm", "install" "-g" "@angular/cli"]
#CMD ["ng", "serve"]

CMD ["npm", "run", "start"]

