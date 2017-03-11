FROM mongo

COPY /data/host_list.json /init.json
CMD mongoimport --host mongodb --db reach-engine --collection hosts --type json --file /init.json --jsonArray
