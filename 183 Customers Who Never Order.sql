Select
  C.Name as Customers
from
  Customers as C
where
  C.id Not in (
    Select
      customerId
    from
      Orders
  );
