WITH ordered_logs AS (
    SELECT
        campaign_id,
        verdict,
        verdict_time,
        datetime(verdict_time) AS dt,
        ROW_NUMBER() OVER (PARTITION BY campaign_id ORDER BY datetime(verdict_time)) AS rn
    FROM logs
),
paired_logs AS (
    SELECT
        n.campaign_id,
        DATE(n.dt) AS field_date,
        JULIANDAY(y.dt) - JULIANDAY(n.dt) AS wait_days
    FROM ordered_logs n
    JOIN ordered_logs y
        ON n.campaign_id = y.campaign_id
        AND y.rn > n.rn
        AND y.verdict = 'Yes'
    WHERE n.verdict = 'No'
      AND NOT EXISTS (
          SELECT 1
          FROM ordered_logs z
          WHERE z.campaign_id = n.campaign_id
            AND z.rn > n.rn AND z.rn < y.rn
            AND z.verdict = 'Yes'
      )
),
wait_minutes AS (
    SELECT
        field_date,
        ROUND(wait_days * 24 * 60, 0) AS wait_minutes
    FROM paired_logs
)
SELECT
    field_date,
    ROUND(AVG(wait_minutes), 0) AS avg_wait_time
FROM wait_minutes
GROUP BY field_date
ORDER BY field_date;
