--  getting all blood banks
SELECT * FROM bloodapp.bloodbank;

-- in a front end if blood bank is matched with the real time the status is opened else closed 
-- please format the date in am pm format 
SELECT bankName
from bloodapp.bloodbank
where current_time() >= openingTimings and  current_time() < closingTimings;

-- getting full bloodbank info 

Select bloodbank.BankName, bloodbankcontactdetails.contactno
from bloodbank 
inner join bloodbankcontactdetails on bloodbank.BankName = bloodbankcontactdetails.bankName;

-- locations-- 
select bloodbank.BankName, bloodbanklocation.*
from bloodbank
inner join bloodbanklocation on bloodbank.BankName = bloodbanklocation.BankName;

-- count total branches
select BankName,count(*) as totalbranches
from bloodbanklocation
group by BankName;

