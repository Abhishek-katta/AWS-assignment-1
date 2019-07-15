aws dynamodb create-table \
 --table-name Games \
 --attribute-definitions \
 AttributeName=gid,AttributeType=N \
 --key-schema AttributeName=gid,KeyType=HASH \
 --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
 --region us-west-1

aws dynamodb put-item \
 --table-name Games \
 --item '{
 "gid": {"N":"2"},
 "gname": {"S":"pubg"},
 "publisher": {"S":"tencent"},
 "rating": {"N":"5"},
 "releasedate": {"S":"september14,2019"},
 "genres": {"SS":["battleroyale","adult"]}}' \
 --return-consumed-capacity TOTAL \
 --region us-west-1
