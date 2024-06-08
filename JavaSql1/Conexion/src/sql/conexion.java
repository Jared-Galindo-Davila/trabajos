/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package sql;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class conexion {

    public static void main(String[] args) throws ClassNotFoundException, SQLException {
        String jdbcURL = "jdbc:sqlserver://DESKTOP-L0FS1RQ\\MSSQL:1433;databaseName=Northwind;encrypt=true;trustServerCertificate=true; ";
        String username = "soporte";
        String password = "12345";

        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");

            Connection connection = DriverManager.getConnection(jdbcURL, username, password);
            if (connection != null) {
                System.out.println("conexion exitosa a la base de datos.\n");
                System.out.println("Datos de la tabla Employees:");
                Statement statementEmployees = connection.createStatement();
                ResultSet resultSetEmployees = statementEmployees.executeQuery("SELECT * FROM Employees");
                while (resultSetEmployees.next()) {
                    System.out.println("EmployeeID: " + resultSetEmployees.getInt("EmployeeID"));
                    System.out.println("LastName: " + resultSetEmployees.getString("LastName"));
                    System.out.println("FirstName: " + resultSetEmployees.getString("FirstName"));
                    System.out.println("Title: " + resultSetEmployees.getString("Title"));
                    System.out.println("--------------------");
                }
                resultSetEmployees.close();
                statementEmployees.close();

                System.out.println("\nDatos de la tabla Customers:");
                Statement statementCustomers = connection.createStatement();
                ResultSet resultSetCustomers = statementCustomers.executeQuery("SELECT * FROM Customers");
                while (resultSetCustomers.next()) {
                    System.out.println("CustomerID: " + resultSetCustomers.getString("CustomerID"));
                    System.out.println("CompanyName: " + resultSetCustomers.getString("CompanyName"));
                    System.out.println("ContactName: " + resultSetCustomers.getString("ContactName"));
                    System.out.println("City: " + resultSetCustomers.getString("City"));
                    System.out.println("--------------------");
                }
                resultSetCustomers.close();
                statementCustomers.close();

                System.out.println("\nDatos de la tabla Orders:");
                Statement statementOrders = connection.createStatement();
                ResultSet resultSetOrders = statementOrders.executeQuery("SELECT * FROM Orders");
                while (resultSetOrders.next()) {
                    System.out.println("OrderID: " + resultSetOrders.getInt("OrderID"));
                    System.out.println("CustomerID: " + resultSetOrders.getString("CustomerID"));
                    System.out.println("EmployeeID: " + resultSetOrders.getInt("EmployeeID"));
                    System.out.println("OrderDate: " + resultSetOrders.getString("OrderDate"));
                    System.out.println("--------------------");
                }
                resultSetOrders.close();
                statementOrders.close();
                connection.close(); // Cerrar conexión

            }
        } catch (ClassNotFoundException e) {
            System.out.println("error al cargar el JDBC: " + e.getMessage());
        } catch (SQLException e) {
            System.out.println("error de SQL:" + e.getMessage());
        }
    }
}
