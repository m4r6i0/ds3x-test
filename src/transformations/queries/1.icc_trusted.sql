CREATE OR REPLACE TABLE `ps-eng-dados-ds3x.marcio_costa.icc_trusted` AS
SELECT
  SAFE_CAST(FORMAT_TIMESTAMP('%Y-%m', TIMESTAMP(load_timestamp)) AS STRING) AS ano_mes,
  indice AS icc_indice,
  variacao AS icc_variacao,
  load_timestamp
FROM `ps-eng-dados-ds3x.marcio_costa.icc_raw`
WHERE indice IS NOT NULL