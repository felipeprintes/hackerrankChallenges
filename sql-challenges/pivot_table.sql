select
    min(case when ocp='Doctor' then name end) as 'Doctor',
    min(case when ocp='Actor' then name end) as 'Actor',
    min(case when ocp='Singer' then name end) as 'Singer',
    min(case when ocp='Professor' then name end) as 'Professor'
from (select name, ocp, 
      row_numbe() over(partition by ocp order by name) as occ) as hcc
group by occ 