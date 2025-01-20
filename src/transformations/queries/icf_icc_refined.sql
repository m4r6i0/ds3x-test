CREATE OR REPLACE TABLE `ps-eng-dados-ds3x.marcio_costa.icf_icc_refined` AS
SELECT
  t1.ano_mes,
  t1.icc_indice,
  t1.icc_variacao,
  t2.icf_indice,
  t2.icf_variacao,
  CURRENT_TIMESTAMP() AS load_timestamp
FROM `ps-eng-dados-ds3x.marcio_costa.icc_trusted` t1
FULL OUTER JOIN `ps-eng-dados-ds3x.marcio_costa.icf_trusted` t2
ON t1.ano_mes = t2.ano_mes;
