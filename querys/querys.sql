--QUERYS BASICAS

-- Contar los estudiantes
SELECT COUNT(DISTINCT student_id) as total_estudiantes
FROM students_grades;

-- Seleccionar promedio de alumnos
SELECT name, average 
FROM students_grades; 

-- Seleccionar alumnos aprobados
SELECT DISTINCT name, average, status 
FROM students_grades
WHERE status='PASS';

-- Seleccionar estudiantes desaprobados
SELECT DISTINCT name, average, status
FROM students_grades
WHERE status='NO PASS';

