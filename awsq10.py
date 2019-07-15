aws dynamodb query \
   --table-name Games \
   --select "SPECIFIC_ATTRIBUTES" \
   --key-condition-expression "gid = :id" \
   --expression-attribute-values  '{":id":{"N":"2"}}' \
   --projection-expression "gname,rating" \
   --region us-west-1
