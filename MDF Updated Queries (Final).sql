a. Manage MDF funds(For Vendor role) : Tiles query

select count(distinct partner_id) as "Total Partners"
,max(coalesce(xmc.mdf_amount,0)) as "MDF ACCOUNT BALANCE"
,max(coalesce(xmc.mdf_used_amount,0)) as "USED BALANCE"
,max(coalesce(xmc.mdf_amount,0)) - max(coalesce(xmc.mdf_used_amount,0)) as "AVAILABLE BALANCE"
from xt_partnership xp
left join xt_mdf_credit xmc on xmc.partnership_id = xp.id
where vendor_company_id = 769;

---------------------------------------------------------------------------------------------------------------------------------------------
a. Manage MDF funds(For Vendor role) : detailed report query  

select xp.partner_id,xcp.company_name as "Partner Company Name",xup.email_id,xup.firstname,xup.lastname
,coalesce(xmc.mdf_amount,0) as "MDF ACCOUNT BALANCE"
,coalesce(xmc.mdf_used_amount,0) as "USED BALANCE"
,coalesce(xmc.mdf_amount,0) - coalesce(xmc.mdf_used_amount,0) as "AVAILABLE BALANCE"
from xt_partnership xp
left join xt_user_profile xup on xup.user_id = xp.partner_id
left join xt_company_profile xcp on xcp.company_id = xp.partner_company_id
left join xt_mdf_credit xmc on xmc.partnership_id = xp.id
where xp.vendor_company_id = 769; 

----------------------------------------------------------------------------------------------------------------------------------------------
b.Manage MDF Requests(For Vendor role) : Tiles query:

select count(distinct partner_id) as "# Partners" from xt_partnership where vendor_company_id = 769 ; 

----------------------------------------------------------------------------------------------------------------------------

select count(distinct m.id) as "Number of Requests"
,sum(case when xl.label_name like 'Request Amount%'  then xfsc.value::integer end)/count(distinct m.id)
as Average_Reuqest_Size,
coalesce(sum(case when xl.label_name like 'Request Amount%'  then xfsc.value::integer end),0)
as Total_value
from xt_mdf_request m
left join xt_user_profile xup on m.user_id = xup.user_id
left join xt_partnership p on p.partner_company_id = m.company_id
left join xt_company_profile xcp on xcp.company_id = p.partner_company_id
left join xt_form_submit xfs on xfs.id= m.form_submit_id
left join xt_form_submit_single_choice xfsc on xfsc.form_submit_id = m.form_submit_id
left join xt_form_label xl on  xl.id= xfsc.form_label_id
where p.vendor_company_id = 769 and p.partner_company_id = 273;

---------------------------------------------------------------------------------------------------------------------------------

Manage MDF Requests(For Vendor role) : detailed report query:  

select created_time "Date Created","MDF Request","Amount",status as "Stage","Partner Company", "Partner Contact"
from (
with a as (select xmr.id,xmr.form_submit_id,xmr.created_time,xmr.status 
,xcp.company_name as "Partner Company",
xup.firstname ||' '|| xup.lastname as "Partner Contact"
from xt_mdf_request xmr
left join xt_user_profile xup on xmr.user_id = xup.user_id
left join xt_company_profile xcp on xcp.company_id = xup.company_id 
left join xt_partnership xp on xcp.company_id = xp.partner_company_id 
where xp.vendor_company_id = 769)
, b as (select * from xt_form xf join xt_form_submit xfs on xfs.form_id = xf.id 
left join xt_form_label xfl on xfl.form_id = xf.id 
left join xt_form_submit_single_choice xfssc on xfssc.form_label_id = xfl.id and xfssc.form_submit_id = xfs.id)
, c as (select * from xt_form xf join xt_form_submit xfs on xfs.form_id = xf.id 
left join xt_form_label xfl on xfl.form_id = xf.id 
left join xt_form_submit_single_choice xfssc on xfssc.form_label_id = xfl.id and xfssc.form_submit_id = xfs.id)
select distinct a.*,
case when b.label_name like 'Title%' then b.value end as "MDF Request",
case when c.label_name like 'Request Amount%' then c.value end as "Amount"
from a join b on a.form_submit_id = b.form_submit_id
join c on a.form_submit_id = c.form_submit_id
) foo where "MDF Request" is not null and "Amount" is not null;

-------------------------------------------------------------------------------------------------------------------------------------
Manage MDF Request (Second screen):

select m.created_time as "Date created",
case when xl.label_name like 'Request Amount%' then xfsc.value::integer end as "Request Amount",
xcp.company_name as "Partner Company",
xup.firstname ||' '|| xup.lastname as "MDF Request Owner",
m.allocation_amount as "Allocated Amount",
m.reimburse_amount as "Reimburse Amount"
from xt_mdf_request m
left join xt_user_profile xup on m.user_id = xup.user_id
left join xt_company_profile xcp on xcp.company_id = xup.company_id 
left join xt_partnership p on p.partner_company_id = xcp.company_id
left join xt_form_submit xfs on xfs.id= m.form_submit_id
left join xt_form xf on xf.id = xfs.form_id 
left join xt_form_label xl on xl.form_id = xf.id
left join xt_form_submit_single_choice xfsc on xfsc.form_submit_id = xfs.id and xfsc.form_label_id = xl.id
where p.vendor_company_id = 769 and m.id = 15
and case when xl.label_name like 'Request Amount%' then xfsc.value end is not null;

------------------------------------------------------------------------------------------

Partner MDF Balances (For Vendor Role) (2nd screenshot in Page 3)

select xp.partner_id,xcp.company_name as "Partner Company Name",xup.email_id,xup.firstname,xup.lastname
,coalesce(xmc.mdf_amount,0) as "MDF ACCOUNT BALANCE"
,coalesce(xmc.mdf_used_amount,0) as "USED BALANCE"
,coalesce(xmc.mdf_amount,0) - coalesce(xmc.mdf_used_amount,0) as "AVAILABLE BALANCE"
from xt_partnership xp
left join xt_user_profile xup on xup.user_id = xp.partner_id
left join xt_company_profile xcp on xcp.company_id = xp.partner_company_id
left join xt_mdf_credit xmc on xmc.partnership_id = xp.id
where xp.vendor_company_id = 769 and xp.partner_company_id = 273;
------------------------------------------------------------------------------------------------------

MDF Request Owner (Right side queries)

select
xup.firstname ||' '|| xup.lastname as "MDF Request Owner",
xup.email_id as "Email ID",
xup.mobile_number as "Phone Number",
xcp.company_name as "Partner Company",
xcp.website as "Website",
xcp.state as "State"
xcp.phone as "Company Phone"
from xt_mdf_request m
left join xt_user_profile xup on m.user_id = xup.user_id
left join xt_partnership p on p.partner_company_id = m.company_id
left join xt_company_profile xcp on xcp.company_id = p.partner_company_id
where p.vendor_company_id = 769 and m.id = 19;

--------------------------------------------------------------------------
Partner Manager:(Right side queries)

select distinct xup.firstname ||' '|| xup.lastname as "Partner Manager",
xup.email_id as "Email ID",
xup.mobile_number as "Phone Number"
from xt_mdf_request m
left join xt_partnership p on m.company_id = p.partner_company_id
left join xt_user_profile xup on p.partner_id = xup.user_id
left join xt_company_profile xcp on xcp.company_id = xup.company_id
where p.vendor_company_id = 769 and m.id = 19;


Partner Role screen :(Manage MDF Request) tiles query
--------------------------------------------------------------------------

select count(distinct m.id) as "Number of Requests"
,sum(case when xl.label_name like 'Request Amount%'  then xfsc.value::integer end)/count(distinct m.id)
as Average_Reuqest_Size,
coalesce(sum(case when xl.label_name like 'Request Amount%'  then xfsc.value::integer end),0)
as Total_value
from xt_mdf_request m
left join xt_user_profile xup on m.user_id = xup.user_id
left join xt_partnership p on p.partner_company_id = m.company_id
left join xt_company_profile xcp on xcp.company_id = p.partner_company_id
left join xt_form_submit xfs on xfs.id= m.form_submit_id
left join xt_form_submit_single_choice xfsc on xfsc.form_submit_id = m.form_submit_id
left join xt_form_label xl on  xl.id= xfsc.form_label_id
where p.vendor_company_id = 769;

----------------------------------------------------------------------------
Partner Role:(Manage MDF Request) Detail query

select created_time "Date Created","MDF Request","Amount",status as "Stage","Partner Company", "Partner Contact"
from (
with a as (select xmr.id,xmr.form_submit_id,xmr.created_time,xmr.status 
,xcp.company_name as "Partner Company",
xup.firstname ||' '|| xup.lastname as "Partner Contact"
from xt_mdf_request xmr
left join xt_user_profile xup on xmr.user_id = xup.user_id
left join xt_company_profile xcp on xcp.company_id = xup.company_id
left join xt_partnership xp on xcp.company_id = xp.partner_company_id 
where xp.vendor_company_id = 769)
, b as (select * from xt_form xf join xt_form_submit xfs on xfs.form_id = xf.id 
left join xt_form_label xfl on xfl.form_id = xf.id 
left join xt_form_submit_single_choice xfssc on xfssc.form_label_id = xfl.id and xfssc.form_submit_id = xfs.id)
, c as (select * from xt_form xf join xt_form_submit xfs on xfs.form_id = xf.id 
left join xt_form_label xfl on xfl.form_id = xf.id 
left join xt_form_submit_single_choice xfssc on xfssc.form_label_id = xfl.id and xfssc.form_submit_id = xfs.id)
select distinct a.*,
case when b.label_name like 'Title%' then b.value end as "MDF Request",
case when c.label_name like 'Request Amount%' then c.value end as "Amount"
from a join b on a.form_submit_id = b.form_submit_id
join c on a.form_submit_id = c.form_submit_id
) foo where "MDF Request" is not null and "Amount" is not null;



