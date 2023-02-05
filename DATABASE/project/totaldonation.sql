SELECT * FROM bloodapp.totaldonations;

-- update fullfilleddonation
-- set status= 'completed' 
-- from totaldonations inner join bloodneedrequirement on totaldonations.requirement_id = bloodneedrequirement.req_id
-- where bloodneedrequirement.Qtyneed = totaldonations.GivenQty;

-- total donations of the requirement
select bloodneedrequirement.*, sum(totaldonations.GivenQty)
from totaldonations, bloodneedrequirement
where totaldonations.requirement_id = bloodneedrequirement.req_id; 

select bloodneedrequirement.req_id, bloodneedrequirement.Qtyneed, bloodneedrequirement.bloodGroup, count(recorddonation.cnic)
from recorddonation, bloodneedrequirement
where recorddonation.req_id = bloodneedrequirement.req_id
group  by (bloodneedrequirement.req_id); 

update fullfilleddonation f, recorddonation r, bloodneedrequirement b
set f.status = 'completed'
where f.req_id = b.req_id AND r.req_id = b.req_id AND b.Qtyneed = 1;
CREATE DEFINER=`root`@`localhost` TRIGGER `bloodneedrequirement_AFTER_INSERT` AFTER INSERT ON `bloodneedrequirement` FOR EACH ROW BEGIN

	insert into requirementbackup values (new.req_id, new.cnic, new.bloodGroup,
    new.Qtyneed, curdate(), curtime(), new.reason, new.TimePeriod);
END