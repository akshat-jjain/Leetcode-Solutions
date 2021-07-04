Select Max(Salary) AS SecondHighestSalary from Employee Where Salary <> (Select Max(Salary) from Employee);
