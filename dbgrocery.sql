-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 18, 2023 at 09:21 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbgrocery`
--

-- --------------------------------------------------------

--
-- Table structure for table `brand`
--

CREATE TABLE `brand` (
  `BrandID` int(10) NOT NULL,
  `BrandName` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `brand`
--

INSERT INTO `brand` (`BrandID`, `BrandName`) VALUES
(1, 'Nabati'),
(2, 'Aqua'),
(3, 'Indomie'),
(4, 'Chitato'),
(5, 'Heineken '),
(6, 'Fiesta '),
(7, 'Ferrero Rocher'),
(8, 'Bintang'),
(9, 'Ultra Milk'),
(10, 'Bimoli'),
(11, 'Choki Choki ');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `EmployeeID` int(20) NOT NULL,
  `EmployeeName` varchar(20) NOT NULL,
  `Position` varchar(20) NOT NULL,
  `ContactInformation` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`EmployeeID`, `EmployeeName`, `Position`, `ContactInformation`) VALUES
(11111, 'Abdullah', 'Manager', '081919061004'),
(11112, 'Michelle', 'Cashier', '081293389167'),
(11113, 'Bessie', 'Cashier', '08114220164'),
(11114, 'Rafi', 'General Assistant', '082110764747'),
(11115, 'Prado', 'Part Time Cashier ', '0810514704488');

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `InventoryID` int(20) NOT NULL,
  `ProductID` int(20) NOT NULL,
  `RestockDate` date NOT NULL,
  `ShelfLocation` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`InventoryID`, `ProductID`, `RestockDate`, `ShelfLocation`) VALUES
(20001, 31, '2023-11-01', 'Aisle 1'),
(20002, 32, '2023-11-08', 'Aisle 2'),
(20003, 33, '2023-10-05', 'Aisle 3'),
(20004, 34, '2023-10-20', 'Aisle 3'),
(20005, 35, '2023-11-22', 'Aisle 5'),
(20006, 36, '2023-12-01', 'Aisle 1'),
(20007, 37, '2023-12-02', 'Aisle 3'),
(20008, 38, '2023-12-03', 'Aisle 5'),
(20009, 39, '2023-12-04', 'Aisle 2'),
(20010, 40, '2023-12-02', 'Aisle 6');

-- --------------------------------------------------------

--
-- Table structure for table `itempurchased`
--

CREATE TABLE `itempurchased` (
  `PurchasedID` int(20) NOT NULL,
  `TransactionID` int(20) NOT NULL,
  `ProductID` int(20) NOT NULL,
  `PurchasedQuantity` int(20) NOT NULL,
  `PurchasedPrice` int(20) NOT NULL,
  `TimeStamp` date NOT NULL,
  `Subtotal` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `itempurchased`
--

INSERT INTO `itempurchased` (`PurchasedID`, `TransactionID`, `ProductID`, `PurchasedQuantity`, `PurchasedPrice`, `TimeStamp`, `Subtotal`) VALUES
(50001, 70001, 35, 1, 50000, '2023-10-12', 50000),
(50002, 70001, 34, 1, 10000, '2023-10-12', 10000),
(50003, 70002, 33, 1, 2000, '2023-11-20', 2000),
(50004, 70002, 32, 1, 4000, '2023-11-20', 4000),
(50005, 70003, 32, 1, 4000, '2023-11-01', 4000),
(50006, 70003, 31, 1, 3000, '2023-11-01', 3000),
(50007, 70004, 34, 2, 10000, '2023-07-18', 20000),
(50008, 70005, 35, 2, 50000, '2023-09-22', 100000),
(50009, 70006, 37, 1, 60000, '2023-11-24', 60000),
(50010, 70006, 34, 4, 10000, '2023-11-24', 40000),
(50011, 70007, 38, 1, 45000, '2023-12-07', 45000),
(50012, 70007, 31, 5, 3000, '2023-12-07', 15000),
(50013, 70008, 36, 2, 40000, '2023-11-30', 80000),
(50014, 70008, 39, 1, 5000, '2023-11-30', 5000),
(50015, 70009, 32, 5, 4000, '2023-11-29', 20000),
(50016, 70009, 40, 1, 55000, '2023-11-29', 55000),
(50017, 70009, 33, 25, 2000, '2023-11-29', 50000),
(50018, 70010, 39, 1, 5000, '2023-11-28', 5000),
(50019, 70010, 33, 1, 2000, '2023-11-28', 2000),
(50020, 70010, 32, 8, 4000, '2023-11-28', 32000),
(50021, 70010, 31, 6, 3000, '2023-11-28', 18000);

-- --------------------------------------------------------

--
-- Table structure for table `productname`
--

CREATE TABLE `productname` (
  `ProductID` int(20) NOT NULL,
  `BrandID` int(20) NOT NULL,
  `StockQuantity` int(20) NOT NULL,
  `Price` int(20) NOT NULL,
  `Category` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `productname`
--

INSERT INTO `productname` (`ProductID`, `BrandID`, `StockQuantity`, `Price`, `Category`) VALUES
(31, 3, 200, 3000, 'Instant Food'),
(32, 2, 100, 4000, 'Beverages'),
(33, 1, 50, 2000, 'Snacks'),
(34, 4, 25, 10000, 'Snacks'),
(35, 5, 15, 50000, 'Alcohol'),
(36, 6, 45, 40000, 'Instant Food'),
(37, 7, 25, 60000, 'Snacks'),
(38, 8, 20, 45000, 'Alcohol'),
(39, 9, 100, 5000, 'Beverages'),
(40, 10, 75, 55000, 'Cooking Supply'),
(41, 11, 30, 1000, 'Snacks');

-- --------------------------------------------------------

--
-- Table structure for table `salestransaction`
--

CREATE TABLE `salestransaction` (
  `TransactionID` int(20) NOT NULL,
  `TransactionDate` date NOT NULL,
  `EmployeeID` int(20) NOT NULL,
  `TotalAmount` int(20) NOT NULL,
  `PaymentStatus` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `salestransaction`
--

INSERT INTO `salestransaction` (`TransactionID`, `TransactionDate`, `EmployeeID`, `TotalAmount`, `PaymentStatus`) VALUES
(70001, '2023-10-12', 11111, 60000, 'Successful'),
(70002, '2023-11-20', 11112, 6000, 'Successful'),
(70003, '2023-11-01', 11113, 7000, 'Successful'),
(70004, '2023-07-18', 11114, 20000, 'Successful'),
(70005, '2023-09-22', 11115, 100000, 'Unsuccessful'),
(70006, '2023-11-24', 11115, 105000, 'Successful'),
(70007, '2023-12-07', 11111, 60000, 'Unsuccessful'),
(70008, '2023-11-30', 11112, 85000, 'Unsuccessful'),
(70009, '2023-11-29', 11113, 125000, 'Successful'),
(70010, '2023-11-28', 11114, 57000, 'Unsuccessful');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `brand`
--
ALTER TABLE `brand`
  ADD PRIMARY KEY (`BrandID`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`EmployeeID`);

--
-- Indexes for table `inventory`
--
ALTER TABLE `inventory`
  ADD PRIMARY KEY (`InventoryID`),
  ADD KEY `ProductID` (`ProductID`);

--
-- Indexes for table `itempurchased`
--
ALTER TABLE `itempurchased`
  ADD PRIMARY KEY (`PurchasedID`),
  ADD KEY `PurchasedProductID` (`ProductID`),
  ADD KEY `TransactionID` (`TransactionID`);

--
-- Indexes for table `productname`
--
ALTER TABLE `productname`
  ADD PRIMARY KEY (`ProductID`),
  ADD KEY `BrandID` (`BrandID`);

--
-- Indexes for table `salestransaction`
--
ALTER TABLE `salestransaction`
  ADD PRIMARY KEY (`TransactionID`),
  ADD KEY `EmployeeID` (`EmployeeID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `inventory`
--
ALTER TABLE `inventory`
  ADD CONSTRAINT `ProductID` FOREIGN KEY (`ProductID`) REFERENCES `productname` (`ProductID`);

--
-- Constraints for table `itempurchased`
--
ALTER TABLE `itempurchased`
  ADD CONSTRAINT `PurchasedProductID` FOREIGN KEY (`ProductID`) REFERENCES `productname` (`ProductID`),
  ADD CONSTRAINT `TransactionID` FOREIGN KEY (`TransactionID`) REFERENCES `salestransaction` (`TransactionID`);

--
-- Constraints for table `productname`
--
ALTER TABLE `productname`
  ADD CONSTRAINT `BrandID` FOREIGN KEY (`BrandID`) REFERENCES `brand` (`BrandID`);

--
-- Constraints for table `salestransaction`
--
ALTER TABLE `salestransaction`
  ADD CONSTRAINT `EmployeeID` FOREIGN KEY (`EmployeeID`) REFERENCES `employee` (`EmployeeID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
