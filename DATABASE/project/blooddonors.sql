SELECT * FROM bloodapp.recorddonation;
-- filter- getting all the donors of the specific blood group
select  person.fname, person.lname, person.weight, person.frequencyDonation, person.profile_pic from recorddonation 
inner join person  on person.cnic = recorddonation.cnic  where bloodGroup = 'A+';

-- donors of the needy means one requirement ke kon konse donor thy and with the help of those blood banks
select  person.fname, person.lname, person.weight, person.frequencyDonation, person.profile_pic, bloodbank.BankName from recorddonation 
inner join person  on person.cnic = recorddonation.cnic inner join bloodneedrequirement on bloodneedrequirement.req_id = recorddonation.req_id inner join bloodbank on bloodbank.BankName = recorddonation.bankName;

 