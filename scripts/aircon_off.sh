set -a
source .env
set +a

curl -X POST https://api.nature.global/1/appliances/a015ff25-04f1-481f-8c11-d238f41312e1/aircon_settings -d "button=power-off" -H "Authorization: Bearer ${NATURE_ACCESS_TOKEN}" | jq
