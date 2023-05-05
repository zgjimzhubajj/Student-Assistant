-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: student_assistant
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `course_ab_es`
--

DROP TABLE IF EXISTS `course_ab_es`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course_ab_es` (
  `course_id` int NOT NULL AUTO_INCREMENT,
  `course_name` varchar(50) NOT NULL,
  `course_year` int NOT NULL,
  `program_id` int NOT NULL,
  PRIMARY KEY (`course_id`),
  KEY `program_id` (`program_id`),
  CONSTRAINT `course_ab_es_ibfk_1` FOREIGN KEY (`program_id`) REFERENCES `program_ab_es` (`program_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course_ab_es`
--

LOCK TABLES `course_ab_es` WRITE;
/*!40000 ALTER TABLE `course_ab_es` DISABLE KEYS */;
INSERT INTO `course_ab_es` VALUES (1,'java',1,2),(2,'python',1,2),(3,'agile',1,2),(4,'networking',2,2),(5,'security',3,2),(6,'anatomy',1,1),(7,'phisiology',2,1),(8,'pharmacology',3,1),(9,'radiology',4,1),(10,'surgery',5,1);
/*!40000 ALTER TABLE `course_ab_es` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `finished_homework_ab_es`
--

DROP TABLE IF EXISTS `finished_homework_ab_es`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `finished_homework_ab_es` (
  `homework_stat_id` int NOT NULL AUTO_INCREMENT,
  `homework_stat` tinyint(1) NOT NULL,
  `personal_id` varchar(10) DEFAULT NULL,
  `homework_id` int NOT NULL,
  PRIMARY KEY (`homework_stat_id`),
  KEY `personal_id` (`personal_id`),
  KEY `homework_id` (`homework_id`),
  CONSTRAINT `finished_homework_ab_es_ibfk_1` FOREIGN KEY (`personal_id`) REFERENCES `student_info` (`personal_id`),
  CONSTRAINT `finished_homework_ab_es_ibfk_2` FOREIGN KEY (`homework_id`) REFERENCES `homework_ab_es` (`homework_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `finished_homework_ab_es`
--

LOCK TABLES `finished_homework_ab_es` WRITE;
/*!40000 ALTER TABLE `finished_homework_ab_es` DISABLE KEYS */;
/*!40000 ALTER TABLE `finished_homework_ab_es` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `homework_ab_es`
--

DROP TABLE IF EXISTS `homework_ab_es`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `homework_ab_es` (
  `homework_id` int NOT NULL AUTO_INCREMENT,
  `homework_name` varchar(50) NOT NULL,
  `homework_dead_line` date NOT NULL,
  `course_id` int NOT NULL,
  PRIMARY KEY (`homework_id`),
  KEY `course_id` (`course_id`),
  CONSTRAINT `homework_ab_es_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `course_ab_es` (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `homework_ab_es`
--

LOCK TABLES `homework_ab_es` WRITE;
/*!40000 ALTER TABLE `homework_ab_es` DISABLE KEYS */;
INSERT INTO `homework_ab_es` VALUES (1,'homework1','2023-05-15',1),(2,'homework2','2023-05-16',2),(3,'homework3','2023-05-17',3),(4,'homework4','2023-05-18',4),(5,'homework5','2023-05-19',5),(6,'homework6','2023-05-20',6),(7,'homework7','2023-05-21',7),(8,'homework8','2023-05-22',8),(9,'homework9','2023-05-23',9),(10,'homework10','2023-05-24',10);
/*!40000 ALTER TABLE `homework_ab_es` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `homework_notes_ab_es`
--

DROP TABLE IF EXISTS `homework_notes_ab_es`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `homework_notes_ab_es` (
  `note_id` int NOT NULL AUTO_INCREMENT,
  `not_text` text NOT NULL,
  `personal_id` varchar(10) NOT NULL,
  `homework_id` int NOT NULL,
  PRIMARY KEY (`note_id`),
  KEY `personal_id` (`personal_id`),
  KEY `homework_id` (`homework_id`),
  CONSTRAINT `homework_notes_ab_es_ibfk_1` FOREIGN KEY (`personal_id`) REFERENCES `student_info` (`personal_id`),
  CONSTRAINT `homework_notes_ab_es_ibfk_2` FOREIGN KEY (`homework_id`) REFERENCES `homework_ab_es` (`homework_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `homework_notes_ab_es`
--

LOCK TABLES `homework_notes_ab_es` WRITE;
/*!40000 ALTER TABLE `homework_notes_ab_es` DISABLE KEYS */;
/*!40000 ALTER TABLE `homework_notes_ab_es` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pdf_files_mil`
--

DROP TABLE IF EXISTS `pdf_files_mil`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pdf_files_mil` (
  `id` int NOT NULL AUTO_INCREMENT,
  `file_name` varchar(255) NOT NULL,
  `file_data` longblob NOT NULL,
  `course_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `course_id` (`course_id`),
  CONSTRAINT `pdf_files_mil_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `course_ab_es` (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pdf_files_mil`
--

LOCK TABLES `pdf_files_mil` WRITE;
/*!40000 ALTER TABLE `pdf_files_mil` DISABLE KEYS */;
INSERT INTO `pdf_files_mil` VALUES (1,'Lecture1_java.pdf',_binary '%PDF-1.4\n%\Ó\ë\é\á\n1 0 obj\n<</Title (Lecture1_java)\n/Producer (Skia/PDF m114 Google Docs Renderer)>>\nendobj\n3 0 obj\n<</ca 1\n/BM /Normal>>\nendobj\n4 0 obj\n<</Length 84>> stream\n1 0 0 -1 0 792 cm\nq\n.75 0 0 .75 0 0 cm\n1 1 1 RG 1 1 1 rg\n/G3 gs\n0 0 816 1056 re\nf\nQ\n\nendstream\nendobj\n2 0 obj\n<</Type /Page\n/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]\n/ExtGState <</G3 3 0 R>>>>\n/MediaBox [0 0 612 792]\n/Contents 4 0 R\n/StructParents 0\n/Parent 5 0 R>>\nendobj\n5 0 obj\n<</Type /Pages\n/Count 1\n/Kids [2 0 R]>>\nendobj\n6 0 obj\n<</Type /Catalog\n/Pages 5 0 R>>\nendobj\nxref\n0 7\n0000000000 65535 f \n0000000015 00000 n \n0000000273 00000 n \n0000000104 00000 n \n0000000141 00000 n \n0000000461 00000 n \n0000000516 00000 n \ntrailer\n<</Size 7\n/Root 6 0 R\n/Info 1 0 R>>\nstartxref\n563\n%%EOF\n',1),(2,'Lecture1_python.pdf',_binary '%PDF-1.4\n%\Ó\ë\é\á\n1 0 obj\n<</Title (Lecture1_python)\n/Producer (Skia/PDF m114 Google Docs Renderer)>>\nendobj\n3 0 obj\n<</ca 1\n/BM /Normal>>\nendobj\n4 0 obj\n<</Length 84>> stream\n1 0 0 -1 0 792 cm\nq\n.75 0 0 .75 0 0 cm\n1 1 1 RG 1 1 1 rg\n/G3 gs\n0 0 816 1056 re\nf\nQ\n\nendstream\nendobj\n2 0 obj\n<</Type /Page\n/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]\n/ExtGState <</G3 3 0 R>>>>\n/MediaBox [0 0 612 792]\n/Contents 4 0 R\n/StructParents 0\n/Parent 5 0 R>>\nendobj\n5 0 obj\n<</Type /Pages\n/Count 1\n/Kids [2 0 R]>>\nendobj\n6 0 obj\n<</Type /Catalog\n/Pages 5 0 R>>\nendobj\nxref\n0 7\n0000000000 65535 f \n0000000015 00000 n \n0000000275 00000 n \n0000000106 00000 n \n0000000143 00000 n \n0000000463 00000 n \n0000000518 00000 n \ntrailer\n<</Size 7\n/Root 6 0 R\n/Info 1 0 R>>\nstartxref\n565\n%%EOF\n',2),(3,'Lecture1_agile.pdf',_binary '%PDF-1.4\n%\Ó\ë\é\á\n1 0 obj\n<</Title (Lecture1_agile)\n/Producer (Skia/PDF m114 Google Docs Renderer)>>\nendobj\n3 0 obj\n<</ca 1\n/BM /Normal>>\nendobj\n4 0 obj\n<</Length 84>> stream\n1 0 0 -1 0 792 cm\nq\n.75 0 0 .75 0 0 cm\n1 1 1 RG 1 1 1 rg\n/G3 gs\n0 0 816 1056 re\nf\nQ\n\nendstream\nendobj\n2 0 obj\n<</Type /Page\n/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]\n/ExtGState <</G3 3 0 R>>>>\n/MediaBox [0 0 612 792]\n/Contents 4 0 R\n/StructParents 0\n/Parent 5 0 R>>\nendobj\n5 0 obj\n<</Type /Pages\n/Count 1\n/Kids [2 0 R]>>\nendobj\n6 0 obj\n<</Type /Catalog\n/Pages 5 0 R>>\nendobj\nxref\n0 7\n0000000000 65535 f \n0000000015 00000 n \n0000000274 00000 n \n0000000105 00000 n \n0000000142 00000 n \n0000000462 00000 n \n0000000517 00000 n \ntrailer\n<</Size 7\n/Root 6 0 R\n/Info 1 0 R>>\nstartxref\n564\n%%EOF\n',3),(4,'Lecture1_networking.pdf',_binary '%PDF-1.4\n%\Ó\ë\é\á\n1 0 obj\n<</Title (Lecture1_networking)\n/Producer (Skia/PDF m114 Google Docs Renderer)>>\nendobj\n3 0 obj\n<</ca 1\n/BM /Normal>>\nendobj\n4 0 obj\n<</Length 84>> stream\n1 0 0 -1 0 792 cm\nq\n.75 0 0 .75 0 0 cm\n1 1 1 RG 1 1 1 rg\n/G3 gs\n0 0 816 1056 re\nf\nQ\n\nendstream\nendobj\n2 0 obj\n<</Type /Page\n/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]\n/ExtGState <</G3 3 0 R>>>>\n/MediaBox [0 0 612 792]\n/Contents 4 0 R\n/StructParents 0\n/Parent 5 0 R>>\nendobj\n5 0 obj\n<</Type /Pages\n/Count 1\n/Kids [2 0 R]>>\nendobj\n6 0 obj\n<</Type /Catalog\n/Pages 5 0 R>>\nendobj\nxref\n0 7\n0000000000 65535 f \n0000000015 00000 n \n0000000279 00000 n \n0000000110 00000 n \n0000000147 00000 n \n0000000467 00000 n \n0000000522 00000 n \ntrailer\n<</Size 7\n/Root 6 0 R\n/Info 1 0 R>>\nstartxref\n569\n%%EOF\n',4),(5,'Lecture1_security.pdf',_binary '%PDF-1.4\n%\Ó\ë\é\á\n1 0 obj\n<</Title (Lecture1_security)\n/Producer (Skia/PDF m114 Google Docs Renderer)>>\nendobj\n3 0 obj\n<</ca 1\n/BM /Normal>>\nendobj\n4 0 obj\n<</Length 84>> stream\n1 0 0 -1 0 792 cm\nq\n.75 0 0 .75 0 0 cm\n1 1 1 RG 1 1 1 rg\n/G3 gs\n0 0 816 1056 re\nf\nQ\n\nendstream\nendobj\n2 0 obj\n<</Type /Page\n/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]\n/ExtGState <</G3 3 0 R>>>>\n/MediaBox [0 0 612 792]\n/Contents 4 0 R\n/StructParents 0\n/Parent 5 0 R>>\nendobj\n5 0 obj\n<</Type /Pages\n/Count 1\n/Kids [2 0 R]>>\nendobj\n6 0 obj\n<</Type /Catalog\n/Pages 5 0 R>>\nendobj\nxref\n0 7\n0000000000 65535 f \n0000000015 00000 n \n0000000277 00000 n \n0000000108 00000 n \n0000000145 00000 n \n0000000465 00000 n \n0000000520 00000 n \ntrailer\n<</Size 7\n/Root 6 0 R\n/Info 1 0 R>>\nstartxref\n567\n%%EOF\n',5),(6,'Lecture1_anatomy.pdf',_binary '%PDF-1.4\n%\Ó\ë\é\á\n1 0 obj\n<</Title (Lecture1_anatomy)\n/Producer (Skia/PDF m114 Google Docs Renderer)>>\nendobj\n3 0 obj\n<</ca 1\n/BM /Normal>>\nendobj\n4 0 obj\n<</Length 84>> stream\n1 0 0 -1 0 792 cm\nq\n.75 0 0 .75 0 0 cm\n1 1 1 RG 1 1 1 rg\n/G3 gs\n0 0 816 1056 re\nf\nQ\n\nendstream\nendobj\n2 0 obj\n<</Type /Page\n/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]\n/ExtGState <</G3 3 0 R>>>>\n/MediaBox [0 0 612 792]\n/Contents 4 0 R\n/StructParents 0\n/Parent 5 0 R>>\nendobj\n5 0 obj\n<</Type /Pages\n/Count 1\n/Kids [2 0 R]>>\nendobj\n6 0 obj\n<</Type /Catalog\n/Pages 5 0 R>>\nendobj\nxref\n0 7\n0000000000 65535 f \n0000000015 00000 n \n0000000276 00000 n \n0000000107 00000 n \n0000000144 00000 n \n0000000464 00000 n \n0000000519 00000 n \ntrailer\n<</Size 7\n/Root 6 0 R\n/Info 1 0 R>>\nstartxref\n566\n%%EOF\n',6),(7,'Lecture1_phisiology.pdf',_binary '%PDF-1.4\n%\Ó\ë\é\á\n1 0 obj\n<</Title (Lecture1_phisiology)\n/Producer (Skia/PDF m114 Google Docs Renderer)>>\nendobj\n3 0 obj\n<</ca 1\n/BM /Normal>>\nendobj\n4 0 obj\n<</Length 84>> stream\n1 0 0 -1 0 792 cm\nq\n.75 0 0 .75 0 0 cm\n1 1 1 RG 1 1 1 rg\n/G3 gs\n0 0 816 1056 re\nf\nQ\n\nendstream\nendobj\n2 0 obj\n<</Type /Page\n/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]\n/ExtGState <</G3 3 0 R>>>>\n/MediaBox [0 0 612 792]\n/Contents 4 0 R\n/StructParents 0\n/Parent 5 0 R>>\nendobj\n5 0 obj\n<</Type /Pages\n/Count 1\n/Kids [2 0 R]>>\nendobj\n6 0 obj\n<</Type /Catalog\n/Pages 5 0 R>>\nendobj\nxref\n0 7\n0000000000 65535 f \n0000000015 00000 n \n0000000279 00000 n \n0000000110 00000 n \n0000000147 00000 n \n0000000467 00000 n \n0000000522 00000 n \ntrailer\n<</Size 7\n/Root 6 0 R\n/Info 1 0 R>>\nstartxref\n569\n%%EOF\n',7),(8,'Lecture1_pharmacology.pdf',_binary '%PDF-1.4\n%\Ó\ë\é\á\n1 0 obj\n<</Title (Lecture1_pharmacology)\n/Producer (Skia/PDF m114 Google Docs Renderer)>>\nendobj\n3 0 obj\n<</ca 1\n/BM /Normal>>\nendobj\n4 0 obj\n<</Length 84>> stream\n1 0 0 -1 0 792 cm\nq\n.75 0 0 .75 0 0 cm\n1 1 1 RG 1 1 1 rg\n/G3 gs\n0 0 816 1056 re\nf\nQ\n\nendstream\nendobj\n2 0 obj\n<</Type /Page\n/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]\n/ExtGState <</G3 3 0 R>>>>\n/MediaBox [0 0 612 792]\n/Contents 4 0 R\n/StructParents 0\n/Parent 5 0 R>>\nendobj\n5 0 obj\n<</Type /Pages\n/Count 1\n/Kids [2 0 R]>>\nendobj\n6 0 obj\n<</Type /Catalog\n/Pages 5 0 R>>\nendobj\nxref\n0 7\n0000000000 65535 f \n0000000015 00000 n \n0000000281 00000 n \n0000000112 00000 n \n0000000149 00000 n \n0000000469 00000 n \n0000000524 00000 n \ntrailer\n<</Size 7\n/Root 6 0 R\n/Info 1 0 R>>\nstartxref\n571\n%%EOF\n',8),(9,'Lecture1_radiology.pdf',_binary '%PDF-1.4\n%\Ó\ë\é\á\n1 0 obj\n<</Title (Lecture1_radiology)\n/Producer (Skia/PDF m114 Google Docs Renderer)>>\nendobj\n3 0 obj\n<</ca 1\n/BM /Normal>>\nendobj\n4 0 obj\n<</Length 84>> stream\n1 0 0 -1 0 792 cm\nq\n.75 0 0 .75 0 0 cm\n1 1 1 RG 1 1 1 rg\n/G3 gs\n0 0 816 1056 re\nf\nQ\n\nendstream\nendobj\n2 0 obj\n<</Type /Page\n/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]\n/ExtGState <</G3 3 0 R>>>>\n/MediaBox [0 0 612 792]\n/Contents 4 0 R\n/StructParents 0\n/Parent 5 0 R>>\nendobj\n5 0 obj\n<</Type /Pages\n/Count 1\n/Kids [2 0 R]>>\nendobj\n6 0 obj\n<</Type /Catalog\n/Pages 5 0 R>>\nendobj\nxref\n0 7\n0000000000 65535 f \n0000000015 00000 n \n0000000278 00000 n \n0000000109 00000 n \n0000000146 00000 n \n0000000466 00000 n \n0000000521 00000 n \ntrailer\n<</Size 7\n/Root 6 0 R\n/Info 1 0 R>>\nstartxref\n568\n%%EOF\n',9),(10,'Lecture1_surgery.pdf',_binary '%PDF-1.4\n%\Ó\ë\é\á\n1 0 obj\n<</Title (Lecture1_surgery)\n/Producer (Skia/PDF m114 Google Docs Renderer)>>\nendobj\n3 0 obj\n<</ca 1\n/BM /Normal>>\nendobj\n4 0 obj\n<</Length 84>> stream\n1 0 0 -1 0 792 cm\nq\n.75 0 0 .75 0 0 cm\n1 1 1 RG 1 1 1 rg\n/G3 gs\n0 0 816 1056 re\nf\nQ\n\nendstream\nendobj\n2 0 obj\n<</Type /Page\n/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]\n/ExtGState <</G3 3 0 R>>>>\n/MediaBox [0 0 612 792]\n/Contents 4 0 R\n/StructParents 0\n/Parent 5 0 R>>\nendobj\n5 0 obj\n<</Type /Pages\n/Count 1\n/Kids [2 0 R]>>\nendobj\n6 0 obj\n<</Type /Catalog\n/Pages 5 0 R>>\nendobj\nxref\n0 7\n0000000000 65535 f \n0000000015 00000 n \n0000000276 00000 n \n0000000107 00000 n \n0000000144 00000 n \n0000000464 00000 n \n0000000519 00000 n \ntrailer\n<</Size 7\n/Root 6 0 R\n/Info 1 0 R>>\nstartxref\n566\n%%EOF\n',10);
/*!40000 ALTER TABLE `pdf_files_mil` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `program_ab_es`
--

DROP TABLE IF EXISTS `program_ab_es`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `program_ab_es` (
  `program_id` int NOT NULL AUTO_INCREMENT,
  `program_name` varchar(50) NOT NULL,
  `program_year` int NOT NULL,
  PRIMARY KEY (`program_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `program_ab_es`
--

LOCK TABLES `program_ab_es` WRITE;
/*!40000 ALTER TABLE `program_ab_es` DISABLE KEYS */;
INSERT INTO `program_ab_es` VALUES (1,'Medicine',5),(2,'Programing',3);
/*!40000 ALTER TABLE `program_ab_es` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `session_ab_es`
--

DROP TABLE IF EXISTS `session_ab_es`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `session_ab_es` (
  `session_id` int NOT NULL AUTO_INCREMENT,
  `session_name` varchar(50) DEFAULT NULL,
  `personal_id` varchar(10) NOT NULL,
  PRIMARY KEY (`session_id`),
  KEY `personal_id` (`personal_id`),
  CONSTRAINT `session_ab_es_ibfk_1` FOREIGN KEY (`personal_id`) REFERENCES `student_info` (`personal_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `session_ab_es`
--

LOCK TABLES `session_ab_es` WRITE;
/*!40000 ALTER TABLE `session_ab_es` DISABLE KEYS */;
/*!40000 ALTER TABLE `session_ab_es` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_course_ab_es`
--

DROP TABLE IF EXISTS `student_course_ab_es`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_course_ab_es` (
  `personal_id` varchar(10) NOT NULL,
  `course_id` int NOT NULL,
  PRIMARY KEY (`personal_id`,`course_id`),
  KEY `course_id` (`course_id`),
  CONSTRAINT `student_course_ab_es_ibfk_1` FOREIGN KEY (`personal_id`) REFERENCES `student_info` (`personal_id`),
  CONSTRAINT `student_course_ab_es_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `course_ab_es` (`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_course_ab_es`
--

LOCK TABLES `student_course_ab_es` WRITE;
/*!40000 ALTER TABLE `student_course_ab_es` DISABLE KEYS */;
INSERT INTO `student_course_ab_es` VALUES ('2345678901',1),('2345678901',2),('2345678901',3),('2345678901',4),('2345678901',5),('1234567890',6),('1234567890',7),('1234567890',8),('1234567890',9),('1234567890',10);
/*!40000 ALTER TABLE `student_course_ab_es` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_info`
--

DROP TABLE IF EXISTS `student_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_info` (
  `personal_id` varchar(10) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `program_name` varchar(50) NOT NULL,
  `year_of_study` int NOT NULL,
  PRIMARY KEY (`personal_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_info`
--

LOCK TABLES `student_info` WRITE;
/*!40000 ALTER TABLE `student_info` DISABLE KEYS */;
INSERT INTO `student_info` VALUES ('0123456789','lik','oj','liko','Wle','je@gmail.com','Programing',1),('1234567890','bb','aa','kilo','lil','kd@gmail.com','Medicine',1),('2345678901','aa','bb','loki','lol','lkf@gmail.com','Programing',1);
/*!40000 ALTER TABLE `student_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_session_ab_es`
--

DROP TABLE IF EXISTS `student_session_ab_es`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_session_ab_es` (
  `personal_id` varchar(10) NOT NULL,
  `session_id` int NOT NULL,
  PRIMARY KEY (`personal_id`,`session_id`),
  KEY `session_id` (`session_id`),
  CONSTRAINT `student_session_ab_es_ibfk_1` FOREIGN KEY (`personal_id`) REFERENCES `student_info` (`personal_id`),
  CONSTRAINT `student_session_ab_es_ibfk_2` FOREIGN KEY (`session_id`) REFERENCES `session_ab_es` (`session_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_session_ab_es`
--

LOCK TABLES `student_session_ab_es` WRITE;
/*!40000 ALTER TABLE `student_session_ab_es` DISABLE KEYS */;
/*!40000 ALTER TABLE `student_session_ab_es` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-05 13:17:15
