select 
    -- Add standard clean-up columns or cast types here from raw_readmission
    * 
from {{ source('main', 'raw_readmission') }}