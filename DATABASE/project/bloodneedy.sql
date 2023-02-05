-- geetting all posts
SELECT * FROM bloodapp.bloodneedrequirement;


-- get the info of the acceptor who is posting the request

select person.fname, person.lname, bloodneedrequirement.*
from person inner join   bloodneedrequirement on  person.cnic = bloodneedrequirement.cnic;


-- getting needy location as well as their req -- 
select person.fname, person.lname, bloodneedrequirement.*, personlocation.Block, personlocation.Area, personlocation.City, personlocation.postalCode
from person inner join   bloodneedrequirement on  person.cnic = bloodneedrequirement.cnic inner join personlocation on 
personlocation.loc_id= person.loc_id;

