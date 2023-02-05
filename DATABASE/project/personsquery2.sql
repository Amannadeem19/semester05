SELECT * FROM bloodapp.person;

-- find all the details of a person
-- add profile pic too
select person.fname, person.lname, person.blood_group, person.weight, person.frequencyDonation, person.IsDiabetes, person.IsHypetitus, personlocation.Block, personlocation.Area, personlocation.City, personlocation.postalCode
from person inner join personlocation where person.loc_id = personlocation.loc_id;

-- contact details of a person

select person.fname, person.lname, person.blood_group, person.weight, person.frequencyDonation, person.IsDiabetes, person.IsHypetitus, personcontactdetails.contactno
from person inner join personcontactdetails  where person.cnic = personcontactdetails.Cnic;