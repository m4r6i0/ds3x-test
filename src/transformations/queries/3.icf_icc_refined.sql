CREATE OR REPLACE TABLE `ps-eng-dados-ds3x.marcio_costa.icf_icc_refined` AS
SELECT
  t1.ano_mes,
  t1.icc_indice,
  SAFE_CAST(t1.icc_variacao AS FLOAT64) AS icc_variacao,
  t2.icf_indice,
  SAFE_CAST(t2.icf_variacao AS FLOAT64) AS icf_variacao,
  CURRENT_TIMESTAMP() AS load_timestamp
FROM `ps-eng-dados-ds3x.marcio_costa.icc_trusted` t1
FULL OUTER JOIN `ps-eng-dados-ds3x.marcio_costa.icf_trusted` t2
ON t1.ano_mes = t2.ano_mes
