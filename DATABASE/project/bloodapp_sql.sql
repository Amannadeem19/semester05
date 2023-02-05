--table person 
create table person (Cnic varchar(13) primary key not null ,
blood_type varchar(10) ,f_name varchar(10),
l_name varchar(10), DOB date, diabetes Number(1) , hypetitus Number(1) , weight FLOAT );


--person location
create table person_location (location_id varchar(10) not null , cnic varchar(13) not null,
street varchar(10) , postal_code varchar(10), 
area_name varchar(15),city varchar(10),

primary key (location_id, cnic),

foreign key (cnic) references person(Cnic)

);




create table  BloodBank (blood_bank_id varchar(6) not null,
bank_name varchar(10),
primary key (blood_bank_id)
);

create table bloodBankContact( bank_id varchar(6) not null, 
contact_number Number(11) not null,
primary key (bank_id, contact_number),
foreign key (bank_id) references BloodBank(blood_bank_id)

);
create table blood_bank_location(blood_bank_location_id varchar(6),
blood_bank_id varchar(10) , postal_code varchar(10) , 
city varchar(10), place varchar(10), street varchar(10), 
area_no varchar(10) , nearby_area varchar(10),

primary key (blood_bank_location_id),
foreign key (blood_bank_id) references BloodBank(blood_bank_id)

);
create table blood_record(
blood_bank_id varchar(6) ,
cnic varchar(13) ,bloodtype varchar(10) not null, 
Datedonation date not null, 

primary key (blood_bank_id, cnic),
foreign key (cnic) references person(Cnic),
foreign key(blood_bank_id) references BLOODBANK(blood_bank_id)

);


create table needy_req(req_id varchar(10)  not null
,cnic varchar(20),blood_type varchar(10),
quantity int ,time_period date ,reason varchar(50),

primary key (req_id),
foreign key (cnic) references person(Cnic)


);



create table fullfilled_req (
blood_bank_id varchar(6) not null,
cnic varchar(13) not null,
req_id varchar(10) not null, 
date_donation date ,qty int ,
status varchar(10) not null,

primary key(blood_bank_id, cnic, req_id),
foreign key (blood_bank_id, cnic) references blood_record(blood_bank_id, cnic)



);




