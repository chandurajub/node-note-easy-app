FROM node
ADD . / tmp/
RUN  (cd tmp/; npm install;)
CMD  (cd tmp/; node server.js;)
