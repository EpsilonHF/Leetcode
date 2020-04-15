/* Employees Earning More Than Their Managers

The Employee table holds all employees including their managers. Every 
employee has an Id, and there is also a column for the manager Id.

+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+
Given the Employee table, write a SQL query that finds out employees 
who earn more than their managers. For the above table, Joe is the only 
employee who earns more than his manager.

+----------+
| Employee |
+----------+
| Joe      |
+----------+ */

SELECT E1.Name AS Employee
FROM Employee AS E1, Employee AS E2
WHERE E1.ManagerId = E2.Id
AND E1.Salary > E2.Salary;
